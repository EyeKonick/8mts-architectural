def edit(p,a,b):
    s=open(p,encoding='utf-8').read(); assert a in s,(p,a[:60]); s=s.replace(a,b,1); open(p,'w',encoding='utf-8').write(s)
F='src/styles/fx.css'
# clay deep enough for white text at 4.5:1
edit(F,'--clay: #c4562a;','--clay: #b94d23;')
edit(F,'box-shadow: 0 14px 30px -18px rgb(196 86 42 / 0.75);','box-shadow: 0 14px 30px -18px rgb(185 77 35 / 0.75);')
# hero glass card: denser so its text reads over the photo
edit(F,'''	background: rgb(21 26 18 / 0.62);
	color: var(--paper);''','''	background: rgb(21 26 18 / 0.9);
	color: var(--paper);''')
# green package card: ink inside turns paper; both columns padded alike
edit(F,'''	--line: rgb(236 235 230 / 0.14);
	--line-strong: rgb(236 235 230 / 0.26);
}
.pkg--green .pkg__body {
	padding: 32px;
}''','''	--line: rgb(236 235 230 / 0.14);
	--line-strong: rgb(236 235 230 / 0.26);
	--p-ink: var(--paper);
	padding: 12px;
	align-items: stretch;
}
.pkg--green .pkg__body {
	padding: 20px 20px 20px 20px;
}
.pkg--green .pkg__addons .mono {
	color: var(--clay-light);
}''')
edit(F,'''	.pkg--green .pkg__body {
		padding: 24px;
	}''','''	.pkg--green .pkg__body {
		padding: 16px 12px 12px;
	}
	/* no parallax zoom on phones and tablets: the file is drawn at its own size */
	.fx-par img {
		scale: 1;
		translate: none;
	}''')
edit(F,'''@media (max-width: 639px) {
	.voice {''','''@media (max-width: 639px) {
	.h2 em {
		font-size: 1em;
	}
	.viz__frame {
		min-height: 200px;
	}
	.voice {''')
# closing button: same height as every other primary
edit('src/components/Closing.astro','<a class="btn btn--primary btn--lg"','<a class="btn btn--primary"')
print('ok')
