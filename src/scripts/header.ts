import { onScroll } from './motion';

/** The fixed bar: a hairline once the page moves, and a pill that slides to the hovered link. */
export function initHeader() {
	const header = document.querySelector<HTMLElement>('[data-header]');
	if (!header) return;
	onScroll((y) => header.classList.toggle('is-scrolled', y > 8));

	const nav = header.querySelector<HTMLElement>('[data-pill-nav]');
	const indicator = nav?.querySelector<HTMLElement>('[data-pill-indicator]');
	if (!nav || !indicator) return;
	const links = [...nav.querySelectorAll<HTMLAnchorElement>('[data-nav-link]')];
	let current: HTMLAnchorElement | null = null;

	const moveTo = (link: HTMLAnchorElement | null) => {
		links.forEach((l) => l.classList.toggle('is-lit', l === link));
		if (!link) {
			indicator.style.opacity = '0';
			return;
		}
		indicator.style.opacity = '1';
		indicator.style.width = `${link.offsetWidth}px`;
		indicator.style.transform = `translateX(${link.offsetLeft}px)`;
	};

	links.forEach((link) => {
		link.addEventListener('pointerenter', () => moveTo(link));
		link.addEventListener('focus', () => moveTo(link));
	});
	nav.addEventListener('pointerleave', () => moveTo(current));
	nav.addEventListener('focusout', (e) => {
		if (!nav.contains(e.relatedTarget as Node)) moveTo(current);
	});
	window.addEventListener('resize', () => moveTo(current));

	// The pill rests on the link of the section in the middle of the screen.
	const sections = links
		.map((l) => document.getElementById(new URL(l.href).hash.slice(1)))
		.filter((s): s is HTMLElement => !!s);
	const io = new IntersectionObserver(
		(entries) => {
			for (const entry of entries) {
				if (!entry.isIntersecting) continue;
				const id = (entry.target as HTMLElement).id;
				current = links.find((l) => l.hash === `#${id}`) ?? null;
				links.forEach((l) => l.setAttribute('aria-current', String(l === current)));
				if (!nav.matches(':hover')) moveTo(current);
			}
		},
		{ rootMargin: '-50% 0px -49% 0px' },
	);
	sections.forEach((s) => io.observe(s));
	// Sections without a nav link clear the pill.
	document.querySelectorAll<HTMLElement>('main > section, footer.closing').forEach((s) => {
		if (sections.includes(s)) return;
		new IntersectionObserver(
			(entries) => {
				if (!entries[0].isIntersecting) return;
				current = null;
				links.forEach((l) => l.setAttribute('aria-current', 'false'));
				if (!nav.matches(':hover')) moveTo(null);
			},
			{ rootMargin: '-50% 0px -49% 0px' },
		).observe(s);
	});
}

/** The full-screen menu on tablets and phones. */
export function initMenu() {
	const toggle = document.querySelector<HTMLButtonElement>('[data-menu-toggle]');
	const menu = document.querySelector<HTMLElement>('[data-menu]');
	if (!toggle || !menu) return;
	const root = document.documentElement;
	const main = document.getElementById('main');
	const footer = document.querySelector<HTMLElement>('footer');
	menu.inert = true;

	const setOpen = (open: boolean) => {
		if (open === root.classList.contains('menu-open')) return;
		root.classList.toggle('menu-open', open);
		toggle.setAttribute('aria-expanded', String(open));
		toggle.setAttribute('aria-label', open ? 'Close the menu' : 'Open the menu');
		menu.inert = !open;
		if (main) main.inert = open;
		if (footer) footer.inert = open;
		root.style.overflow = open ? 'hidden' : '';
		if (open) menu.querySelector<HTMLElement>('a')?.focus({ preventScroll: true });
	};

	toggle.addEventListener('click', () => setOpen(!root.classList.contains('menu-open')));
	menu.addEventListener('click', (e) => {
		if ((e.target as Element).closest('a')) setOpen(false);
	});
	document.addEventListener('keydown', (e) => {
		if (e.key === 'Escape' && root.classList.contains('menu-open')) {
			setOpen(false);
			toggle.focus();
		}
	});
	window.matchMedia('(min-width: 1024px)').addEventListener('change', (e) => {
		if (e.matches) setOpen(false);
	});
}
