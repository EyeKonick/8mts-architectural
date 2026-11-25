import re
p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()


def sub(a, b):
    global s
    if a not in s:
        raise SystemExit('MISSING: ' + a[:80])
    s = s.replace(a, b, 1)


sub("""	--p-muted: #5a5f54;""", """	--p-muted: #43463e;
	--p-quiet: #63685c;""")
sub("""	color-scheme: light;
}""", """	/* aliases the kit's moments read */
	--bg: var(--p-bg);
	--surface: var(--p-surface);
	--ink: var(--p-ink);
	--accent: var(--p-accent);
	--muted: var(--p-muted);
	--t-h2: var(--fs-h2);

	color-scheme: light;
}""")
sub(""".wrap {
	position: relative;
	z-index: 1;
	width: 100%;
	max-width: calc(var(--wrap) + 2 * var(--pad));
	margin-inline: auto;
	padding-inline: var(--pad);
}""", """.wrap {
	position: relative;
	z-index: 1;
	width: min(var(--wrap), 100% - 2 * var(--pad));
	margin-inline: auto;
}""")
sub(""".label {
	display: inline-flex;
	align-items: center;
	gap: 10px;
	color: var(--p-muted);""", """.label {
	display: inline-flex;
	align-items: center;
	gap: 10px;
	color: var(--p-quiet);""")
sub(""".h2 .muted,
.muted {
	color: var(--p-muted);
}""", """.h2 .muted,
.muted {
	color: var(--p-quiet);
}""")
sub("""	column-gap: var(--gap);
	align-items: end;
}
.sec-head--split > div {""", """	column-gap: var(--gap);
	align-items: start;
}
.sec-head--split > div {""")
sub(""".sec-head__lead {
	grid-column: 9 / span 4;""", """.sec-head__lead {
	grid-column: 9 / span 4;
	padding-top: 38px;""")
sub(""".sec-head {
	margin-bottom: 48px;
}""", """.sec-head {
	margin-bottom: 40px;
}""")
sub("""	padding: 4px;
	border-radius: 999px;
	background: var(--p-surface);
}""", """	padding: 4px;
	border-radius: 999px;
}""")
sub("""	background: var(--p-bg);
	box-shadow: 0 1px 2px rgb(20 22 17 / 0.1), inset 0 0 0 1px var(--line);
	opacity: 0;""", """	background: var(--p-surface);
	opacity: 0;""")
sub(""".nav__link {
	position: relative;
	z-index: 1;
	display: inline-flex;
	align-items: center;
	min-height: 40px;""", """.nav__link {
	position: relative;
	z-index: 1;
	display: inline-flex;
	align-items: center;
	min-height: 44px;""")
sub(""".nav__sub {
	font-size: 0.6875rem;
	color: var(--p-muted);""", """.nav__sub {
	font-size: 0.6875rem;
	color: var(--p-quiet);""")
sub("""	min-height: 52px;
	padding: 6px 12px 6px 0;""", """	min-height: 50px;
	padding: 5px 12px 5px 0;""")
sub(""".pkg--wide {
	grid-template-columns: repeat(12, minmax(0, 1fr));
	column-gap: var(--gap);
	height: calc(100% - 168px);
	min-height: 480px;
}""", """.packages .g2__row {
	display: flex;
	flex-direction: column;
}
.packages .g2__row > .pkg--wide {
	flex: 1;
	min-height: 0;
}
.packages .pkg.pkg--wide,
.packages .pkg.pkg--wide:hover {
	background: transparent;
	box-shadow: none;
}
.pkg--wide {
	grid-template-columns: repeat(12, minmax(0, 1fr));
	column-gap: var(--gap);
	min-height: 440px;
}""")
sub(""".pkg--wide .pkg__body {
	grid-column: 8 / span 5;
	padding: 28px 28px 20px 4px;
}""", """.pkg--wide .pkg__body {
	grid-column: 8 / span 5;
	padding: 0;
}""")
sub(""".pkg-pair .pkg {
	grid-template-rows: minmax(0, 1fr) auto;
	min-height: 0;
}""", """.pkg-pair .pkg {
	grid-template-rows: minmax(0, 1fr) auto;
	min-height: 0;
}
.pkg-pair .pkg__body {
	background: var(--p-surface);
	border-radius: 0 0 var(--r-lg) var(--r-lg);
}""")
sub(""".pkg__sheet {
	color: var(--p-muted);""", """.pkg__sheet {
	color: var(--p-quiet);""")
