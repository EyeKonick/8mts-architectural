import { reduceMotion } from './motion';

/** FAQ: <details> that open and close with a height animation instead of a jump. */
export function initFaq() {
	document.querySelectorAll<HTMLDetailsElement>('[data-faq] details').forEach((d) => {
		const summary = d.querySelector('summary');
		const body = d.querySelector<HTMLElement>('.qa__a');
		if (!summary || !body || reduceMotion) return;
		let anim: Animation | null = null;

		summary.addEventListener('click', (e) => {
			e.preventDefault();
			anim?.cancel();
			if (d.open) {
				const h = body.offsetHeight;
				anim = body.animate({ height: [`${h}px`, '0px'], opacity: [1, 0] }, { duration: 320, easing: 'cubic-bezier(0.22,1,0.36,1)' });
				anim.onfinish = () => {
					d.open = false;
					anim = null;
				};
			} else {
				d.open = true;
				const h = body.offsetHeight;
				anim = body.animate({ height: ['0px', `${h}px`], opacity: [0, 1] }, { duration: 420, easing: 'cubic-bezier(0.22,1,0.36,1)' });
				anim.onfinish = () => (anim = null);
			}
		});
	});
}
