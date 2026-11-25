/**
 * The page's motion layer: smooth scrolling, scroll reveals, image parallax, the progress
 * bar, the services band, the "View" badge over projects, magnetic buttons and the nav
 * colour over the dark hero. CSS (src/styles/fx.css) owns the look; this file only sets
 * classes and custom properties.
 *
 * Every hidden "before" state lives under html.fx-rv, which this script adds itself, so a
 * page whose script fails shows everything at rest. Reduced motion: none of it runs.
 */
import Lenis from 'lenis';
import 'lenis/dist/lenis.css';
import { onScroll, reduceMotion } from './motion';

const root = document.documentElement;
const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

/* ---------- smooth scrolling ---------- */

function initSmooth() {
	if (reduceMotion) return;
	const lenis = new Lenis({ autoRaf: true, lerp: 0.1, anchors: { offset: 0 } });
	// The mobile menu locks the page; let Lenis follow.
	new MutationObserver(() => {
		if (root.classList.contains('menu-open')) lenis.stop();
		else lenis.start();
	}).observe(root, { attributes: true, attributeFilter: ['class'] });
}

/* ---------- scroll reveals ---------- */

/** Wrap every word of a heading in a mask, keeping <em> and other inline elements intact. */
function splitWords(el: HTMLElement) {
	let n = 0;
	const walk = (node: Node) => {
		for (const child of [...node.childNodes]) {
			if (child.nodeType === Node.TEXT_NODE) {
				const parts = (child.textContent ?? '').split(/(\s+)/);
				const frag = document.createDocumentFragment();
				for (const part of parts) {
					if (!part) continue;
					if (/^\s+$/.test(part)) {
						frag.append(document.createTextNode(part));
						continue;
					}
					const mask = document.createElement('span');
					mask.className = 'rw';
					const inner = document.createElement('span');
					inner.style.setProperty('--wi', String(n++));
					inner.textContent = part;
					mask.append(inner);
					frag.append(mask);
				}
				child.replaceWith(frag);
			} else if (child.nodeType === Node.ELEMENT_NODE) {
				walk(child);
			}
		}
	};
	walk(el);
}

/** Groups of things that rise in one after another, by their parent. */
const RISE = [
	'main > section:not(.hero) .label',
	'.sec-head__lead',
	'.work',
	'.svc-list > li',
	'.plan',
	'.isheet',
	'.voice',
	'.step',
	'.qa',
	'.viz__side',
	'.viz__list > div',
	'.faq__head > p',
	'.quote__lead',
	'.quote__details > div',
	'.form .field',
	'.form__foot',
	'.close__head .btn',
	'.titleblock .tb',
];

function initReveals() {
	if (reduceMotion || !('IntersectionObserver' in window)) return;

	const items = new Set<HTMLElement>();
	const add = (el: HTMLElement, kind: string, i = 0) => {
		el.dataset.rv = kind;
		el.style.setProperty('--i', String(Math.min(i, 6)));
		items.add(el);
	};

	document.querySelectorAll<HTMLElement>('main > section:not(.hero) .h2, footer .h2').forEach((h) => {
		splitWords(h);
		add(h, 'words');
	});

	RISE.forEach((sel) => {
		const byParent = new Map<Element | null, number>();
		document.querySelectorAll<HTMLElement>(sel).forEach((el) => {
			if (el.closest('.hero') || items.has(el)) return;
			const i = byParent.get(el.parentElement) ?? 0;
			byParent.set(el.parentElement, i + 1);
			add(el, 'rise', i);
		});
	});

	// Photographs open with a wipe (the moment frames run their own entrance).
	document
		.querySelectorAll<HTMLElement>('main > section:not(.hero) .frame--photo, footer .frame--photo')
		.forEach((f) => {
			if (f.closest('[data-moment]:not(.statement)') || f.hasAttribute('data-moment')) return;
			add(f, 'wipe');
		});

	root.classList.add('fx-rv');

	const io = new IntersectionObserver(
		(entries) => {
			for (const e of entries) {
				if (!e.isIntersecting) continue;
				e.target.classList.add('is-in');
				io.unobserve(e.target);
			}
		},
		{ rootMargin: '0px 0px -10% 0px', threshold: 0.12 },
	);
	items.forEach((el) => io.observe(el));

	// Anything already above the fold (a reload half way down) shows at once.
	requestAnimationFrame(() => {
		items.forEach((el) => {
			if (el.getBoundingClientRect().bottom < 0) el.classList.add('is-in');
		});
	});
}

/* ---------- parallax inside photo frames ---------- */

function initParallax() {
	if (reduceMotion) return;
	const frames = [
		...document.querySelectorAll<HTMLElement>('.frame--photo:not([data-moment]):not(.hero__frame)'),
	].filter((f) => f.querySelector('img'));
	frames.forEach((f) => f.classList.add('fx-par'));
	const vh = () => window.innerHeight;
	onScroll(() => {
		const h = vh();
		for (const f of frames) {
			const r = f.getBoundingClientRect();
			if (r.bottom < -100 || r.top > h + 100) continue;
			// -1 when the frame enters at the bottom, +1 when it leaves at the top
			const p = (h - r.top) / (h + r.height) * 2 - 1;
			f.style.setProperty('--py', Math.max(-1, Math.min(1, p)).toFixed(3));
		}
	});
}

