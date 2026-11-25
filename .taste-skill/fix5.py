p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()


def sub(a, b, count=1):
    global s
    if a not in s:
        raise SystemExit('MISSING css: ' + a[:80])
    s = s.replace(a, b, count)


# fixed screen heights only on screens tall enough to hold the content; shorter screens grow
sub("""@media (min-width: 1024px) and (min-height: 640px) {
	main > section,
	footer.closing {
		height: calc(var(--h, 1) * 100svh);
	}
}
@media (max-width: 1023px), (max-height: 639px) {""", """@media (min-width: 1024px) and (min-height: 820px) {
	main > section,
	footer.closing {
		height: calc(var(--h, 1) * 100svh);
	}
}
@media (min-width: 1024px) and (max-height: 819px) {
	#services,
	#process,
	#quote {
		--h: 2;
	}
}
@media (max-width: 1023px), (max-height: 819px) {""")
sub("""@media (min-width: 1024px) and (min-height: 640px) {
	main > section > .wrap {
		height: 100%;
	}
}""", """@media (min-width: 1024px) and (min-height: 820px) {
	main > section > .wrap {
		height: 100%;
	}
}""")
sub("""@media (min-width: 1024px) and (min-height: 640px) {
	.g2 .g2__row {""", """@media (min-width: 1024px) and (min-height: 820px) {
	.g2 .g2__row {""")
sub("""@media (max-width: 1023px), (max-height: 639px) {
	.g2 .g2__row + .g2__row {""", """@media (max-width: 1023px), (max-height: 819px) {
	.g2 .g2__row + .g2__row {""")
# price under the title in the pair cards, on the column line
sub(""".pkg__top {
	display: flex;
	justify-content: space-between;
	align-items: flex-start;
	gap: 24px;
	width: 100%;
	margin-bottom: 20px;
}
.pkg__top .pkg__price {
	margin: 0;
	font-size: 2.25rem;
}""", """.pkg__top {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	gap: 12px;
	width: 100%;
	margin-bottom: 18px;
}
.pkg__top .pkg__price {
	margin: 0;
	font-size: 2.25rem;
}""")
# tablet: the two package cards side by side; taller pictures where a section is two screens
sub("""	.pkg-pair {
		grid-template-columns: minmax(0, 1fr);
	}""", """	.pkg-pair {
		grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
	}
	.pkg-pair .pkg__media {
		aspect-ratio: 4 / 3 !important;
	}
	.pkg-pair .pkg__list--cols {
		grid-template-columns: minmax(0, 1fr);
	}""")
sub("""@media (min-width: 640px) and (max-width: 1023px) {
	#packages,
	#process,
	#services {
		--h: 2;
	}
}""", """@media (min-width: 640px) and (max-width: 1023px) {
	#packages,
	#process,
	#services {
		--h: 2;
	}
	.services__frame {
		aspect-ratio: 4 / 3 !important;
	}
	.process__frame {
		aspect-ratio: 1 / 1 !important;
	}
}""")
sub("""	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		padding-top: 0;
	}""", """	.pkg-pair {
		grid-template-columns: minmax(0, 1fr);
	}
	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		padding-top: 0;
	}""")
open(p, 'w', encoding='utf-8').write(s)

k = 'src/components/Packages.astro'
t = open(k, encoding='utf-8').read()
t = t.replace('id="packages" aria-labelledby="packages-title" style="--h: 2"', 'id="packages" aria-labelledby="packages-title" style="--h: 2; --hm: 2"')
open(k, 'w', encoding='utf-8').write(t)
print('ok')
