def edit(p, a, b):
    s=open(p,encoding='utf-8').read()
    assert a in s, (p, a[:50]); s=s.replace(a,b,1); open(p,'w',encoding='utf-8').write(s)
L='src/layouts/Layout.astro'
edit(L,"import '@fontsource/ibm-plex-mono/500.css';\nimport '../styles/global.css';","import '@fontsource/ibm-plex-mono/500.css';\nimport '@fontsource/instrument-serif/400-italic.css';\nimport '../styles/global.css';\nimport '../styles/fx.css';")
edit(L,'<meta name="theme-color" content="#ecebe6" />','<meta name="theme-color" content="#151a12" />')
edit(L,"""	<body>
""","""	<body>
		<div class="progress" aria-hidden="true"><i data-progress></i></div>
		<div class="cursor-badge" aria-hidden="true" data-cursor-badge>View</div>
""")
edit(L,"""			deal: hero split (house render right) · palette: the client's own (logo black, drafting paper, the forest green of its package posts)""","""			deal: hero split (house render right) on a deep ink-green ground · palette: the client's own (logo black, drafting paper, the forest green of its package posts) plus a clay accent, asked for by the client brief ("add some colors")""")
edit('src/components/Process.astro','class="section ground-surface process"','class="section ground-deep process"')
edit('src/components/Hero.astro','<section class="hero"','<section class="hero ground-deep"')
edit('src/components/Packages.astro','<article class="pkg pkg--wide"','<article class="pkg pkg--wide pkg--green"')
print('ok')
