import re

# data: add the loft office
p = 'src/data/site.ts'
s = open(p, encoding='utf-8').read()
if 'workLoftOffice' not in s:
    s = s.replace("import workOfficeFitout from '../assets/images/work-office-fitout.jpg';",
                  "import workOfficeFitout from '../assets/images/work-office-fitout.jpg';\nimport workLoftOffice from '../assets/images/work-loft-office.jpg';")
    s = s.replace("""		package: 'Commercial fit-out or kiosk',
	},
];""", """		package: 'Commercial fit-out or kiosk',
	},
	{
		id: 'makati-loft',
		title: 'Loft studio office',
		kind: 'Commercial',
		place: 'Makati',
		year: '2025',
		scope: 'Fit-out design, lighting plan',
		image: workLoftOffice,
		alt: 'Open-plan loft office with full-height steel windows, a long timber table, pink chairs and black pendants',
		focus: '42% 50%',
		package: 'Commercial fit-out or kiosk',
	},
];""")
    open(p, 'w', encoding='utf-8').write(s)

W = """---
import { Image } from 'astro:assets';
import Icon from './Icon.astro';
import { works } from '../data/site';

// Two rows of three: wide, tall, tall, then tall, tall, wide.
const byId = Object.fromEntries(works.map((w) => [w.id, w]));
const rows = [
	[
		{ w: byId['alabang'], span: 's6' },
		{ w: byId['rockwell-unit'], span: 's3' },
		{ w: byId['qc-kitchen'], span: 's3' },
	],
	[
		{ w: byId['bgc-office'], span: 's3' },
		{ w: byId['makati-loft'], span: 's3' },
		{ w: byId['tagaytay'], span: 's6' },
	],
];
const img = {
	s6: { widths: [800, 1200, 1600], sizes: '(max-width: 1023px) 100vw, 60vw' },
	s3: { widths: [480, 800, 1200], sizes: '(max-width: 1023px) 50vw, 40vw' },
} as const;
---

<section class="section work-sec g2" id="work" aria-labelledby="work-title" style="--h: 2; --hm: 2">
	<div class="wrap">
		{
			rows.map((row, r) => (
				<div class={`g2__row work-row work-row--${r + 1}`}>
					{r === 0 && (
						<div class="sec-head sec-head--split">
							<div>
								<p class="label mono">
									<span>F</span> Finished work
								</p>
								<h2 class="h2" id="work-title">
									Finished houses, condos and offices across Metro Manila.
								</h2>
							</div>
							<div class="sec-head__lead work__lead">
								<p>
									Each project started as a brief and a lot or a unit. Every one left the studio as a full set of plans
									the contractor built from.
								</p>
								<a class="link-arrow" href="#quote">
									Start your project <Icon name="arrow-right" />
								</a>
							</div>
						</div>
					)}
					<div class="work-grid">
						{row.map(({ w, span }) => (
							<a class={`work work--${span}`} href="#quote" data-package={w.package}>
								<span class="work__head">
									<span class="work__name">
										<span class="work__title">{w.title}</span>
										<span class="work__scope">{w.scope}</span>
									</span>
									<span class="work__meta mono">
										{w.kind} · {w.place} · {w.year}
									</span>
								</span>
								<span class="frame frame--photo work__frame">
									<Image
										src={w.image}
										alt={w.alt}
										widths={[...img[span as 's6' | 's3'].widths]}
										sizes={img[span as 's6' | 's3'].sizes}
										data-source="stand-in"
										data-subject={`${w.kind.toLowerCase()} project`}
										style={w.focus ? `object-position: ${w.focus}` : undefined}
									/>
								</span>
							</a>
						))}
					</div>
				</div>
			))
		}
	</div>
</section>
"""
open('src/components/Work.astro', 'w', encoding='utf-8').write(W)

# Interiors: sheets left, photo right; sheet titles as p
p = 'src/components/Interiors.astro'
s = open(p, encoding='utf-8').read()
m = re.search(r'\t\t\t<div class="frame frame--photo interiors__frame">.*?\t\t\t</div>\n', s, re.S)
frame = m.group(0)
s = s.replace(frame, '')
s = s.replace('\t\t\t</ol>\n', '\t\t\t</ol>\n' + frame)
s = s.replace('<h3 class="isheet__title">{s.title}</h3>', '<p class="isheet__title">{s.title}</p>')
open(p, 'w', encoding='utf-8').write(s)

