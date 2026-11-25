import re


def edit(p, pairs):
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            raise SystemExit('MISSING in ' + p + ': ' + a[:80])
        s = s.replace(a, b, 1)
    open(p, 'w', encoding='utf-8').write(s)


edit('src/data/site.ts', [
    ("title: 'Project brief by message',", "title: 'Project brief and location',"),
    ("title: 'Site inspection',", "title: 'Site visit and measurements',"),
])

# hero: kit structure, .wrap > .hero-text
edit('src/components/Hero.astro', [
    ('<div class="wrap hero__grid">', '<div class="wrap hero__wrap">\n\t\t<div class="hero-text hero__grid">'),
    ("""		</div>
	</div>
</section>""", """		</div>
		</div>
	</div>
</section>"""),
])

# faq: two answers open
edit('src/components/Faq.astro', [("open={i === 0}", "open={i < 2}")])

# quote: photo moves to the right column, above the form
s = open('src/components/Quote.astro', encoding='utf-8').read()
m = re.search(r"\n\t\t\t<div class=\"frame frame--photo quote__frame\">.*?\n\t\t\t</div>\n", s, flags=re.S)
photo = m.group(0)
s = s.replace(photo, '\n', 1)
s = s.replace('\t\t<form class="form"', '\t\t<div class="quote__side">' + photo.replace('\n\t\t\t', '\n\t\t\t\t').rstrip('\n') + '\n\t\t<form class="form"', 1)
s = s.replace('\t\t</form>\n', '\t\t</form>\n\t\t</div>\n', 1)
s = s.replace('class="section ground-surface quote" id="quote"', 'class="section ground-surface quote" id="quote" style="--hm: 2"', 1)
open('src/components/Quote.astro', 'w', encoding='utf-8').write(s)

edit('src/components/Process.astro', [
    ('class="section ground-surface process" id="process"', 'class="section ground-surface process" id="process" style="--hm: 2"'),
])

# packages: wide card text left, photo right
s = open('src/components/Packages.astro', encoding='utf-8').read()
m = re.search(r"\n\t\t\t\t<a class=\"pkg__media frame frame--photo crop\" href=\"#quote\" data-package=\{lead.short\}.*?\n\t\t\t\t</a>", s, flags=re.S)
media = m.group(0)
s = s.replace(media, '', 1)
s = s.replace("""					</a>
				</div>
			</article>
		</div>

		<div class="g2__row pkg-pair">""", """					</a>
				</div>""" + media + """
			</article>
		</div>

		<div class="g2__row pkg-pair">""", 1)
open('src/components/Packages.astro', 'w', encoding='utf-8').write(s)

# css
p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()


def sub(a, b):
    global s
    if a not in s:
        raise SystemExit('MISSING css: ' + a[:80])
    s = s.replace(a, b, 1)


sub("--p-quiet: #63685c;", "--p-quiet: #5a5f54;")
sub(""".nav__sub {
	font-size: 0.6875rem;""", """.nav__sub {
	white-space: nowrap;
	font-size: 0.6875rem;""")
sub("""	max-width: 12ch;
	line-height: 1.25;""", """	line-height: 1.25;""")
sub(""".skip-link:focus-visible {
	transform: none;
}""", """.skip-link:not(:focus-visible) {
	clip-path: inset(50%);
	width: 1px;
	height: 1px;
	padding: 0;
	min-height: 0;
	overflow: hidden;
	white-space: nowrap;
}
.skip-link:focus-visible {
	transform: none;
}""")
sub(""".sec-head__lead {
	grid-column: 9 / span 4;
	padding-top: 38px;""", """.sec-head__lead {
	grid-column: 9 / span 4;""")
sub(""".viz__side {
	grid-column: 9 / span 4;
	padding-top: 38px;""", """.viz__side {
	grid-column: 9 / span 4;""")
# hero wrap chain + dims inside the column
sub(""".hero__grid {
	display: grid;""", """.hero__wrap {
	height: 100%;
}
.hero__grid {
	display: grid;""")