sub(""".statement__text {
	font-family: var(--font-display);
	font-size: clamp(1.75rem, 0.8rem + 3.3vw, 4rem);""", """.statement .mo-wh__text.statement__text {
	font-family: var(--font-display);
	font-size: clamp(1.75rem, 0.8rem + 3.3vw, 4rem);""")
s = re.sub(r"\.wh-live \.statement__text \.wd \{.*?\n\}\n\.wh-live \.statement__text \.wd\.is-lit \{.*?\n\}\n\.wh-live \.statement__text strong \.wd\.is-lit \{.*?\n\}\n", "", s, flags=re.S)
s, n = re.subn(r"/\* ---------- 3D views ---------- \*/.*?/\* ---------- FAQ ---------- \*/", """/* ---------- 3D views ---------- */

.viz {
	display: flex;
	flex-direction: column;
}
.viz__head {
	display: grid;
	grid-template-columns: repeat(12, minmax(0, 1fr));
	column-gap: var(--gap);
	margin-bottom: 32px;
}
.viz__head > div:first-child {
	grid-column: 1 / span 7;
}
.viz__side {
	grid-column: 9 / span 4;
	padding-top: 38px;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	gap: 12px;
}
.viz__lead {
	color: var(--p-muted);
	max-width: 40ch;
}
.viz__frame {
	flex: 1;
	min-height: 260px;
}
.viz__list {
	display: grid;
	grid-template-columns: repeat(3, minmax(0, 1fr));
	gap: var(--gap);
	margin-top: 20px;
}
.viz__list div {
	display: grid;
	gap: 4px;
	padding-top: 14px;
	border-top: 1px solid var(--line-strong);
}
.viz__list dt {
	color: var(--p-quiet);
}

/* ---------- FAQ ---------- */""", s, flags=re.S)
assert n == 1
sub(""".process__body {
	display: grid;
	grid-template-columns: repeat(12, minmax(0, 1fr));
	column-gap: var(--gap);
	height: calc(100% - 196px);
	min-height: 0;
}
.process__frame {
	grid-column: 1 / span 5;
	height: 100%;
	min-height: 300px;
	background: #f4f2ec;
}
.process__frame img {
	object-fit: contain;
	padding: 24px;
	mix-blend-mode: multiply;
}
.steps {
	grid-column: 7 / span 6;""", """.process__wrap {
	display: flex;
	flex-direction: column;
}
.process__body {
	flex: 1;
	min-height: 0;
	display: grid;
	grid-template-columns: repeat(12, minmax(0, 1fr));
	column-gap: var(--gap);
}
.process__frame {
	grid-column: 7 / span 6;
	height: 100%;
	min-height: 300px;
	background: #f4f2ec;
}
.process__frame img {
	position: absolute;
	inset: 0;
	width: 100%;
	height: 100%;
	object-fit: contain !important;
	padding: 24px;
	mix-blend-mode: multiply;
}
.steps {
	grid-column: 1 / span 6;""")
sub(""".step__n {
	display: block;
	color: var(--p-muted);""", """.step__n {
	display: block;
	color: var(--p-quiet);""")
