p='src/components/Testimonials.astro'; s=open(p,encoding='utf-8').read()
import re
s=re.sub(r'\t+<span class="voice__mark mono" aria-hidden="true">\s*\{initials\(t\.name\)\}\s*</span>\n','',s)
s=re.sub(r"const initials = .*?join\(''\);\n",'',s,flags=re.S)
s=s.replace('''								<span>
									<span class="voice__name">{t.name}</span>
									<span class="voice__role">{t.role}</span>
								</span>''','''								<span class="voice__name">{t.name}</span>
								<span class="voice__role">{t.role}</span>''')
open(p,'w',encoding='utf-8').write(s)

p='src/components/Work.astro'; s=open(p,encoding='utf-8').read()
s=s.replace("""	s3: { widths: [480, 800, 1200], sizes: '(max-width: 1023px) 50vw, 40vw' },""","""	s3: { widths: [480, 800, 1200], sizes: '(max-width: 1023px) 50vw, 40vw' },
	// a landscape photograph cropped into a tall slot needs a wider file
	s3wide: { widths: [600, 900, 1200], sizes: '(max-width: 1023px) 50vw, 64vw' },""")
s=s.replace("""										widths={[...img[span as 's6' | 's3'].widths]}
										sizes={img[span as 's6' | 's3'].sizes}""","""										widths={[...img[span === 's3' && w.image.width > w.image.height ? 's3wide' : (span as 's6' | 's3')].widths]}
										sizes={img[span === 's3' && w.image.width > w.image.height ? 's3wide' : (span as 's6' | 's3')].sizes}""")
open(p,'w',encoding='utf-8').write(s)

p='src/styles/global.css'; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b,1)
rep(""".voices__frame {
	grid-column: 8 / span 5;""",""".voices__frame {
	grid-column: 7 / span 6;""")
rep(""".voice__person {
	display: flex;
	align-items: center;
	gap: 12px;
	font-size: var(--fs-small);
}""",""".voice__person {
	display: flex;
	flex-wrap: wrap;
	align-items: baseline;
	gap: 4px 10px;
	font-size: var(--fs-small);
}""")
rep(""".voice__name {
	display: block;
	font-weight: 500;
}
.voice__role {
	display: block;
	color: var(--p-muted);
}""",""".voice__name {
	font-weight: 500;
}
.voice__name::after {
	content: '·';
	margin-left: 10px;
	color: var(--p-quiet);
}
.voice__role {
	color: var(--p-muted);
}""")
rep("""	.work-grid {
		row-gap: 32px;
		column-gap: 12px;
	}""","""	.work-grid .work--s3 {
		grid-column: 1 / -1;
	}
	.work-grid {
		row-gap: 28px;
	}""")
rep("""	.work--s6 .work__frame {
		aspect-ratio: 3 / 2;
	}
	.work--s3 .work__frame {
		aspect-ratio: 1 / 1;
	}""","""	.work--s6 .work__frame,
	.work--s3 .work__frame {
		aspect-ratio: 16 / 10;
	}""")
open(p,'w',encoding='utf-8').write(s)
print('ok')
