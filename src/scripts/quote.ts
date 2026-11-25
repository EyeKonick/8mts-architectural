import { haptic, reduceMotion } from './motion';

type Field = HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement;
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

/** "Request this package" links pick the package in the quote form on the way down. */
export function initPackageLinks() {
	const select = document.querySelector<HTMLSelectElement>('[data-package-select]');
	if (!select) return;
	document.querySelectorAll<HTMLElement>('[data-package], [data-service]').forEach((link) => {
		link.addEventListener('click', () => {
			const wanted = link.dataset.package ?? '';
			const service = link.dataset.service ?? '';
			const options = [...select.options].map((o) => o.value);
			let value = options.find((o) => o.toLowerCase() === wanted.toLowerCase()) ?? '';
			if (!value && service) {
				const s = service.toLowerCase();
				if (s.includes('3d')) value = '3D visualization';
				else if (s.includes('consultation')) value = 'Design consultation';
				else if (s.includes('as-built')) value = 'As-built package';
				else if (s.includes('interior') && !s.includes('fit-out')) value = 'Condo and interior package';
				else if (s.includes('fit-out') || s.includes('kiosk')) value = 'Commercial fit-out or kiosk';
				else value = 'Building permit package';
			}
			if (value) {
				select.value = value;
				select.dispatchEvent(new Event('change'));
			}
		});
	});
}

function validate(field: Field): string {
	const value = field.value.trim();
	switch (field.name) {
		case 'name':
			return value.length >= 2 ? '' : 'Write your name, at least 2 letters.';
		case 'email':
			if (!value) return 'Write the email address we should reply to.';
			return EMAIL_RE.test(value) ? '' : 'Write the email in the form name@example.com.';
		case 'projectType':
			return value ? '' : 'Choose the package or service you need.';
		case 'message':
			if (value.length < 20) return `Say a little more about the project: at least 20 characters (${value.length} so far).`;
			return '';
		default:
			return '';
	}
}

/** Quote form: inline checks, then a form backend when one is set, else the visitor's email app. */
export function initQuoteForm() {
	const form = document.querySelector<HTMLFormElement>('[data-contact-form]');
	if (!form) return;
	const status = form.querySelector<HTMLElement>('[data-form-status]')!;
	const submit = form.querySelector<HTMLButtonElement>('[data-submit]')!;
	const fields = [...form.querySelectorAll<Field>('input:not([name="_gotcha"]), select, textarea')];
	const endpoint = form.dataset.endpoint?.trim();
	const studioEmail = form.dataset.email!;
	let attempted = false;

	const showError = (field: Field, message: string) => {
		const wrap = field.closest('.field');
		const el = wrap?.querySelector<HTMLElement>('.field__error');
		wrap?.classList.toggle('field--error', !!message);
		field.setAttribute('aria-invalid', String(!!message));
		if (el) el.textContent = message;
	};
	const check = (f: Field) => {
		const m = validate(f);
		showError(f, m);
		return !m;
	};
	fields.forEach((f) => {
		f.addEventListener('blur', () => {
			if (attempted || f.value) check(f);
		});
		f.addEventListener(f.tagName === 'SELECT' ? 'change' : 'input', () => {
			if (attempted || f.getAttribute('aria-invalid') === 'true') check(f);
		});
	});

	const setStatus = (text: string, state: 'idle' | 'success' | 'error' = 'idle') => {
		status.textContent = text;
		status.dataset.state = state;
		status.classList.remove('is-new');
		void status.offsetWidth;
		status.classList.add('is-new');
		if (state !== 'idle') haptic(state);
	};

	form.addEventListener('submit', async (e) => {
		e.preventDefault();
		attempted = true;
		const invalid = fields.filter((f) => !check(f));
		if (invalid.length) {
			setStatus(`Fix ${invalid.length === 1 ? '1 field' : `${invalid.length} fields`} before sending.`, 'error');
			if (!reduceMotion)
				invalid.forEach((f) => {
					const w = f.closest<HTMLElement>('.field');
					w?.classList.remove('field--shake');
					void w?.offsetWidth;
					w?.classList.add('field--shake');
				});
			invalid[0].focus();
			return;
		}
		if (form.querySelector<HTMLInputElement>('[name="_gotcha"]')?.value) return;

		const data = Object.fromEntries(new FormData(form).entries()) as Record<string, string>;
		delete data._gotcha;

		if (!endpoint) {
			const body = [
				`Name: ${data.name}`,
				`Email: ${data.email}`,
				`Package or service: ${data.projectType}`,
				`Location: ${data.location || 'Not given'}`,
				'',
				data.message,
			].join('\n');
			window.location.href = `mailto:${studioEmail}?subject=${encodeURIComponent(`Quote request: ${data.projectType}`)}&body=${encodeURIComponent(body)}`;
			setStatus(`Your email app opened with the request filled in. Press send there, or write to ${studioEmail}.`, 'success');
			return;
		}

		submit.disabled = true;
		setStatus('Sending your request…');
		try {
			const res = await fetch(endpoint, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
				body: JSON.stringify({ ...data, _subject: `Quote request: ${data.projectType}` }),
			});
			if (!res.ok) throw new Error(String(res.status));
			form.reset();
			attempted = false;
			fields.forEach((f) => showError(f, ''));
			setStatus('Your quote request is in. We reply by email with the scope and the quotation.', 'success');
		} catch {
			setStatus(`The request could not be sent. Try again, or write to ${studioEmail}.`, 'error');
		} finally {
			submit.disabled = false;
		}
	});
}
