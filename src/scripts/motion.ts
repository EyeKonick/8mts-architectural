/** Shared motion settings for the few effects that need script. CSS owns the rest. */
export const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* One passive scroll listener for the whole page; work is batched into a single frame. */
type ScrollCb = (y: number) => void;
const subscribers = new Set<ScrollCb>();
let ticking = false;
const flush = () => {
	ticking = false;
	const y = window.scrollY;
	subscribers.forEach((cb) => cb(y));
};
const schedule = () => {
	if (ticking) return;
	ticking = true;
	requestAnimationFrame(flush);
};
window.addEventListener('scroll', schedule, { passive: true });
window.addEventListener('resize', schedule, { passive: true });

/** Subscribe to the shared scroll loop. Runs once immediately. */
export function onScroll(cb: ScrollCb) {
	subscribers.add(cb);
	cb(window.scrollY);
	return () => subscribers.delete(cb);
}

const canVibrate = 'vibrate' in navigator && window.matchMedia('(pointer: coarse)').matches;
/** A short buzz for the outcome of the visitor's own submit, on phones that support it. */
export function haptic(kind: 'success' | 'error') {
	if (!canVibrate) return;
	try {
		navigator.vibrate(kind === 'success' ? [12] : [24, 60, 24]);
	} catch {
		/* blocked by the browser: ignore */
	}
}
