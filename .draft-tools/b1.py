from lib import page

# 11 after Marcel Stuliglowa
page(11, 'statement-dark', 'family=Hanken+Grotesk:wght@400..700', '#17181A', '''
:root { color-scheme: dark; --line: #2C2E31; --focus: #F5C542; --f-bg: #202225; --f-text: #F1F1EF; --f-ph: #9A9B9D; --f-border: 1px solid #2C2E31; --b-bg: #F5C542; --b-text: #17181A; --note: #9A9B9D; --err: #FF9B8F; }
body { background: #17181A; color: #F1F1EF; font: 16px/1.6 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #F5C542; color: #17181A; }
.top a { color: #F5C542; }
h1 { max-width: 12em; margin-top: clamp(40px, 12vh, 120px); font-size: clamp(2.2rem, 1.2rem + 3.6vw, 3.8rem); font-weight: 700; line-height: 1.02; letter-spacing: -0.035em; }
.sub { max-width: 30em; margin: 22px 0 28px; color: #B4B5B6; }
.signup { max-width: 440px; }
.sec { display: grid; gap: 14px 40px; margin-top: clamp(64px, 12vh, 120px); padding-top: 18px; border-top: 1px solid var(--line); }
.sec h2 { font-size: 0.85rem; font-weight: 500; color: #9A9B9D; }
.who { display: flex; gap: 18px; align-items: center; }
.face { flex: none; width: 96px; height: 96px; border-radius: 8px; background: #2C2E31; }
@media (min-width: 800px) { .sec { grid-template-columns: 220px minmax(0, 1fr); } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<h1 data-in>{{H}}</h1>
		<p class="sub" data-in style="--i:1">{{INTRO}}</p>
		<div data-in style="--i:2">{{FORM}}</div>
		<section class="sec"><h2>The instructor</h2><div class="who"><div class="face">{{IMG}}</div><p>Mostafa Saher, technical instructor. I teach AI and cloud for a living.</p></div></section>
		<section class="sec"><h2>The writing</h2>{{TOPICS_UL}}</section>
		<section class="sec"><h2>Elsewhere</h2>{{LINKS_ROWS}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 12 after Rafael Cespedes
page(12, 'dense-index', 'family=Schibsted+Grotesk:wght@400..600', '#131313', '''
:root { color-scheme: dark; --line: #2A2A2A; --focus: #fff; --f-bg: #1D1D1D; --f-text: #EDEDED; --f-ph: #8E8E8E; --b-bg: #EDEDED; --b-text: #131313; --note: #8E8E8E; --err: #FF9B8F; --f-radius: 8px; --b-radius: 4px; --w: 620px; }
body { background: #131313; color: #EDEDED; font: 16px/1.45 "Schibsted Grotesk", system-ui, sans-serif; }
::selection { background: #EDEDED; color: #131313; }
.bar { display: flex; align-items: center; gap: 10px; padding-block: 20px; }
.face { width: 30px; height: 30px; border-radius: 50%; background: #333; }
.bar a { margin-left: auto; padding: 4px 10px; border-radius: 6px; background: #242424; font-size: 0.85rem; }
h1 { margin-top: 28px; font-size: clamp(1.35rem, 1.1rem + 1.1vw, 1.7rem); font-weight: 500; line-height: 1.22; letter-spacing: -0.02em; }
h1 span { color: #8E8E8E; }
h2 { margin: 44px 0 10px; font-size: 0.8rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; color: #8E8E8E; }
.rows li { display: grid; grid-template-columns: 84px minmax(0, 1fr); gap: 12px; align-items: baseline; padding-block: 3px; font-size: 1.2rem; letter-spacing: -0.015em; }
.tag { justify-self: start; padding: 1px 6px; border-radius: 4px; background: #242424; color: #A8A8A8; font-size: 0.68rem; letter-spacing: 0.04em; text-transform: uppercase; }
.rows small { display: block; font-size: 0.9rem; color: #8E8E8E; letter-spacing: 0; }
.rows a { display: inline-flex; gap: 6px; align-items: center; }
''', '''
<div class="wrap">
	<header class="bar"><div class="face">{{IMG}}</div><b>Mostafa Saher</b><a href="#email" data-focus-signup>Subscribe</a></header>
	<main>
		<h1 data-in>Mostafa Saher is a technical instructor <span>who teaches</span> AI and cloud, <span>one clear step at a time.</span></h1>
		<h2>Newsletter</h2>
		<div data-in style="--i:1">{{FORM}}</div>
		<h2>Writing index</h2>
		<ul class="rows">
			<li><span class="tag">Notes</span><span>Thoughts<small>What students get stuck on, and the explanation that made it click.</small></span></li>
			<li><span class="tag">Takes</span><span>Opinions<small>Where I stand on new models, cloud services and the hype.</small></span></li>
			<li><span class="tag">Links</span><span>Resources<small>Labs, docs, courses and tools I actually use.</small></span></li>
		</ul>
		<h2>Elsewhere</h2>
		<ul class="rows">
			<li><span class="tag">Social</span><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a></li>
			<li><span class="tag">Code</span><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a></li>
			<li><span class="tag">Mail</span><a href="mailto:mostafasaher@gmail.com">Email</a></li>
		</ul>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 13 after Vitalii Savchenko
page(13, 'centred-card', 'family=Figtree:wght@400..700', '#E9EAEE', '''
:root { --line: #E2E3E8; --focus: #1B1D24; --f-bg: #fff; --f-border: 1px solid #D5D7DE; --b-bg: #B9F04A; --b-text: #1B1D24; --note: #666A78; --f-radius: 999px; --b-radius: 999px; }
body { background: #E9EAEE; color: #1B1D24; font: 16px/1.55 "Figtree", system-ui, sans-serif; }
::selection { background: #B9F04A; color: #1B1D24; }
.wrap { --w: 980px; padding-block: 12px 0; }
.top { padding-inline: 8px; } .top a { font-weight: 600; }
.hero { padding: clamp(40px, 8vw, 88px) clamp(20px, 5vw, 64px); border-radius: 28px; background: #F6F7F9; text-align: center; }
.face { width: 64px; height: 64px; margin: 0 auto 18px; border-radius: 50%; background: #DDE0E8; }
.role { color: #666A78; font-size: 0.95rem; }
h1 { max-width: 15em; margin: 12px auto 26px; font-size: clamp(1.9rem, 1.2rem + 2.6vw, 3rem); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance; }
.signup { max-width: 430px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.after { margin: 56px auto 0; max-width: 620px; text-align: center; }
.after h2 { font-size: 1.5rem; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 10px; }
.after p { color: #555967; margin-bottom: 26px; }
.tp { text-align: left; } .li-inline { justify-content: center; margin-top: 28px; font-weight: 600; }
.foot { text-align: center; }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="hero" data-in>
			<div class="face">{{IMG}}</div>
			<p class="role">Technical instructor. AI and cloud.</p>
			<h1>People remember the class that finally made it click. I teach that one.</h1>
			{{FORM}}
		</section>
		<section class="after">
			<h2>Some of what I write.</h2>
			<p>{{INTRO}}</p>
			{{TOPICS_UL}}
			{{LINKS_INLINE}}
		</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 14 after Natan Novum
page(14, 'selection', 'family=Albert+Sans:wght@400..700', '#0B0B0D', '''
:root { color-scheme: dark; --blue: #3B6CFF; --line: #26262B; --focus: var(--blue); --f-bg: #17171B; --f-text: #F2F2F4; --f-ph: #8F8F98; --f-border: 1px solid #2B2B31; --b-bg: var(--blue); --b-text: #fff; --note: #8F8F98; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; }
body { background: #0B0B0D; color: #F2F2F4; font: 16px/1.55 "Albert Sans", system-ui, sans-serif; }
::selection { background: var(--blue); color: #fff; }
.top a { padding: 6px 12px; border-radius: 6px; background: var(--blue); font-size: 0.9rem; font-weight: 600; }
.stage { position: relative; display: grid; place-items: center; padding-block: clamp(36px, 8vh, 72px); }
.stage::before, .stage::after { content: ""; position: absolute; border: 0 dashed #2D3A6B; }
.stage::before { left: 0; right: 0; top: 50%; border-top-width: 1px; }
.stage::after { top: 0; bottom: 0; left: 50%; border-left-width: 1px; }
.sel { position: relative; z-index: 1; width: min(300px, 70%); aspect-ratio: 1; border: 1.5px solid var(--blue); background: radial-gradient(circle at 50% 40%, #3A3A44, #15151A 72%); }
.sel i { position: absolute; width: 9px; height: 9px; background: #fff; border: 1.5px solid var(--blue); }
.sel i:nth-child(1) { left: -5px; top: -5px; } .sel i:nth-child(2) { right: -5px; top: -5px; } .sel i:nth-child(3) { left: -5px; bottom: -5px; } .sel i:nth-child(4) { right: -5px; bottom: -5px; }
.sel .tagx { position: absolute; left: -1.5px; bottom: 100%; padding: 2px 8px; background: var(--blue); font-size: 0.72rem; font-weight: 600; }
.sel .face { position: absolute; inset: 0; }
.sel .face img { width: 124%; margin: 8% 0 0 -12%; }
h1 { font-size: clamp(1.7rem, 1.2rem + 2vw, 2.6rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.03em; }
h1 span { display: block; }
.grid { display: grid; gap: 24px 56px; padding-bottom: 12px; }
.grid p { color: #A9A9B2; margin: 12px 0 20px; max-width: 32em; }
@media (min-width: 860px) { .grid { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: end; } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<div class="stage" data-in><div class="sel"><span class="tagx">Instructor</span><div class="face">{{IMG}}</div><i></i><i></i><i></i><i></i></div></div>
		<div class="grid">
			<div data-in style="--i:1"><h1><span>Mostafa Saher</span><span>AI and cloud instructor</span></h1><p>{{INTRO}}</p>{{FORM}}</div>
			<div data-in style="--i:2">{{LINKS_ROWS}}</div>
		</div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 15 after Omkar Talwalkar
page(15, 'inline-chips', 'family=Sora:wght@300..600', '#0A0A0A', '''
:root { color-scheme: dark; --line: #262626; --focus: #fff; --f-bg: #161616; --f-text: #F4F4F4; --f-ph: #909090; --f-border: 1px solid #2A2A2A; --b-bg: #F4F4F4; --b-text: #0A0A0A; --note: #909090; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; }
body { background: #0A0A0A radial-gradient(60% 50% at 80% 0%, #1E2230, transparent); background-repeat: no-repeat; color: #F4F4F4; font: 15px/1.6 "Sora", system-ui, sans-serif; text-align: center; }
::selection { background: #F4F4F4; color: #0A0A0A; }
h1 { margin: clamp(48px, 12vh, 120px) auto 0; max-width: 17em; font-size: clamp(1.6rem, 1.1rem + 2.2vw, 2.7rem); font-weight: 300; line-height: 1.5; letter-spacing: -0.02em; }
.chip { display: inline-block; vertical-align: middle; padding: 0.15em 0.7em; margin-inline: 0.1em; border-radius: 999px; font-size: 0.6em; line-height: 1.4; font-weight: 600; }
.c1 { background: #5B8CFF; color: #06122E; } .c2 { background: #7DE0B5; color: #052416; }
h1 .face { display: inline-block; vertical-align: middle; width: 1.25em; height: 1.25em; border-radius: 50%; background: #333; margin-inline: 0.1em; }
.sub { max-width: 34em; margin: 22px auto 28px; color: #A8A8A8; }
.signup { max-width: 430px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.li-inline { justify-content: center; margin-top: 44px; }
.tp { max-width: 560px; margin: 72px auto 0; text-align: left; }
.foot { margin-top: 24px; }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<h1 data-in>Hey, I’m <span class="face">{{IMG}}</span> Mostafa. An instructor teaching <span class="chip c1">AI</span> and <span class="chip c2">cloud</span> one clear step at a time.</h1>
		<p class="sub" data-in style="--i:1">{{INTRO}}</p>
		<div data-in style="--i:2">{{FORM}}</div>
		{{LINKS_INLINE}}
		{{TOPICS_UL}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 16 after Chi Quach
page(16, 'serif-caps', 'family=Bodoni+Moda:opsz,wght@6..96,400..600&family=Hanken+Grotesk:wght@400..600', '#FFFFFF', '''
:root { --line: #E4E4E4; --focus: #111; --f-bg: #F3F3F3; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 15px/1.5 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #111; color: #fff; }
.hero { position: relative; min-height: min(92svh, 780px); padding-top: 24px; overflow: hidden; }
h1 { position: relative; z-index: 2; font-family: "Bodoni Moda", serif; font-size: clamp(3.4rem, 1rem + 11vw, 9rem); font-weight: 400; line-height: 0.9; letter-spacing: -0.03em; text-transform: uppercase; mix-blend-mode: multiply; }
.hero figure { position: absolute; z-index: 1; right: -4%; bottom: 0; width: min(70%, 520px); }
.metas { position: relative; z-index: 2; display: grid; grid-template-columns: repeat(2, minmax(0, 150px)); gap: 14px 24px; margin-top: 32px; font-size: 0.8rem; }
.metas b { display: block; font-weight: 600; }
.metas a { text-decoration: underline; text-underline-offset: 3px; }
.below { display: grid; gap: 28px 56px; padding-block: 48px 8px; border-top: 1px solid #111; }
.below h2 { font-family: "Bodoni Moda", serif; font-size: 2rem; font-weight: 400; line-height: 1; margin-bottom: 14px; }
.below p { margin-bottom: 18px; max-width: 34em; color: #444; }
.field { gap: 0; }
@media (min-width: 860px) { .below { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } .hero figure { right: 6%; width: 40%; } }
''', '''
<div class="wrap">
	<main>
		<section class="hero">
			<h1 data-in>Mostafa,<br>Saher</h1>
			<div class="metas" data-in style="--i:2">
				<p><b>Role</b>Technical instructor</p><p><b>Subjects</b>AI and cloud</p>
				<p><b>Newsletter</b><a href="#email" data-focus-signup>Subscribe</a></p><p><b>Contact</b><a href="mailto:mostafasaher@gmail.com">Email</a></p>
			</div>
			<figure data-in style="--i:1">{{IMG}}</figure>
		</section>
		<section class="below">
			<div><h2>{{H}}</h2><p>{{INTRO}}</p>{{FORM}}</div>
			<div>{{TOPICS_UL}}<div style="margin-top:24px">{{LINKS_INLINE}}</div></div>
		</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 17 after Nidhi Prajapati
page(17, 'quiet-corner', 'family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=Geist:wght@400;500', '#F7F5EF', '''
:root { --line: #DFDBCF; --focus: #1A1915; --f-bg: #fff; --f-border: 1px solid #DFDBCF; --b-bg: #1A1915; --b-text: #F7F5EF; --note: #6F6B5E; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #F7F5EF; color: #1A1915; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #1A1915; color: #F7F5EF; }
.screen { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; }
.top b { font: 400 1.3rem "Newsreader", serif; }
.mid { display: grid; place-items: center; padding-block: 16px; }
.mid figure { width: min(280px, 62%); }
.mid img { filter: grayscale(1) contrast(1.05); -webkit-mask-image: linear-gradient(#000 72%, transparent); mask-image: linear-gradient(#000 72%, transparent); }
.low { display: grid; gap: 22px 40px; align-items: end; padding-bottom: 28px; }
h1 { font: 400 clamp(2rem, 1.3rem + 2.6vw, 3.1rem)/1 "Newsreader", serif; letter-spacing: -0.02em; }
h1 em { display: block; }
.after { display: grid; gap: 24px 56px; padding-block: 44px 8px; border-top: 1px solid var(--line); }
.after p { max-width: 34em; color: #55524A; }
@media (min-width: 820px) { .low { grid-template-columns: minmax(0, 1fr) 400px; } .after { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="wrap">
	<div class="screen">
		{{TOP}}
		<div class="mid" data-in><figure>{{IMG}}</figure></div>
		<div class="low">
			<h1 data-in style="--i:1">the notes of a <em>curious instructor.</em></h1>
			<div data-in style="--i:2">{{FORM}}</div>
		</div>
	</div>
	<main class="after">
		<p>I’m Mostafa Saher. I teach AI and cloud, one clear step at a time. {{INTRO}}</p>
		<div>{{TOPICS_UL}}<div style="margin-top:22px">{{LINKS_INLINE}}</div></div>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 18 after Jenny Wen
page(18, 'handwritten', 'family=Kalam:wght@700&family=Golos+Text:wght@400..600', '#FFFFFF', '''
:root { --line: #F0DDD3; --focus: #1B1B1B; --f-bg: #fff; --f-border: 1.5px solid #1B1B1B; --b-bg: #1B1B1B; --b-text: #fff; --note: #7A5E50; --f-radius: 12px; --b-radius: 7px; --w: 700px; }
body { background: #fff; color: #1B1B1B; font: 16px/1.6 "Golos Text", system-ui, sans-serif; }
::selection { background: #FFD9C7; }
.head { display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; padding-top: 28px; }
h1 { font: 700 clamp(2.4rem, 1.6rem + 3vw, 3.4rem)/1 "Kalam", cursive; transform: rotate(-2deg); transform-origin: 0 100%; }
.head .li-inline { flex-direction: column; gap: 2px; text-align: right; font-size: 0.9rem; } .head .l-go { display: none; }
.bio { margin-top: 22px; font-size: 1.05rem; }
.bio + .bio { margin-top: 12px; }
h2 { margin: 40px 0 12px; font-size: 0.85rem; font-weight: 500; color: #8A6A5A; }
.peach { padding: 22px; border-radius: 14px; background: #FFE9DE; }
.peach p { margin-bottom: 14px; }
.pic { display: flex; align-items: flex-end; gap: 16px; margin-top: 12px; padding: 20px 20px 0; border-radius: 14px; background: #FBF1EB; overflow: hidden; }
.pic figure { flex: none; width: 150px; margin-bottom: -6px; }
.pic p { padding-bottom: 20px; font: 700 1.5rem/1.15 "Kalam", cursive; }
''', '''
<div class="wrap">
	<header class="head"><h1 data-in>Mostafa Saher</h1>{{LINKS_INLINE}}</header>
	<main>
		<p class="bio" data-in style="--i:1">I’m a technical instructor, and I teach AI and cloud one clear step at a time.</p>
		<p class="bio" data-in style="--i:1">{{INTRO}}</p>
		<h2>Now</h2>
		<section class="peach" data-in style="--i:2"><p><b>The newsletter.</b> Everything that used to stay in the corridor after class, sent to your inbox.</p>{{FORM}}</section>
		<div class="pic"><figure>{{IMG}}</figure><p>“Wait, so why does that work?”</p></div>
		<h2>What’s inside</h2>
		{{TOPICS_UL}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 19 after Ilia Lushnikov
page(19, 'colour-blocks', 'family=Red+Hat+Display:wght@400..800', '#FFFFFF', '''
:root { --line: #E6E6E6; --focus: #111; --f-bg: #F2F2F2; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 10px; --b-radius: 6px; }
body { background: #fff; color: #111; font: 16px/1.5 "Red Hat Display", system-ui, sans-serif; }
::selection { background: #FF3D6E; color: #fff; }
.top a { padding: 6px 14px; border-radius: 999px; background: #111; color: #fff; font-size: 0.9rem; font-weight: 600; }
.intro { display: grid; gap: 20px 48px; padding-block: 20px 44px; }
.pic { width: 132px; aspect-ratio: 4 / 5; background: #ECECEC; overflow: hidden; }
.pic img { width: 128%; max-width: none; margin: 6% 0 0 -14%; }
h1 { margin-top: 14px; font-size: clamp(2.6rem, 1.6rem + 4vw, 4.4rem); font-weight: 500; line-height: 0.95; letter-spacing: -0.045em; }
.role { margin-top: 6px; font-size: 1.1rem; }
.intro p.say { color: #555; max-width: 32em; margin-bottom: 18px; }
h2 { text-align: center; font-size: clamp(1.6rem, 1.2rem + 1.6vw, 2.3rem); font-weight: 500; letter-spacing: -0.03em; margin-bottom: 20px; }
.blocks { display: grid; gap: 8px; }
.blocks li { min-height: 190px; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; color: #fff; }
.blocks b { font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; text-transform: uppercase; line-height: 1; }
.blocks li:nth-child(1) { background: #FF3D6E; } .blocks li:nth-child(2) { background: #E02A1F; } .blocks li:nth-child(3) { background: #1F5FE0; }
.li-inline { justify-content: center; margin-top: 36px; font-weight: 600; }
.foot { text-align: center; }
@media (min-width: 820px) { .intro { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: end; } .blocks { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<section class="intro">
			<div data-in><div class="pic">{{IMG}}</div><h1>mostafa saher</h1><p class="role">Technical instructor (AI/cloud)</p></div>
			<div data-in style="--i:1"><p class="say">{{INTRO}}</p>{{FORM}}</div>
		</section>
		<h2>Selected writing</h2>
		<ul class="blocks" data-in style="--i:2">
			<li><b>Thoughts</b><span>Notes from the classroom: what students get stuck on, and the explanation that made it click.</span></li>
			<li><b>Opinions</b><span>Where I stand on new models, cloud services and the hype around them.</span></li>
			<li><b>Resources</b><span>The labs, docs, courses and tools I actually use, each with a line on why.</span></li>
		</ul>
		{{LINKS_INLINE}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 20 after Ivan Annikov
page(20, 'two-band', 'family=Rethink+Sans:wght@400..700', '#F4EFE6', '''
:root { --line: #3A3A44; --focus: #E7A93B; --f-bg: #fff; --f-border: 1px solid #D9D2C4; --b-bg: #E7A93B; --b-text: #1C1C22; --note: #6E6858; --f-radius: 10px; --b-radius: 6px; }
body { background: #F4EFE6; color: #1C1C22; font: 16px/1.55 "Rethink Sans", system-ui, sans-serif; }
::selection { background: #E7A93B; color: #1C1C22; }
.top a { padding: 6px 12px; border-radius: 6px; background: #E7A93B; font-size: 0.9rem; font-weight: 600; }
.hi { display: grid; gap: 24px 40px; align-items: center; padding-block: 28px 56px; }
.face { width: 150px; height: 150px; border-radius: 50%; background: #E2D9C8; }
h1 { font-size: clamp(1.8rem, 1.3rem + 1.8vw, 2.5rem); font-weight: 700; letter-spacing: -0.03em; line-height: 1.1; }
.hi p { margin: 10px 0 14px; max-width: 30em; font-size: 1.1rem; }
.hi ul.dots { margin-bottom: 20px; color: #5A5548; font-size: 0.92rem; }
.dots li::before { content: "•"; color: #E7A93B; margin-right: 8px; }
.signup { max-width: 440px; }
.band { background: #1C1C22; color: #F1EEE7; padding-block: 48px; }
.band h2 { font-size: 0.8rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #E7A93B; margin-bottom: 18px; }
.three { display: grid; gap: 12px; }
.three li { padding: 20px; border: 1px solid var(--line); border-radius: 10px; }
.three b { display: block; font-size: 1.15rem; margin-bottom: 6px; } .three span { color: #B5B2A9; font-size: 0.95rem; }
.band .li-rows { margin-top: 36px; }
@media (min-width: 800px) { .hi { grid-template-columns: 150px minmax(0, 1fr); } .three { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
''', '''
<div class="wrap">{{TOP}}
	<section class="hi">
		<div class="face" data-in>{{IMG}}</div>
		<div data-in style="--i:1">
			<h1>Hi, I’m Mostafa.</h1>
			<p>I teach AI and cloud, one clear step at a time, and write down what comes up after class.</p>
			<ul class="dots"><li>Technical instructor</li><li>AI and cloud</li><li>Newsletter writer</li></ul>
			{{FORM}}
		</div>
	</section>
</div>
<main class="band"><div class="wrap">
	<h2>What I write</h2>
	<ul class="three">
	{{TOPICS}}
	</ul>
	{{LINKS_ROWS}}
	<footer class="foot">{{FOOT}}</footer>
</div></main>
''')
print('batch 1 done')