sub(""".hero__frame {
	height: 100%;
}""", """.hero__frame {
	height: calc(100% - 16px);
	margin-top: 16px;
}""")
sub("""	top: -14px;
	height: 9px;
}""", """	top: 0;
	height: 9px;
}""")
sub("""	top: 0;
	bottom: 0;
	right: -14px;
	width: 9px;
}""", """	top: 16px;
	bottom: 0;
	right: -14px;
	width: 9px;
}""")
# services rows: one line height, arrow always shown
sub(""".svc__code {
	color: var(--p-muted);
	padding-left: 4px;""", """.svc > span {
	line-height: 20px;
}
.svc__code {
	color: var(--p-quiet);
	padding-left: 4px;""")
sub("""	color: var(--p-muted);
	opacity: 0;
	transform: translate(-6px, 6px);""", """	color: var(--p-quiet);
	opacity: 0.45;
	transform: none;""")
sub("""	opacity: 1;
	transform: none;
	color: var(--p-ink);
}""", """	opacity: 1;
	transform: translate(2px, -2px);
	color: var(--p-ink);
}""")
# packages wide: text left, photo right
sub(""".pkg--wide .pkg__media {
	grid-column: 1 / span 7;
	height: 100%;
}
.pkg--wide .pkg__body {
	grid-column: 8 / span 5;
	padding: 0;
}""", """.pkg--wide .pkg__body {
	grid-column: 1 / span 5;
	grid-row: 1;
	padding: 0;
}
.pkg--wide .pkg__media {
	grid-column: 6 / span 7;
	grid-row: 1;
	height: 100%;
}""")
# quote side column
sub(""".form {
	grid-column: 7 / span 6;""", """.quote__side {
	grid-column: 7 / span 6;
	display: flex;
	flex-direction: column;
	gap: 24px;
}
.form {""")
sub(""".quote__frame {
	margin-top: 28px;
	height: 180px;
}
@media (min-width: 1024px) and (min-height: 860px) {
	.quote__frame {
		height: 220px;
	}
}""", """.quote__frame {
	height: 150px;
	flex: none;
}
@media (min-width: 1024px) and (min-height: 860px) {
	.quote__frame {
		height: 180px;
	}
	.quote__lead {
		margin-bottom: 36px !important;
	}
}""")
sub("""	.quote__intro,
	.form {
		grid-column: 1;
	}""", """	.quote__intro,
	.quote__side {
		grid-column: 1;
	}""")
sub("""	.services__frame {
		aspect-ratio: 16 / 9;
		height: auto;
	}""", """	.services__frame {
		aspect-ratio: 16 / 9;
		height: auto;
		min-height: 0;
	}""")
sub("""	.viz__frame {
		flex: none;
		aspect-ratio: 16 / 10;
	}""", """	.viz__frame {
		flex: none;
		aspect-ratio: 16 / 10;
		min-height: 0;
	}""")
sub("""	.process__frame {
		aspect-ratio: 16 / 10;
		height: auto;
	}""", """	.process__frame {
		aspect-ratio: 16 / 10;
		height: auto;
		min-height: 0;
	}""")
sub("""	.pkg--wide .pkg__media,
	.pkg--wide .pkg__body {
		grid-column: 1;
	}""", """	.pkg--wide .pkg__media,
	.pkg--wide .pkg__body {
		grid-column: 1;
		grid-row: auto;
	}""")
sub("""	.pkg--wide .pkg__body {
		padding: 28px;
	}""", """	.pkg--wide .pkg__body {
		padding: 0 0 28px;
	}""")
# phone: packages compact so the section stays within two screens
sub("""	.pkg__body,
	.pkg--wide .pkg__body {
		padding: 22px 20px 12px;
	}""", """	.pkg__body {
		padding: 20px 20px 8px;
	}
	.pkg--wide .pkg__body {
		padding: 0 0 20px;
	}
	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		border-radius: var(--r-lg);
	}
	.pkg__list {
		font-size: 0.875rem;
		gap: 4px 16px;
		margin-bottom: 12px;
	}
	.pkg__price {
		margin: 10px 0 14px;
	}
	.pkg__title,
	.pkg--wide .pkg__title {
		font-size: 1.25rem;
	}
	.packages .sec-head {
		margin-bottom: 24px;
	}""")
sub("""	.pkg__list--cols {
		grid-template-columns: 1fr;
	}""", """	.pkg__list--cols {
		grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
	}""")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
