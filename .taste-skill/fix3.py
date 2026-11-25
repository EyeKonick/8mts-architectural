p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()


def sub(a, b):
    global s
    if a not in s:
        raise SystemExit('MISSING css: ' + a[:80])
    s = s.replace(a, b, 1)


# split lines: right columns start on column 8 (x 841 at 1440)
sub(""".sec-head__lead {
	grid-column: 9 / span 4;""", """.sec-head__lead {
	grid-column: 8 / span 5;""")
sub(""".viz__side {
	grid-column: 9 / span 4;""", """.viz__side {
	grid-column: 8 / span 5;""")
sub(""".pkg--wide .pkg__body {
	grid-column: 1 / span 5;""", """.pkg--wide .pkg__body {
	grid-column: 1 / span 6;""")
sub(""".pkg--wide .pkg__media {
	grid-column: 6 / span 7;""", """.pkg--wide .pkg__media {
	grid-column: 8 / span 5;""")
sub(""".faq__list {
	grid-column: 6 / span 7;""", """.faq__list {
	grid-column: 7 / span 6;""")
# open package cards: no box, the photograph on top, words on the column lines
sub(""".packages .pkg {
	background: var(--p-surface);
	box-shadow: none;
}
.packages .pkg:hover {
	box-shadow: 0 18px 40px -28px rgb(20 22 17 / 0.5);
}""", """.packages .pkg,
.packages .pkg:hover {
	background: transparent;
	box-shadow: none;
}""")
sub(""".pkg-pair .pkg__body {
	background: var(--p-surface);
	border-radius: 0 0 var(--r-lg) var(--r-lg);
}""", """.pkg-pair .pkg__body {
	padding: 24px 0 0;
}""")
# hanging dashes so list text sits on the line
sub(""".pkg__list li {
	position: relative;
	padding-left: 18px;
}
.pkg__list li::before {
	content: '';
	position: absolute;
	left: 0;""", """.pkg__list li {
	position: relative;
}
.pkg__list li::before {
	content: '';
	position: absolute;
	left: -16px;""")
# services rows: one height for every item
sub(""".svc__go {
	display: grid;""", """.svc__go {
	height: 20px;
	display: grid;""")
# nav never wraps
sub(""".nav__link {
	position: relative;
	z-index: 1;
	display: inline-flex;""", """.nav__link {
	white-space: nowrap;
	position: relative;
	z-index: 1;
	display: inline-flex;""")
s += """
@media (min-width: 1024px) and (max-width: 1199px) {
	.nav__link {
		padding: 0 11px;
	}
	.nav__sub {
		display: none;
	}
}
@media (max-width: 419px) {
	.nav__sub {
		display: none;
	}
}
"""
# remove the vertical dimension line (it sat outside the container)
sub("""@media (max-width: 1360px) {
	.dim--y {
		display: none;
	}
}""", """.dim--y {
	display: none;
}""")
# phone: services fit one screen with a bigger picture; packages compact
sub("""	.svc__line {
		grid-column: 2;
		grid-row: 2;
	}""", """	.svc__line {
		display: none;
	}
	.services__frame {
		aspect-ratio: 4 / 3 !important;
	}
	.process__frame {
		aspect-ratio: 1 / 1 !important;
	}
	.quote__frame {
		aspect-ratio: 4 / 3 !important;
	}
	.pkg__sheet {
		display: none;
	}
	.pkg--wide .pkg__media {
		aspect-ratio: 2 / 1 !important;
	}
	.pkg__list li::before {
		left: -12px;
		width: 7px;
	}
	.pkg__list {
		padding-left: 12px;
	}""")
sub("""	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		border-radius: var(--r-lg);
	}""", """	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		padding-top: 0;
	}""")
sub("""	.pkg__body {
		padding: 20px 20px 8px;
	}""", """	.pkg__body {
		padding: 0;
	}""")
open(p, 'w', encoding='utf-8').write(s)

f = 'src/components/Faq.astro'
t = open(f, encoding='utf-8').read().replace('open={i < 2}', 'open={i < 3}')
open(f, 'w', encoding='utf-8').write(t)
h = 'src/components/Hero.astro'
t = open(h, encoding='utf-8').read().replace('\t\t\t<span class="dim dim--y" aria-hidden="true"><i></i></span>\n', '')
open(h, 'w', encoding='utf-8').write(t)
print('ok')
