p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()


def sub(a, b):
    global s
    if a not in s:
        raise SystemExit('MISSING css: ' + a[:80])
    s = s.replace(a, b, 1)


# every split shares the hero's line: left 1-6, right 7-12
sub(""".sec-head--split > div {
	grid-column: 1 / span 7;
}
.sec-head__lead {
	grid-column: 8 / span 5;
	color: var(--p-muted);
	max-width: 42ch;
}""", """.sec-head--split > div {
	grid-column: 1 / span 6;
}
.sec-head__lead {
	grid-column: 7 / span 6;
	color: var(--p-muted);
}""")
sub(""".viz__head > div:first-child {
	grid-column: 1 / span 7;
}
.viz__side {
	grid-column: 8 / span 5;""", """.viz__head > div:first-child {
	grid-column: 1 / span 6;
}
.viz__side {
	grid-column: 7 / span 6;""")
sub(""".pkg--wide .pkg__media {
	grid-column: 8 / span 5;""", """.pkg--wide .pkg__media {
	grid-column: 7 / span 6;""")
sub(""".svc-list {
	grid-column: 1 / span 7;""", """.svc-list {
	grid-column: 1 / span 6;""")
sub(""".services__visual {
	grid-column: 8 / span 5;""", """.services__visual {
	grid-column: 7 / span 6;""")
sub(""".faq__head {
	grid-column: 1 / span 4;""", """.faq__head {
	grid-column: 1 / span 6;""")
sub(""".quote__intro {
	grid-column: 1 / span 5;
}""", """.quote__intro {
	grid-column: 1 / span 6;
}""")
# services rows in a narrower column: the line drops under the title
sub(""".svc {
	position: relative;
	display: grid;
	grid-template-columns: 64px minmax(0, 1.1fr) minmax(0, 1fr) 20px;""", """.svc {
	position: relative;
	display: grid;
	grid-template-columns: 56px minmax(0, 1.25fr) minmax(0, 1fr) 20px;""")
# the note: plain text on the line
sub(""".pkg__note {
	display: flex;
	align-items: center;
	gap: 10px;
	margin-top: 14px;""", """.pkg__note {
	margin-top: 14px;""")
sub(""".pkg__note::before {
	content: '';
	width: 22px;
	height: 22px;
	flex: none;
	border-radius: 50%;
	border: 1.5px solid var(--p-accent);
	background: radial-gradient(circle, var(--p-accent) 0 3px, transparent 3.5px);
}
""", "")
# statement a little smaller so it ends higher in its screen
sub("font-size: clamp(1.75rem, 0.8rem + 3.3vw, 4rem);", "font-size: clamp(1.75rem, 0.9rem + 2.9vw, 3.5rem);")
# phone
sub("""	.process__frame {
		aspect-ratio: 1 / 1 !important;
	}
	.quote__frame {
		aspect-ratio: 4 / 3 !important;
	}""", """	.process__frame {
		aspect-ratio: 3 / 4 !important;
	}
	.quote__frame {
		aspect-ratio: 1 / 1 !important;
	}
	.quote__details dd a {
		min-height: 44px;
		display: inline-flex;
		align-items: center;
	}""")
sub("""	.pkg__list li::before {
		left: -12px;
		width: 7px;
	}
	.pkg__list {
		padding-left: 12px;
	}""", """	.pkg__list li::before {
		left: -12px;
		width: 7px;
	}""")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
