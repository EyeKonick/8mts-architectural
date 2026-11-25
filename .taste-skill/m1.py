import re
C='src/components/'
def edit(f, a, b):
    p=C+f; s=open(p,encoding='utf-8').read()
    assert a in s, (f, a[:50]); s=s.replace(a,b,1); open(p,'w',encoding='utf-8').write(s)

edit('Closing.astro','Plans first, then the build. <span class="muted">Start with a quote.</span>','Plans first, then the build. <em>Start with a quote.</em>')
edit('Faq.astro','Questions about plans and permits.','Questions about <em>plans and permits.</em>')
edit('Interiors.astro','Interiors planned to the last fixture.','Interiors planned <em>to the last fixture.</em>')
edit('Packages.astro','Packages and prices. <span class="muted">Three ways to start.</span>','Packages and prices. <em>Three ways to start.</em>')
edit('Process.astro','Four steps from first message to signed plans.','Four steps from first message <em>to signed plans.</em>')
edit('Quote.astro','Request a quote for your plans.','Request a quote <em>for your plans.</em>')
edit('Services.astro','Nine design and drafting services. <span class="muted">One studio draws them all.</span>','Nine design and drafting services. <em>One studio draws them all.</em>')
edit('Testimonials.astro','What owners say once the plans are filed.','What owners say <em>once the plans are filed.</em>')
edit('Visualization.astro','3D views of your house before it is built.','3D views of your house <em>before it is built.</em>')
edit('Work.astro','Finished houses, condos and offices across Metro Manila.','Finished houses, condos and offices <em>across Metro Manila.</em>')
# hero: last two words in the serif
edit('Hero.astro','''							<span class="w">
								<span style={`--w:${i}`}>{w}</span>
							</span>{' '}''','''							<span class:list={['w', { 'w--serif': i >= words.length - 2 }]}>
								<span style={`--w:${i}`}>{w}</span>
							</span>{' '}''')
print('ok')
