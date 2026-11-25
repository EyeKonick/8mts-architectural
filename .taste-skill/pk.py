import re

G = 'src/styles/global.css'
s = open(G, encoding='utf-8').read()

# 1. the old package block, up to the statement header
a = s.index('/* ---------- Packages ---------- */')
b = s.index('/* ---------- Statement (word-highlight) ---------- */')
s = s[:a] + s[b:]

# 2. old responsive package rules
def drop(block):
    global s
    assert block in s, block[:60]
    s = s.replace(block, '', 1)

drop("""	.pkg--wide {
		grid-template-columns: 1fr;
		height: auto;
	}
	.pkg--wide .pkg__media,
	.pkg--wide .pkg__body {
		grid-column: 1;
		grid-row: auto;
	}
	.pkg--wide .pkg__media,
	.pkg-pair .pkg__media {
		aspect-ratio: 16 / 9;
		height: auto;
		order: 2;
	}
	.pkg--wide .pkg__body {
		padding: 0 0 28px;
	}
	.pkg-pair {
		grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
	}
	.pkg-pair .pkg__media {
		aspect-ratio: 4 / 3 !important;
	}
	.pkg-pair .pkg__list--cols {
		grid-template-columns: minmax(0, 1fr);
	}
	.pkg-pair .pkg {
		grid-template-rows: auto;
	}
""")
drop("""	.pkg__sheet {
		display: none;
	}
	.pkg--wide .pkg__media {
		aspect-ratio: 2 / 1 !important;
	}
	.pkg__list li::before {
		left: -12px;
		width: 7px;
	}
""")
drop("""	.pkg__list--cols {
		grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
	}
	.pkg__body {
		padding: 0;
	}
	.pkg--wide .pkg__body {
		padding: 0 0 20px;
	}
	.pkg-pair {
		grid-template-columns: minmax(0, 1fr);
	}
	.pkg-pair .pkg__media {
		display: none;
	}
	.pkg-pair .pkg__body {
		padding-top: 0;
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
	}
	.pkg__top {
		flex-direction: column;
		gap: 12px;
	}
	.pkg__price,
	.pkg__top .pkg__price {
		font-size: 1.75rem;
	}
""")
left = re.findall(r'^.*pkg.*$', s, re.M)
print('global pkg left:', left)

# 3. services: the list and the photograph fill the section
s = s.replace(""".services__body {
	display: grid;""", """.services > .wrap {
	display: flex;
	flex-direction: column;
}
.services__body {
	flex: 1;
	min-height: 0;
	display: grid;""", 1)
open(G, 'w', encoding='utf-8').write(s)

# 4. fx.css: drop the old .pkg colour rules, add the plans
F = 'src/styles/fx.css'
f = open(F, encoding='utf-8').read()
a = f.index('/* ---------- packages: the lead on green')
b = f.index('/* ---------- interiors: sheets slide')
f = f[:a] + PLANS + '\n' + f[b:] if False else f[:a] + open('.taste-skill/plans.css', encoding='utf-8').read() + '\n' + f[b:]
f = f.replace("""	.pkg--green .pkg__body {
		padding: 16px 12px 12px;
	}
""", "")
open(F, 'w', encoding='utf-8').write(f)
print('fx pkg left:', re.findall(r'^.*pkg.*$', f, re.M))