/* ---------- progress bar, services band, nav over the dark hero ---------- */

function initScrollBits() {
	const bar = document.querySelector<HTMLElement>('[data-progress]');
	const track = document.querySelector<HTMLElement>('[data-band-track]');
	const band = document.querySelector<HTMLElement>('[data-band]');
	const hero = document.querySelector<HTMLElement>('.hero');
	const nav = document.querySelector<HTMLElement>('[data-header]');

	onScroll((y) => {
		const max = root.scrollHeight - window.innerHeight;
		if (bar) bar.style.transform = `scaleX(${max > 0 ? (y / max).toFixed(4) : 0})`;

		if (hero && nav) root.classList.toggle('nav-on-dark', y < hero.offsetHeight - nav.offsetHeight);

		if (track && band && !reduceMotion) {
			const r = band.getBoundingClientRect();
			if (r.bottom > 0 && r.top < window.innerHeight) {
				const half = track.scrollWidth / 2;
				const shift = ((y * 0.35) % half) / half;
				track.style.transform = `translate3d(${(-shift * 50).toFixed(3)}%, 0, 0)`;
			}
		}
	});
}

/* ---------- the "View" badge that follows the pointer over a project ---------- */

function initCursorBadge() {
	const badge = document.querySelector<HTMLElement>('[data-cursor-badge]');
	if (!badge || !finePointer) return;
	let x = 0;
	let y = 0;
	let cx = 0;
	let cy = 0;
	let raf = 0;
	const loop = () => {
		const k = reduceMotion ? 1 : 0.2;
		cx += (x - cx) * k;
		cy += (y - cy) * k;
		badge.style.transform = `translate3d(${cx.toFixed(1)}px, ${cy.toFixed(1)}px, 0)`;
		raf = requestAnimationFrame(loop);
	};
	document.querySelectorAll<HTMLElement>('.work, .plan__media, .viz__frame').forEach((el) => {
		el.addEventListener('pointerenter', (e) => {
			x = cx = e.clientX;
			y = cy = e.clientY;
			badge.textContent = el.classList.contains('work') ? 'View' : el.classList.contains('viz__frame') ? '3D' : 'Plans';
			badge.classList.add('is-on');
			root.classList.add('badge-on');
			if (!raf) raf = requestAnimationFrame(loop);
		});
		el.addEventListener('pointermove', (e) => {
			x = e.clientX;
			y = e.clientY;
		});
		el.addEventListener('pointerleave', () => {
			badge.classList.remove('is-on');
			root.classList.remove('badge-on');
			setTimeout(() => {
				if (!badge.classList.contains('is-on')) {
					cancelAnimationFrame(raf);
					raf = 0;
				}
			}, 300);
		});
	});
}

/* ---------- magnetic buttons ---------- */

function initMagnetic() {
	if (reduceMotion || !finePointer) return;
	document.querySelectorAll<HTMLElement>('.btn--primary, .btn--secondary').forEach((el) => {
		let tx = 0;
		let ty = 0;
		let px = 0;
		let py = 0;
		let raf = 0;
		const loop = () => {
			px += (tx - px) * 0.18;
			py += (ty - py) * 0.18;
			el.style.translate = `${px.toFixed(2)}px ${py.toFixed(2)}px`;
			if (Math.abs(tx - px) + Math.abs(ty - py) > 0.05) raf = requestAnimationFrame(loop);
			else {
				raf = 0;
				if (!tx && !ty) el.style.translate = '';
			}
		};
		const kick = () => {
			if (!raf) raf = requestAnimationFrame(loop);
		};
		el.addEventListener('pointermove', (e) => {
			const r = el.getBoundingClientRect();
			tx = (e.clientX - (r.left + r.width / 2)) * 0.18;
			ty = (e.clientY - (r.top + r.height / 2)) * 0.3;
			kick();
		});
		el.addEventListener('pointerleave', () => {
			tx = 0;
			ty = 0;
			kick();
		});
	});
}

/* ---------- spotlight: cards light up where the pointer is ---------- */

function initSpotlight() {
	if (!finePointer) return;
	document.querySelectorAll<HTMLElement>('.plan, .step, .isheet, .voice').forEach((el) => {
		el.addEventListener('pointermove', (e) => {
			const r = el.getBoundingClientRect();
			el.style.setProperty('--mx', `${e.clientX - r.left}px`);
			el.style.setProperty('--my', `${e.clientY - r.top}px`);
		});
	});
}

export function initFx() {
	initSmooth();
	initReveals();
	initParallax();
	initScrollBits();
	initCursorBadge();
	initMagnetic();
	initSpotlight();
}