s, n = re.subn(r"/\* picture-develops, film look.*?@keyframes develop \{.*?\n\}\n", "", s, flags=re.S)
assert n == 1
sub(""".quote__details dt {
	color: var(--p-muted);""", """.quote__frame {
	margin-top: 28px;
	height: 180px;
}
@media (min-width: 1024px) and (min-height: 860px) {
	.quote__frame {
		height: 220px;
	}
}
.quote__details dt {
	color: var(--p-quiet);""")
sub(""".quote__lead {
	color: var(--p-muted);
	max-width: 40ch;
	margin: 24px 0 36px;
}""", """.quote__lead {
	color: var(--p-muted);
	max-width: 40ch;
	margin: 20px 0 24px;
}""")
sub(""".quote__details div {
	padding: 14px 0;""", """.quote__details div {
	padding: 10px 0;""")
sub(""".tb__links a,
.tb > a {
	min-height: 28px;""", """.tb__links a,
.tb > a,
.tb__credits a {
	min-height: 32px;""")
sub("""	.services__body,
	.viz,
	.faq__grid,
	.process__body,
	.quote__grid {
		grid-template-columns: 1fr;
		row-gap: 32px;
		height: auto;
	}""", """	.services__body,
	.faq__grid,
	.process__body,
	.quote__grid,
	.viz__head,
	.hero__grid,
	.sec-head--split {
		grid-template-columns: minmax(0, 1fr);
		row-gap: 32px;
	}
	.viz__head > div,
	.viz__side {
		grid-column: 1 !important;
		padding-top: 0;
	}
	.viz__frame {
		flex: none;
		aspect-ratio: 16 / 10;
	}
	.viz__list {
		grid-template-columns: minmax(0, 1fr);
	}""")
sub("""	.svc-list,
	.services__visual,
	.viz__text,
	.viz__visual,
	.faq__head,""", """	.svc-list,
	.services__visual,
	.faq__head,""")
sub("""	.viz__frame,
	.process__frame {
		aspect-ratio: 16 / 10;
		height: auto;
	}
	.process__body {
		display: flex;
		flex-direction: column-reverse;
	}""", """	.process__frame {
		aspect-ratio: 16 / 10;
		height: auto;
	}
	.process__body {
		display: flex;
		flex-direction: column;
		gap: 32px;
	}
	.quote__frame {
		height: auto;
		aspect-ratio: 16 / 9;
	}""")
sub("""	.pkg-pair {
		grid-template-columns: 1fr;
	}""", """	.pkg-pair {
		grid-template-columns: minmax(0, 1fr);
	}""")
sub("""	.pkg__top {
		flex-direction: column;
		gap: 12px;
	}""", """	.pkg__top {
		flex-direction: column;
		gap: 12px;
	}
	.pkg__price,
	.pkg__top .pkg__price {
		font-size: 1.75rem;
	}
	.tb__links a,
	.tb > a,
	.tb__credits a {
		min-height: 44px;
	}
	.tb__links {
		gap: 0 20px;
	}""")
sub("""	.svc {
		grid-template-columns: 48px 1fr 20px;""", """	.svc {
		grid-template-columns: 48px minmax(0, 1fr) 20px;""")
sub("""	.form {
		grid-template-columns: 1fr;
	}""", """	.form {
		grid-template-columns: minmax(0, 1fr);
	}""")
s += """
/* ---------- Credits page ---------- */

.credits__lead {
	color: var(--p-muted);
	max-width: 60ch;
	margin: 20px 0 32px;
}
.credits__list {
	border-top: 1px solid var(--line);
	max-width: 900px;
}
.credits__list li {
	display: grid;
	grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
	gap: 16px;
	padding: 12px 0;
	border-bottom: 1px solid var(--line);
}
.credits__list a {
	min-height: 32px;
	display: inline-flex;
	align-items: center;
}
@media (max-width: 639px) {
	.credits__list li {
		grid-template-columns: minmax(0, 1fr);
		gap: 4px;
	}
}
"""
open(p, 'w', encoding='utf-8').write(s)
print('ok')
