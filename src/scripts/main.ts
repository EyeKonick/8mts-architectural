import { initHeader, initMenu } from './header';
import { initFaq } from './faq';
import { initPackageLinks, initQuoteForm } from './quote';
import { initFx } from './fx';

// Tell the fail-safe in Layout.astro that the motion layer is running.
document.documentElement.classList.add('motion-ready');

// Button labels: wrap the text so CSS can roll a copy of it up on hover.
document.querySelectorAll<HTMLElement>('.btn__label').forEach((label) => {
	const text = label.textContent?.trim() ?? '';
	const inner = document.createElement('span');
	inner.dataset.text = text;
	inner.textContent = text;
	label.replaceChildren(inner);
});

initHeader();
initMenu();
initFaq();
initPackageLinks();
initQuoteForm();
initFx();