# Clients: text left, photo right
p = 'src/components/Testimonials.astro'
s = open(p, encoding='utf-8').read()
m = re.search(r'\t\t<div class="frame frame--photo voices__frame">.*?\t\t</div>\n', s, re.S)
frame = m.group(0)
s = s.replace(frame, '', 1)
s = s.replace('\t\t</div>\n\t</div>\n</section>', '\t\t</div>\n' + frame + '\t</div>\n</section>')
open(p, 'w', encoding='utf-8').write(s)

# CSS
p = 'src/styles/global.css'
s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b, 1)

rep(""".sec-head--split > .sec-head__lead {
	grid-column: 7 / span 6;
	align-self: end;
}""", """.sec-head--split > .sec-head__lead {
	grid-column: 7 / span 6;
}""")
rep(""".interiors__frame {
	grid-column: 1 / span 7;
	min-height: 300px;
}
.isheets {
	grid-column: 8 / span 5;""", """.interiors__frame {
	grid-column: 6 / span 7;
	grid-row: 1;
	min-height: 300px;
}
.isheets {
	grid-column: 1 / span 5;
	grid-row: 1;""")
rep(""".voices__frame {
	grid-column: 1 / span 5;
	min-height: 320px;
}
.voices__side {
	grid-column: 7 / span 6;""", """.voices__frame {
	grid-column: 8 / span 5;
	grid-row: 1;
	min-height: 320px;
}
.voices__side {
	grid-column: 1 / span 6;
	grid-row: 1;""")
rep("""	.interiors__frame {
		aspect-ratio: 16 / 10;
		min-height: 0;
		margin-bottom: 24px;
	}
	.voices__frame {
		aspect-ratio: 16 / 10;
		min-height: 0;
		margin-bottom: 40px;
	}""", """	.interiors__frame,
	.voices__frame,
	.isheets,
	.voices__side {
		grid-row: auto;
	}
	.interiors__frame {
		aspect-ratio: 16 / 10;
		min-height: 0;
		margin-top: 24px;
	}
	.voices__frame {
		aspect-ratio: 16 / 10;
		min-height: 0;
		margin-top: 40px;
	}""")
rep("""	.work-grid--3 .work--s3 {
		grid-column: span 6;
	}
	.work-grid--3 .work--s6 {
		grid-column: 1 / -1;
		order: -1;
	}""", """	.work-grid .work--s3 {
		grid-column: span 6;
	}""")
rep("""@media (max-width: 639px) {
	.work-grid--3 .work--s3 {
		grid-column: 1 / -1;
	}
	.work__head {
		flex-direction: column;
		gap: 6px;
	}
	.work__meta {
		text-align: left;
		padding-top: 0;
	}
	.work--s4 .work__frame,
	.work--s3 .work__frame {
		aspect-ratio: 4 / 3;
	}""", """@media (max-width: 639px) {
	.work-grid {
		row-gap: 32px;
		column-gap: 12px;
	}
	.work {
		gap: 10px;
	}
	.work__head {
		flex-direction: column;
		gap: 4px;
		padding-top: 10px;
	}
	.work__title {
		font-size: 1.0625rem;
	}
	.work__scope {
		display: none;
	}
	.work__meta {
		text-align: left;
		padding-top: 0;
		font-size: 0.625rem;
	}
	.work--s6 .work__frame {
		aspect-ratio: 3 / 2;
	}
	.work--s3 .work__frame {
		aspect-ratio: 1 / 1;
	}
	.work__lead > p {
		display: none;
	}""")
# isheet title was an h3: keep its look on a p
rep(""".isheet__title {
	font-size: 1.125rem;
}""", """.isheet__title {
	font-family: var(--font-display);
	font-size: 1.125rem;
	font-weight: 500;
	letter-spacing: -0.015em;
	line-height: 1.2;
}""")
open(p, 'w', encoding='utf-8').write(s)

open('.taste-skill/waivers.json', 'w', encoding='utf-8').write("""[
  {"check": "card-layout", "target": "section#work", "reason": "The sections share only the photo frame class: a row of project tiles, a list beside a photo, open package cards, a sheet list beside a photo, a full-width band, quotes beside a photo and a form under a strip are different compositions."}
]
""")
print('ok')
