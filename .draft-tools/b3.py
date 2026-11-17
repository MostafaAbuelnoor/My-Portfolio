from lib import page
import random

# 31 after George Wood
page(31, 'all-blue', 'family=Geist:wght@400..600', '#1F4BFF', '''
:root { --line: rgb(255 255 255 / 0.35); --focus: #fff; --f-bg: #fff; --b-bg: #0A1440; --b-text: #fff; --note: #D5DDFF; --err: #FFD9D2; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #1F4BFF; color: #fff; font: 14px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #fff; color: #1F4BFF; }
.id { display: flex; align-items: center; gap: 12px; padding-block: 20px; }
.face { width: 44px; height: 44px; background: #5F7FFF; }
.id span { display: block; color: #D5DDFF; }
.id a { margin-left: auto; padding: 5px 10px; border: 1px solid var(--line); }
.cols { display: grid; gap: 16px 40px; padding-block: 12px 36px; }
h1 { font-size: 1rem; font-weight: 400; }
.tbl { border-top: 1px solid var(--line); }
.tbl li { display: grid; grid-template-columns: 110px minmax(0, 1fr); gap: 16px; padding-block: 10px; border-bottom: 1px solid var(--line); }
.tbl b { font-weight: 500; } .tbl a { text-decoration: underline; text-underline-offset: 3px; }
.join { padding-block: 36px; max-width: 440px; }
.join h2 { font-size: 1.5rem; font-weight: 500; letter-spacing: -0.02em; margin-bottom: 14px; }
.end { background: #0A1440; margin-top: 12px; }
.end .in { display: flex; align-items: flex-end; gap: 20px; }
.end figure { width: 150px; flex: none; margin-top: -60px; }
.end p { padding-bottom: 22px; color: #B9C4F5; }
@media (min-width: 820px) { .cols { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="wrap">
	<header class="id"><div class="face">{{IMG}}</div><div><b>Mostafa Saher</b><span>Technical instructor, AI and cloud</span></div><a href="#email" data-focus-signup>Subscribe</a></header>
	<main>
		<div class="cols" data-in><h1>I’m a technical instructor teaching AI and cloud, one clear step at a time.</h1><p>{{INTRO}}</p></div>
		<ul class="tbl" data-in style="--i:1">
			<li><b>Thoughts</b><span>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</span></li>
			<li><b>Opinions</b><span>Where I stand on new models, cloud services and the hype around them.</span></li>
			<li><b>Resources</b><span>The labs, docs, courses and tools I actually use, each with a line on why.</span></li>
			<li><b>LinkedIn</b><a href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">Mostafa Abuelnoor</a></li>
			<li><b>GitHub</b><a href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">@MostafaAbuelnoor</a></li>
			<li><b>Email</b><a href="mailto:mostafasaher@gmail.com">mostafasaher@gmail.com</a></li>
		</ul>
		<section class="join" data-in style="--i:2"><h2>Soon in your inbox.</h2>{{FORM}}</section>
	</main>
</div>
<footer class="end"><div class="wrap in"><figure>{{IMG}}</figure><p>{{FOOT}}</p></div></footer>
''')

# 32 after Tiffany Devos
random.seed(7)
pal = ['#FF5A36', '#C9B3FF', '#1447FF', '#FFB3D1', '#17C98B', '#6B0F1A', '#FFD23F', '#FFFFFF']
cells = ''.join(f'<i style="background:{random.choice(pal)}"></i>' for _ in range(48))
page(32, 'pattern-band', 'family=Epilogue:wght@400..700', '#FFFFFF', '''
:root { --line: #E6E6E6; --focus: #1447FF; --f-bg: #F3F3F3; --b-bg: #1447FF; --b-text: #fff; --note: #666; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 14px/1.55 "Epilogue", system-ui, sans-serif; }
::selection { background: #FFD23F; }
.head { display: grid; gap: 14px 40px; padding-block: 20px 28px; }
.head p { max-width: 34em; }
.head .li-inline { margin-top: 10px; font-weight: 600; text-transform: uppercase; font-size: 0.78rem; letter-spacing: 0.04em; }
.band { position: relative; }
.cells { display: grid; grid-template-columns: repeat(8, 1fr); }
.cells i { aspect-ratio: 1; }
.band figure { position: absolute; left: 50%; bottom: 0; height: 118%; aspect-ratio: 1100 / 1433; transform: translateX(-50%); }
.band figure img { height: 100%; width: auto; max-width: none; }
.low { display: grid; gap: 24px 56px; padding-block: 40px 8px; }
h1 { font-size: clamp(1.9rem, 1.2rem + 2.6vw, 3rem); font-weight: 700; line-height: 1.02; letter-spacing: -0.04em; max-width: 12em; }
.field { gap: 0; }
@media (min-width: 820px) { .head { grid-template-columns: 1fr 1fr; } .cells { grid-template-columns: repeat(16, 1fr); } .cells i:nth-child(n+49) { display: none; } .low { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: end; } }
@media (max-width: 819px) { .cells i:nth-child(n+33) { display: none; } }
''', '''
<div class="wrap">
	<header class="head"><b>Mostafa Saher</b><div><p>Want to make AI and cloud make sense? You’ve come to the right place. I’m a technical instructor, and I teach one clear step at a time.</p>{{LINKS_INLINE}}</div></header>
</div>
<div class="band" data-in><div class="cells" aria-hidden="true">''' + cells + '''</div><figure>{{IMG}}</figure></div>
<main class="wrap low">
	<h1 data-in style="--i:1">{{H}}</h1>
	<div data-in style="--i:2"><p style="margin-bottom:14px">{{INTRO}}</p>{{FORM}}</div>
</main>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 33 after Britt Taylor
page(33, 'big-talk', 'family=Bricolage+Grotesque:opsz,wght@12..96,500..800', '#1C1C1C', '''
:root { color-scheme: dark; --pink: #FF7AB8; --line: #383838; --focus: var(--pink); --f-bg: #2A2A2A; --f-text: #F5F2EA; --f-ph: #A19E96; --b-bg: var(--pink); --b-text: #1C1C1C; --note: #A19E96; --err: #FF9B8F; --f-radius: 999px; --b-radius: 999px; --w: 860px; }
body { background: #1C1C1C; color: #F5F2EA; font: 16px/1.55 "Bricolage Grotesque", system-ui, sans-serif; text-align: center; }
::selection { background: var(--pink); color: #1C1C1C; }
.say { margin: 0 auto; max-width: 13em; font-size: clamp(1.9rem, 1.1rem + 4.2vw, 4rem); font-weight: 700; line-height: 1.02; letter-spacing: -0.04em; text-wrap: balance; }
.say + .say, .blob + .say { margin-top: 0.9em; }
.say em { font-style: normal; color: var(--pink); } .say u { text-decoration: none; color: #8FD8FF; }
h1.say { margin-top: clamp(28px, 8vh, 72px); }
.blob { width: min(250px, 60%); margin: 40px auto 0; border-radius: 46% 54% 50% 50% / 55% 48% 52% 45%; background: var(--pink); overflow: hidden; }
.blob img { width: 112%; max-width: none; margin: 8% 0 0 -6%; }
.join { max-width: 440px; margin: 48px auto 0; text-align: left; } .note { text-align: center; }
.tp { margin-top: 64px; text-align: left; } .li-inline { justify-content: center; margin-top: 32px; font-weight: 600; }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<h1 class="say" data-in>Remember when the class ended and the <em>real questions</em> started?</h1>
		<div class="blob" data-in style="--i:1">{{IMG}}</div>
		<p class="say">The corridor ones. The <u>“wait, so why does that work?”</u></p>
		<p class="say">I’m Mostafa. I teach <em>AI and cloud</em>, and I write those down.</p>
		<div class="join">{{FORM}}</div>
		{{TOPICS_UL}}
		{{LINKS_INLINE}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 34 after Felix Haas
page(34, 'letter', 'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&family=Reenie+Beanie&family=Geist:wght@400;500', '#FFFFFF', '''
:root { --line: #E7E5DE; --focus: #171715; --f-bg: #F5F4EF; --b-bg: #171715; --b-text: #fff; --note: #77756C; --f-radius: 8px; --b-radius: 4px; --w: 640px; }
body { background: #fff; color: #171715; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #171715; color: #fff; }
.from { padding-block: clamp(40px, 12vh, 120px) clamp(32px, 8vh, 72px); text-align: center; font-size: 0.85rem; color: #77756C; }
.from b { color: #171715; font-weight: 500; }
.body p { font: 400 clamp(1.15rem, 1rem + 0.5vw, 1.32rem)/1.55 "Source Serif 4", Georgia, serif; }
.body p + p { margin-top: 1.1em; }
.sig { margin-top: 20px; font: 400 3rem/1 "Reenie Beanie", cursive; transform: rotate(-3deg); transform-origin: 0 50%; }
.ps { margin-top: 44px; padding-top: 24px; border-top: 1px solid var(--line); }
.ps p { margin-bottom: 14px; font: italic 400 1.1rem/1.5 "Source Serif 4", Georgia, serif; }
.li-inline { margin-top: 28px; }
.peek { width: min(300px, 70%); margin: 56px auto 0; height: 210px; overflow: hidden; }
''', '''
<div class="wrap">
	<p class="from" data-in>A letter from <b>Mostafa Saher</b></p>
	<main>
		<div class="body" data-in style="--i:1">
			<p>Dear reader,</p>
			<p>I teach AI and cloud for a living. The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p>
			<p>I have started writing those down. Thoughts from the classroom, where I stand on the latest models and cloud services, and the resources I’d actually hand a student. One clear step at a time, the way I’d explain it to you in person.</p>
			<p>If that sounds useful, leave me your email and I’ll write to you.</p>
		</div>
		<p class="sig" data-in style="--i:2">Mostafa</p>
		<section class="ps"><p>P.S. It’s free, and you can leave whenever you like.</p>{{FORM}}{{LINKS_INLINE}}</section>
		<div class="peek">{{IMG}}</div>
	</main>
</div>
''')

# 35 after Zara Webb
page(35, 'half-photo', 'family=Gilda+Display&family=Geist:wght@400;500', '#F6F0E1', '''
:root { --green: #2F5D46; --line: #E0D8C4; --focus: var(--green); --f-bg: #fff; --f-border: 1px solid #D8CFB8; --b-bg: var(--green); --b-text: #fff; --note: #746C58; --f-radius: 999px; --b-radius: 999px; }
body { background: #F6F0E1; color: #25231C; font: 15px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: var(--green); color: #fff; }
.split { display: grid; }
.left { display: grid; grid-template-rows: auto 1fr; padding: 0 clamp(18px, 4vw, 40px) 40px; text-align: center; }
.left .top { font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; }
.mid { align-self: center; padding-block: 32px; }
h1 { font: 400 clamp(2rem, 1.3rem + 2.4vw, 3.1rem)/1.12 "Gilda Display", serif; max-width: 11em; margin: 0 auto 18px; text-wrap: balance; }
.mid p.sub { max-width: 28em; margin: 0 auto 22px; color: #5B5545; }
.signup { max-width: 420px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.right { background: #D9C7A6; display: flex; justify-content: center; align-items: flex-end; height: 56svh; overflow: hidden; }
.right img { height: 96%; width: auto; max-width: none; }
.more { display: grid; gap: 28px 56px; padding-block: 44px 8px; }
@media (min-width: 880px) { .split { grid-template-columns: 1fr 1fr; min-height: 100svh; } .right { height: auto; } .more { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="split">
	<div class="left">
		{{TOP}}
		<main class="mid"><h1 data-in>Support for AI and cloud, through the first class and beyond.</h1><p class="sub" data-in style="--i:1">I’m Mostafa Saher, a technical instructor. I teach one clear step at a time, and my newsletter carries what comes up after class.</p><div data-in style="--i:2">{{FORM}}</div></main>
	</div>
	<div class="right">{{IMG}}</div>
</div>
<section class="wrap more">{{TOPICS_UL}}{{LINKS_ROWS}}</section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 36 after Justin Lerner
page(36, 'letter-grid', 'family=Zilla+Slab:wght@600;700&family=Geist:wght@400;500', '#FFFFFF', '''
:root { --line: #E4E4E4; --focus: #111; --f-bg: #F3F3F3; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 10px; --b-radius: 6px; }
body { background: #fff; color: #111; font: 15px/1.55 "Geist", system-ui, sans-serif; }
::selection { background: #FFD23F; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); border-left: 1px solid var(--line); }
.grid > * { aspect-ratio: 1; display: grid; place-items: center; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); overflow: hidden; }
.grid b { font: 700 clamp(1.6rem, 1rem + 2.4vw, 2.6rem)/1 "Zilla Slab", serif; }
.grid a { font-weight: 500; text-decoration: underline; text-underline-offset: 4px; transition: background-color 160ms ease; }
.grid .face { place-items: start; background: #F1EADB; } .grid .face img { width: 150%; margin: 4% 0 0 -25%; }
.sh { width: 38%; aspect-ratio: 1; }
.s1 { border-radius: 50%; background: #FF5A36; } .s2 { background: #1447FF; transform: rotate(45deg); } .s3 { border-radius: 50% 50% 0 0; background: #17C98B; } .s4 { background: #FFD23F; border-radius: 50% 0 50% 0; }
.low { display: grid; gap: 24px 56px; padding-block: 40px 8px; }
h1 { font: 700 clamp(1.8rem, 1.2rem + 2vw, 2.6rem)/1.08 "Zilla Slab", serif; letter-spacing: -0.02em; max-width: 13em; }
@media (hover: hover) and (pointer: fine) { .grid a:hover { background: #F6F6F6; } }
@media (min-width: 820px) { .grid { grid-template-columns: repeat(5, 1fr); } .low { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
@media (prefers-reduced-motion: no-preference) { .grid > * > * { animation: pop 500ms var(--ease-out) backwards; animation-delay: calc(var(--k) * 45ms); } @keyframes pop { from { opacity: 0; transform: scale(0.9); } } }
''', '''
<div class="wrap">
	{{TOP}}
	<div class="grid">
		<div style="--k:0"><b>M</b></div><div style="--k:1"><i class="sh s1"></i></div><div class="face" style="--k:2">{{IMG}}</div><div style="--k:3"><b>O</b></div><div style="--k:4"><b>S</b></div>
		<div style="--k:5"><b>T</b></div><a style="--k:6" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener"><span>LinkedIn</span></a><div style="--k:7"><b>A</b></div><div style="--k:8"><i class="sh s2"></i></div><div style="--k:9"><b>F</b></div>
		<a style="--k:10" href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener"><span>GitHub</span></a><div style="--k:11"><b>A</b></div><div style="--k:12"><i class="sh s3"></i></div><a style="--k:13" href="mailto:mostafasaher@gmail.com"><span>Email</span></a><div style="--k:14"><i class="sh s4"></i></div>
	</div>
	<main class="low">
		<div><h1>{{H}}</h1><p style="margin:14px 0 18px;color:#555;max-width:32em">{{INTRO}}</p>{{FORM}}</div>
		{{TOPICS_UL}}
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 37 after Shawn Golden
page(37, 'windows', 'family=Old+Standard+TT:wght@700&family=Pixelify+Sans:wght@400;600', '#008080', '''
:root { --line: #808080; --focus: #000080; --f-bg: #fff; --b-bg: #C0C0C0; --b-text: #000; --note: #222; --f-radius: 0; --b-radius: 0; --f-pad: 3px; --f-border: 2px inset #fff; }
body { background: #008080; color: #000; font: 14px/1.5 Tahoma, Verdana, "Segoe UI", sans-serif; }
::selection { background: #000080; color: #fff; }
.mast { background: #fff; border-bottom: 2px solid #000; overflow: hidden; }
h1 { font: 700 min(9.4vw, 8.4rem)/0.9 "Old Standard TT", serif; text-transform: uppercase; letter-spacing: -0.02em; white-space: nowrap; padding: 10px 14px 4px; }
.tick { padding: 4px 14px; border-top: 1px solid #000; color: #0000EE; font-style: italic; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.tick a { text-decoration: underline; }
.desk { display: grid; gap: 18px; padding: 18px 14px 40px; max-width: 1100px; margin-inline: auto; }
.win { background: #C0C0C0; border: 2px outset #fff; box-shadow: 2px 2px 0 #000; }
.bar { display: flex; justify-content: space-between; align-items: center; margin: 2px; padding: 3px 6px; background: #000080; color: #fff; font: 600 0.95rem "Pixelify Sans", Tahoma, sans-serif; }
.bar i { width: 16px; height: 14px; background: #C0C0C0; border: 2px outset #fff; }
.in { padding: 12px; }
.in.white { margin: 0 6px 6px; background: #fff; border: 2px inset #fff; }
.btn { border: 2px outset #fff; font-weight: 400; height: 40px; } .btn:active { border-style: inset; transform: none; } .btn svg { display: none; }
.field input { height: 40px; }
.pic { background: #5A9; display: flex; justify-content: center; align-items: flex-end; height: 260px; overflow: hidden; }
.pic img { height: 100%; width: auto; max-width: none; }
.li-rows a { padding-block: 6px; border: 0 !important; color: #0000EE; text-decoration: underline; } .li-rows .l-meta { color: #000; opacity: 1; }
.tp li { border-color: #C0C0C0; padding-block: 8px; }
.foot { color: #fff; opacity: 1; text-align: center; padding: 0 0 24px; }
@media (min-width: 860px) { .desk { grid-template-columns: 1.15fr 0.85fr; align-items: start; } .w1 { grid-row: span 2; } }
''', '''
<header class="mast"><h1>Mostafa Saher</h1><p class="tick">Contact me at <a href="mailto:mostafasaher@gmail.com">mostafasaher@gmail.com</a> · technical instructor · AI and cloud · one clear step at a time</p></header>
<main class="desk">
	<section class="win w1" data-in><div class="bar"><span>newsletter.exe</span><i></i></div><div class="in"><p style="margin-bottom:10px"><b>{{H}}</b></p><p style="margin-bottom:12px">{{INTRO}}</p>{{FORM}}</div></section>
	<section class="win" data-in style="--i:1"><div class="bar"><span>mostafa.bmp</span><i></i></div><div class="in"><div class="pic">{{IMG}}</div></div></section>
	<section class="win" data-in style="--i:2"><div class="bar"><span>links.txt</span><i></i></div><div class="in white">{{LINKS_ROWS}}</div></section>
	<section class="win" data-in style="--i:3"><div class="bar"><span>topics.txt</span><i></i></div><div class="in white">{{TOPICS_UL}}</div></section>
</main>
<footer class="foot">{{FOOT}}</footer>
''')

# 38 after Ryan Brewer
page(38, 'ground', 'family=Geist:wght@400;500', '#1456F0', '''
:root { --line: rgb(255 255 255 / 0.4); --focus: #fff; --f-bg: #fff; --b-bg: #0B2A7A; --b-text: #fff; --note: #D6E2FF; --err: #FFD9D2; --f-radius: 4px; --b-radius: 2px; --f-pad: 4px; }
body { background: #1456F0; color: #fff; font: 14px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #fff; color: #1456F0; }
.sky { position: relative; min-height: 100svh; display: grid; grid-template-rows: 1fr auto; overflow: hidden; }
.text { display: grid; gap: 14px 40px; align-content: start; padding-block: 28px; }
.text .col { max-width: 30em; }
.text p + p { margin-top: 12px; }
.text a.u { text-decoration: underline; text-underline-offset: 3px; }
.signup { margin-top: 18px; max-width: 400px; }
.floor { position: relative; height: 54px; background: #5B3A1E; border-top: 14px solid #2FA84F; }
.floor figure { position: absolute; left: 50%; bottom: 16px; width: min(260px, 62%); transform: translateX(-50%); }
@media (min-width: 820px) { .text { grid-template-columns: 180px minmax(0, 30em); } .floor figure { left: auto; right: 9%; transform: none; width: 330px; } }
@media (prefers-reduced-motion: no-preference) { .floor figure { animation: grow 1100ms var(--ease-out) 200ms backwards; transform-origin: 50% 100%; } @keyframes grow { from { translate: 0 30%; opacity: 0; } } }
''', '''
<main class="sky">
	<div class="wrap text">
		<b data-in>Mostafa Saher</b>
		<div class="col" data-in style="--i:1">
			<p>I’m a technical instructor. I teach AI and cloud, one clear step at a time.</p>
			<p>The best part of every class comes once it’s over: the questions in the corridor, the “wait, so why does that work?”, the links I send people afterwards.</p>
			<p>I’m interested in writing those down. My newsletter is where they go now.</p>
			<p><a class="u" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a> · <a class="u" href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a> · <a class="u" href="mailto:mostafasaher@gmail.com">mostafasaher@gmail.com</a></p>
			{{FORM}}
		</div>
	</div>
	<div class="floor"><figure>{{IMG}}</figure></div>
</main>
''')

# 39 after Julianna Wang
page(39, 'sentence-pills', 'family=Instrument+Serif:ital@0;1&family=Geist:wght@400..600', '#FFFFFF', '''
:root { --line: #EAEAEA; --focus: #6B4CE6; --f-bg: #F4F4F4; --b-bg: #6B4CE6; --b-text: #fff; --note: #6A6A6A; --f-radius: 12px; --b-radius: 8px; --w: 900px; }
body { background: #fff; color: #161616; font: 15px/1.65 "Geist", system-ui, sans-serif; }
::selection { background: #D9CFFF; }
.top b { font: italic 400 1.4rem "Instrument Serif", serif; }
h1 { margin-top: clamp(36px, 10vh, 96px); font-size: clamp(1.6rem, 1.1rem + 2vw, 2.5rem); font-weight: 400; line-height: 1.32; letter-spacing: -0.025em; }
h1 .face { display: inline-block; vertical-align: -0.2em; width: 1.3em; height: 1.3em; border-radius: 0.35em; background: #E7E0FF; margin-right: 0.15em; }
h1 i { display: inline-block; vertical-align: 0.08em; padding: 0.1em 0.55em; border-radius: 999px; font: 600 0.5em/1.5 "Geist", sans-serif; }
.p1 { background: #CFE6FF; color: #0B3A75; } .p2 { background: #FFE39B; color: #5A3D00; } .p3 { background: #BFEFD6; color: #0B4A2A; }
h1 em { font: italic 400 1.12em "Instrument Serif", serif; }
.say { margin: 24px 0 28px; max-width: 46em; color: #555; } .say b { color: #161616; font-weight: 600; }
.signup { max-width: 440px; }
.two { display: grid; gap: 28px 56px; margin-top: 64px; }
@media (min-width: 820px) { .two { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); } }
''', '''
<div class="wrap">
	{{TOP}}
	<main>
		<h1 data-in><span class="face">{{IMG}}</span> Hi, I’m Mostafa, a technical instructor, <i class="p1">AI</i> an AI explainer, <i class="p2">Cloud</i> a cloud guide, <i class="p3">Notes</i> and an <em>after-class note-taker.</em></h1>
		<p class="say" data-in style="--i:1">I teach <b>AI and cloud</b>, one clear step at a time. The best part of every class comes once it’s over: <b>the questions in the corridor</b>, the “wait, so why does that work?”, the links I send people afterwards. My newsletter is where that goes now.</p>
		<div data-in style="--i:2">{{FORM}}</div>
		<section class="two">{{TOPICS_UL}}{{LINKS_ROWS}}</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')

# 40 after Mark Hurrell
page(40, 'top-and-bottom', 'family=Host+Grotesk:wght@400..700', '#FFFFFF', '''
:root { --line: #111; --focus: #111; --f-bg: #F2F2F2; --b-bg: #111; --b-text: #fff; --note: #555; --f-radius: 0; --b-radius: 0; --f-pad: 0; }
body { background: #fff; color: #111; font: 600 clamp(1.05rem, 0.95rem + 0.6vw, 1.4rem)/1.18 "Host Grotesk", system-ui, sans-serif; letter-spacing: -0.02em; }
::selection { background: #111; color: #fff; }
.screen { min-height: 100svh; display: grid; grid-template-rows: auto 1fr auto; gap: 32px; padding-block: 16px 20px; }
.screen > p { max-width: 34em; }
.mid { align-self: center; display: grid; gap: 20px; }
.pic { width: 120px; aspect-ratio: 4 / 5; background: #EAEAEA; overflow: hidden; }
.pic img { width: 128%; max-width: none; margin: 6% 0 0 -14%; filter: grayscale(1); }
.signup { max-width: 440px; font-weight: 400; letter-spacing: 0; } .field { gap: 0; } .note { font-size: 0.8rem; }
.screen a.u { text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 3px; }
.tag { display: inline-block; margin-right: 0.3em; padding: 0 0.4em; background: #111; color: #fff; font-size: 0.6em; vertical-align: 0.2em; letter-spacing: 0; }
@media (min-width: 820px) { .mid { grid-template-columns: 120px minmax(0, 440px); align-items: end; } }
''', '''
<main class="wrap screen">
	<p data-in><b>Mostafa Saher.</b> I’m an instructor who teaches AI and cloud. I work one clear step at a time, explaining models and cloud services the way I explain them in class.</p>
	<div class="mid" data-in style="--i:1"><div class="pic">{{IMG}}</div>{{FORM}}</div>
	<p data-in style="--i:2"><span class="tag">NOW</span> I write a newsletter with notes from the classroom, where I stand on the hype, and the resources I’d hand a student. Find me on <a class="u" href="https://www.linkedin.com/in/mostafa-abuelnoor-96b2b1171/" target="_blank" rel="noopener">LinkedIn</a>, <a class="u" href="https://github.com/MostafaAbuelnoor" target="_blank" rel="noopener">GitHub</a> or by <a class="u" href="mailto:mostafasaher@gmail.com">email</a>.</p>
</main>
''')
print('batch 3 done')
