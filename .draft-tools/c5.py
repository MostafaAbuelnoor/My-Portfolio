from lib2 import page
import random
MORE = '<section class="wrap more"><div data-reveal>{{TOPICS_UL}}</div><div data-reveal style="--i:1">{{LINKS_ROWS}}</div></section>\n<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>'
MORECSS = '.more { display: grid; gap: 28px 56px; padding-block: 48px 8px; } @media (min-width: 860px) { .more { grid-template-columns: 1fr 1fr; } }'
HERO2 = '.hero { display: grid; gap: 24px 48px; align-items: center; min-height: calc(100svh - 70px); padding-bottom: 36px; } @media (min-width: 900px) { .hero { grid-template-columns: 1.1fr 0.9fr; } }'

# 91 Neon
page(91, 'neon', 'family=Monoton&family=Manrope:wght@400..700', '#0D0A14', '''
:root { color-scheme: dark; --pink: #FF4FD8; --cyan: #3DF5FF; --line: #2A2238; --focus: var(--cyan); --f-bg: #171222; --f-text: #F4F0FA; --f-ph: #9D93B3; --f-border: 1px solid #332A47; --b-bg: var(--cyan); --b-text: #06181A; --note: #9D93B3; --err: #FF9B8F; --f-radius: 10px; --b-radius: 6px; }
body { background: #0D0A14; color: #F4F0FA; font: 16px/1.55 "Manrope", system-ui, sans-serif; }
::selection { background: var(--pink); color: #0D0A14; }
.wall { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto 1fr; background: radial-gradient(60% 45% at 50% 34%, rgb(255 79 216 / 0.22), transparent 70%), radial-gradient(40% 30% at 50% 62%, rgb(61 245 255 / 0.14), transparent 70%); }
.sign { align-self: center; text-align: center; padding-block: 8px 40px; }
h1 { font: 400 clamp(3rem, 1rem + 12vw, 10.5rem)/1 "Monoton", cursive; color: #FFE9FB; text-shadow: 0 0 6px #fff, 0 0 18px var(--pink), 0 0 44px var(--pink), 0 0 90px var(--pink); }
.sub { margin-top: 10px; font-size: clamp(1.1rem, 1rem + 1.2vw, 2rem); font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: #E9FEFF; text-shadow: 0 0 6px #fff, 0 0 18px var(--cyan), 0 0 40px var(--cyan); }
@media (prefers-reduced-motion: no-preference) { h1 { animation: flick 3.2s linear 1 backwards; } .sub { animation: flick 2.4s linear 0.9s 1 backwards; } h1 span { animation: buzz 7s linear 4s infinite; } @keyframes flick { 0%, 9%, 13%, 22%, 26% { opacity: 0.08; text-shadow: none; } 10%, 12%, 23%, 25%, 30%, 100% { opacity: 1; } } @keyframes buzz { 0%, 96%, 98%, 100% { opacity: 1; } 97% { opacity: 0.35; } } }
.sign p.s { max-width: 30em; margin: 26px auto 22px; color: #C9BFDD; }
.signup { max-width: 440px; margin-inline: auto; text-align: left; } .note { text-align: center; }
.under { display: grid; gap: 28px 56px; align-items: end; padding-block: 12px 8px; }
.under figure { width: min(230px, 60%); filter: drop-shadow(0 0 1.5px rgb(255 79 216 / 0.9)) drop-shadow(0 0 24px rgb(255 79 216 / 0.35)); }
@media (min-width: 880px) { .under { grid-template-columns: 230px 1fr 1fr; } .under figure { width: 100%; } }
''', '''
<div class="wall"><div class="wrap">{{TOP}}</div>
	<main class="wrap sign"><h1>Mo<span>s</span>tafa</h1><p class="sub">AI · Cloud · Open late</p><p class="s" data-reveal style="--wait:1800ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:1950ms">{{FORM}}</div></main>
</div>
<section class="wrap under"><figure data-reveal>{{IMG}}</figure><div data-reveal style="--i:1">{{TOPICS_UL}}</div><div data-reveal style="--i:2">{{LINKS_ROWS}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 92 Ticket
page(92, 'ticket', 'family=Barlow+Condensed:wght@500;700&family=Barlow:wght@400;500;600', '#1B2A4A', '''
:root { --line: rgb(27 42 74 / 0.25); --focus: #1B2A4A; --f-bg: #fff; --f-border: 1.5px solid #1B2A4A; --b-bg: #E4572E; --b-text: #fff; --note: #5A5F6E; --f-radius: 8px; --b-radius: 5px; --f-pad: 4px; }
body { background: #1B2A4A; color: #F4EFE4; font: 16px/1.55 "Barlow", system-ui, sans-serif; }
::selection { background: #E4572E; color: #fff; }
''' + HERO2 + '''
h1 { font: 700 clamp(3.2rem, 1.4rem + 7vw, 7.4rem)/0.9 "Barlow Condensed", sans-serif; text-transform: uppercase; }
h1 em { font-style: normal; color: #FFB84D; }
.hero p.s { margin: 16px 0 0; max-width: 30em; color: #C6CEDF; }
.tk { justify-self: center; width: min(100%, 460px); display: grid; grid-template-columns: 1fr 96px; color: #1B2A4A; filter: drop-shadow(0 24px 30px rgb(0 0 0 / 0.45)); }
.main, .stub { background: #F4EFE4; padding: 20px; -webkit-mask: radial-gradient(circle 12px at var(--mx) 0, transparent 98%, #000) top / 100% 51% no-repeat, radial-gradient(circle 12px at var(--mx) 100%, transparent 98%, #000) bottom / 100% 51% no-repeat; mask: radial-gradient(circle 12px at var(--mx) 0, transparent 98%, #000) top / 100% 51% no-repeat, radial-gradient(circle 12px at var(--mx) 100%, transparent 98%, #000) bottom / 100% 51% no-repeat; }
.main { --mx: 100%; border-right: 2px dashed #1B2A4A; border-radius: 14px 0 0 14px; } .stub { --mx: 0%; border-radius: 0 14px 14px 0; display: grid; place-items: center; transform-origin: 0 0; transition: transform 900ms cubic-bezier(0.5, 0, 0.9, 0.4), opacity 500ms ease 500ms; }
.stub b { writing-mode: vertical-rl; font: 700 1.5rem "Barlow Condensed", sans-serif; letter-spacing: 0.12em; text-transform: uppercase; }
.tk.torn .stub { transform: translate(30px, 260px) rotate(38deg); opacity: 0; }
.k { font: 700 0.8rem "Barlow Condensed", sans-serif; letter-spacing: 0.14em; text-transform: uppercase; color: #E4572E; }
.who { display: flex; align-items: center; gap: 12px; margin: 10px 0 14px; } .face { flex: none; width: 64px; height: 64px; border-radius: 10px; background: #DDD4C0; }
.who b { display: block; font: 700 1.8rem/1 "Barlow Condensed", sans-serif; text-transform: uppercase; }
.meta { display: grid; grid-template-columns: repeat(3, auto); gap: 10px; margin-bottom: 14px; font-size: 0.85rem; } .meta b { display: block; font-weight: 600; }
.main .note { color: #5A5F6E; }
@media (max-width: 520px) { .tk { grid-template-columns: 1fr 52px; } .main, .stub { padding: 14px; } .stub b { font-size: 1.1rem; } .tk .btn svg { display: none; } .tk .btn { padding-inline: 12px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split data-fx="flip">Admit one to <em>AI and cloud.</em></h1><p class="s" data-reveal style="--wait:600ms">One clear step at a time. Fill in the ticket and the stub tears off.</p></div>
		<div class="tk" id="tk" data-reveal="scale" style="--wait:300ms" data-tilt="7">
			<div class="main"><span class="k">Admit one · Newsletter</span><div class="who"><div class="face">{{IMG}}</div><div><b>Mostafa Saher</b>Technical instructor</div></div><div class="meta"><p><b>Subject</b>AI, cloud</p><p><b>Seat</b>Front row</p><p><b>Price</b>Free</p></div>{{FORM}}</div>
			<div class="stub"><b>After class</b></div>
		</div>
	</main>
</div>''' + MORE, '''
const tk = document.getElementById('tk'), form = document.querySelector('form.signup');
new MutationObserver(() => { if (form.classList.contains('is-done')) tk.classList.add('torn'); }).observe(form, { attributes: true, attributeFilter: ['class'] });
''')

# 93 Envelope
page(93, 'envelope', 'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Reenie+Beanie', '#E9E1D2', '''
:root { --red: #B6362B; --line: #E1D9C8; --focus: var(--red); --f-bg: #F7F3EA; --f-border: 1px solid #CFC6B2; --b-bg: var(--red); --b-text: #fff; --note: #7A7260; --f-radius: 6px; --b-radius: 3px; --f-pad: 4px; }
body { background: #E9E1D2; color: #2A261E; font: 17px/1.55 "Source Serif 4", Georgia, serif; }
::selection { background: var(--red); color: #fff; }
.scene { display: grid; place-items: center; min-height: calc(100svh - 70px); padding-block: 12px 48px; perspective: 1400px; }
.env { position: relative; width: min(100%, 560px); margin-top: clamp(160px, 34vh, 300px); }
.back { position: relative; aspect-ratio: 16 / 10; background: #C9B89A; border-radius: 6px; box-shadow: 0 30px 50px -24px rgb(0 0 0 / 0.5); }
.flap { position: absolute; left: 0; right: 0; top: 0; height: 56%; background: #BFAD8D; clip-path: polygon(0 0, 100% 0, 50% 100%); transform-origin: 50% 0; z-index: 4; transition: transform 800ms var(--ease-io), z-index 0s 400ms; }
.front { position: absolute; inset: 0; z-index: 3; background: #D6C7AB; clip-path: polygon(0 0, 50% 52%, 100% 0, 100% 100%, 0 100%); border-radius: 6px; }
.front::after { content: "To: you"; position: absolute; left: 50%; bottom: 14%; translate: -50% 0; font: 400 2rem "Reenie Beanie", cursive; color: #5B4E38; }
.letter { position: absolute; z-index: 2; left: 5%; right: 5%; bottom: 6%; padding: clamp(16px, 3vw, 28px); background: #FFFDF8; border-radius: 4px; box-shadow: 0 10px 24px -14px rgb(0 0 0 / 0.5); transition: transform 1100ms var(--ease-out) 700ms; font-size: 0.98rem; }
.fx:not(.fx-rm) .env:not(.open) .letter { transform: translateY(18%) scale(0.96); }
.env.open .letter, html:not(.fx) .letter, .fx-rm .letter { transform: translateY(calc(-1 * clamp(150px, 32vh, 290px))); z-index: 5; }
.env.open .flap, html:not(.fx) .flap, .fx-rm .flap { transform: rotateX(180deg); z-index: 1; }
.letter h1 { font-size: clamp(1.4rem, 1.1rem + 1.4vw, 2rem); font-weight: 600; line-height: 1.15; letter-spacing: -0.02em; margin-bottom: 8px; }
.letter .sig { font: 400 2.2rem/1 "Reenie Beanie", cursive; margin: 6px 0 10px; }
.letter .signup { font-family: system-ui, sans-serif; }
.letter .face { float: right; width: 62px; height: 62px; margin-left: 12px; border-radius: 50%; background: #E9E1D2; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="scene"><div class="env" id="env" data-inview>
		<div class="back"></div>
		<div class="letter"><div class="face">{{IMG}}</div><h1>{{H}}</h1><p>The best part of every class comes once it’s over. I write that part down and post it to you.</p><p class="sig">Mostafa</p>{{FORM}}</div>
		<div class="front"></div><div class="flap"></div>
	</div></main>
</div>''' + MORE, '''
const env = document.getElementById('env'); if (FX.RM) { env.classList.add('open'); return; } env.addEventListener('fx:in', () => setTimeout(() => env.classList.add('open'), 500));
''')

# 94 Cube
page(94, 'cube', 'family=Unbounded:wght@500;800&family=Hanken+Grotesk:wght@400..600', '#101014', '''
:root { color-scheme: dark; --line: #2A2A33; --focus: #C8FF5A; --f-bg: #1A1A21; --f-text: #F4F4F7; --f-ph: #9B9BA8; --f-border: 1px solid #2E2E39; --b-bg: #C8FF5A; --b-text: #101014; --note: #9B9BA8; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #101014; color: #F4F4F7; font: 16px/1.55 "Hanken Grotesk", system-ui, sans-serif; }
::selection { background: #C8FF5A; color: #101014; }
''' + HERO2 + '''
h1 { font: 800 clamp(2rem, 1.1rem + 3.4vw, 3.8rem)/1 "Unbounded", sans-serif; letter-spacing: -0.04em; text-transform: uppercase; }
.hero p.s { margin: 18px 0 22px; max-width: 30em; color: #B9B9C6; }
.signup { max-width: 440px; }
.space { --s: min(250px, 58vw); display: grid; place-items: center; height: calc(var(--s) * 1.9); perspective: 1100px; cursor: grab; touch-action: none; user-select: none; }
.cube { position: relative; width: var(--s); height: var(--s); transform-style: preserve-3d; transform: rotateX(var(--rx, -18deg)) rotateY(var(--ry, 32deg)); }
.f { position: absolute; inset: 0; display: grid; place-items: center; overflow: hidden; font: 800 clamp(1.4rem, 5vw, 2.4rem) "Unbounded", sans-serif; text-transform: uppercase; letter-spacing: -0.04em; backface-visibility: hidden; }
.f1 { background: #C8FF5A; color: #101014; transform: translateZ(calc(var(--s) / 2)); align-items: end; } .f1 img { width: 104%; max-width: none; }
.f2 { background: #5B8CFF; transform: rotateY(90deg) translateZ(calc(var(--s) / 2)); } .f3 { background: #FF5A7A; transform: rotateY(180deg) translateZ(calc(var(--s) / 2)); } .f4 { background: #FFB02E; color: #101014; transform: rotateY(-90deg) translateZ(calc(var(--s) / 2)); }
.f5 { background: #F4F4F7; color: #101014; transform: rotateX(90deg) translateZ(calc(var(--s) / 2)); } .f6 { background: #2A2A33; transform: rotateX(-90deg) translateZ(calc(var(--s) / 2)); }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split data-fx="flip">Every side of AI and cloud.</h1><p class="s" data-reveal style="--wait:600ms">I’m Mostafa Saher. I teach one clear step at a time. Drag the cube to turn it.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
		<div class="space" id="space" data-reveal="scale" style="--wait:300ms"><div class="cube" id="cube"><div class="f f1">{{IMG}}</div><div class="f f2">AI</div><div class="f f3">Cloud</div><div class="f f4">Notes</div><div class="f f5">Takes</div><div class="f f6">Links</div></div></div>
	</main>
</div>''' + MORE, '''
const cube = document.getElementById('cube'), sp = document.getElementById('space'); let rx = -18, ry = 32, vx = 0, vy = 0.25, drag = false, lx = 0, ly = 0;
sp.addEventListener('pointerdown', (e) => { drag = true; lx = e.clientX; ly = e.clientY; sp.setPointerCapture(e.pointerId); sp.style.cursor = 'grabbing'; });
sp.addEventListener('pointermove', (e) => { if (!drag) return; vy = (e.clientX - lx) * 0.4; vx = -(e.clientY - ly) * 0.4; lx = e.clientX; ly = e.clientY; });
const end = () => { drag = false; sp.style.cursor = 'grab'; }; sp.addEventListener('pointerup', end); sp.addEventListener('pointercancel', end);
FX.onTick(() => { ry += vy; rx = FX.clamp(rx + vx, -70, 70); if (!drag) { vx *= 0.94; vy = FX.lerp(vy, 0.25, 0.03); } cube.style.setProperty('--rx', rx.toFixed(2) + 'deg'); cube.style.setProperty('--ry', ry.toFixed(2) + 'deg'); });
''')

# 95 Clouds
page(95, 'clouds', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800', '#5AA9F2', '''
:root { --navy: #0E2A52; --line: rgb(14 42 82 / 0.2); --focus: var(--navy); --f-bg: #fff; --b-bg: var(--navy); --b-text: #fff; --note: #5A6B85; --f-radius: 999px; --b-radius: 999px; }
body { background: #F4F8FD; color: var(--navy); font: 16px/1.55 "Bricolage Grotesque", system-ui, sans-serif; }
::selection { background: var(--navy); color: #fff; }
.sky { position: relative; min-height: 100svh; display: grid; grid-template-rows: auto auto 1fr; overflow: hidden; background: linear-gradient(#3F8FE8, #8FC6F7 60%, #DCEEFC); text-align: center; }
.cl { position: absolute; left: 0; width: 46vmin; height: 15vmin; border-radius: 999px; background: #fff; filter: blur(2px); opacity: var(--o, 0.95); top: var(--t); }
.cl::before, .cl::after { content: ""; position: absolute; border-radius: 50%; background: #fff; } .cl::before { width: 42%; height: 150%; left: 14%; top: -72%; } .cl::after { width: 34%; height: 120%; right: 16%; top: -50%; }
@media (prefers-reduced-motion: no-preference) { .cl { animation: fly var(--d) linear infinite; animation-delay: var(--dl); } @keyframes fly { from { transform: translateX(-60vmin) scale(var(--sc, 1)); } to { transform: translateX(110vw) scale(var(--sc, 1)); } } }
@media (prefers-reduced-motion: reduce) { .cl { left: var(--x); } }
.sky > .wrap { position: relative; z-index: 3; }
h1 { margin-top: clamp(8px, 4vh, 44px); font-size: clamp(2.6rem, 1.2rem + 6.4vw, 6.6rem); font-weight: 800; line-height: 0.92; letter-spacing: -0.05em; color: var(--navy); }
.ask { max-width: 440px; margin: 22px auto 0; text-align: left; } .ask .note { text-align: center; color: var(--navy); } .field { box-shadow: 0 14px 34px -16px rgb(14 42 82 / 0.6); }
.sky figure { position: relative; z-index: 2; align-self: end; justify-self: center; width: min(320px, 70%); margin-top: 20px; }
''' + MORECSS, '''
<div class="sky">
	<i class="cl" style="--t:14%;--d:46s;--dl:-8s;--sc:1.1;--x:8%"></i><i class="cl" style="--t:34%;--d:64s;--dl:-40s;--sc:0.7;--o:0.8;--x:62%"></i><i class="cl" style="--t:52%;--d:38s;--dl:-20s;--sc:1.4;--x:30%"></i><i class="cl" style="--t:70%;--d:72s;--dl:-55s;--sc:0.9;--o:0.85;--x:74%"></i><i class="cl" style="--t:24%;--d:54s;--dl:-30s;--sc:0.55;--o:0.7;--x:44%"></i>
	<div class="wrap">{{TOP}}</div>
	<div class="wrap"><h1 data-split data-fx="pop">Head in the cloud. Feet in the classroom.</h1><div class="ask" data-reveal style="--wait:700ms">{{FORM}}</div></div>
	<figure data-reveal style="--wait:400ms" data-par="-12">{{IMG}}</figure>
</div>
<section class="wrap more"><div data-reveal><p style="margin-bottom:18px">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time. {{INTRO}}</p>{{LINKS_INLINE}}</div><div data-reveal style="--i:1">{{TOPICS_UL}}</div></section>
<div class="wrap"><footer class="foot">{{FOOT}}</footer></div>
''')

# 96 Mosaic
random.seed(11)
tiles = ''.join(f'<i style="--c:{c};--r:{r};--tx:{random.randint(-160,160)}%;--ty:{random.randint(-160,160)}%;--rt:{random.randint(-90,90)}deg;--d:{random.randint(0,700)}ms"></i>' for r in range(6) for c in range(5))
page(96, 'mosaic', 'family=Figtree:wght@400..800', '#F1EEE6', '''
:root { --line: #D9D4C6; --focus: #17171A; --f-bg: #fff; --b-bg: #17171A; --b-text: #fff; --note: #6A675C; --f-radius: 12px; --b-radius: 8px; }
body { background: #F1EEE6; color: #17171A; font: 16px/1.55 "Figtree", system-ui, sans-serif; }
::selection { background: #17171A; color: #F1EEE6; }
''' + HERO2 + '''
h1 { font-size: clamp(2.3rem, 1.2rem + 4vw, 4.6rem); font-weight: 800; line-height: 0.98; letter-spacing: -0.045em; max-width: 10em; }
.hero p.s { margin: 16px 0 22px; max-width: 30em; color: #55524A; }
.signup { max-width: 440px; }
.mo { justify-self: center; width: min(380px, 84vw); aspect-ratio: 5 / 6; display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: repeat(6, 1fr); gap: 3px; }
.mo i { background-color: #9DB8F5; background-image: url(../assets/mostafa-cutout.webp); background-repeat: no-repeat; background-size: 520% auto; background-position: calc(var(--c) * 25%) calc(var(--r) * 21%); border-radius: 4px; transition: transform 1100ms var(--ease-out), opacity 700ms ease, border-radius 300ms ease; transition-delay: var(--d); }
.fx:not(.fx-rm) .mo:not(.in) i { transform: translate(var(--tx), var(--ty)) rotate(var(--rt)) scale(0.4); opacity: 0; }
@media (hover: hover) and (pointer: fine) { .mo.in i { transition-delay: 0ms; transition-duration: 400ms; } .mo.in i:hover { transform: scale(0.82) rotate(6deg); border-radius: 50%; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split>The pieces fall into place.</h1><p class="s" data-reveal style="--wait:600ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:750ms">{{FORM}}</div></div>
		<div class="mo" data-inview role="img" aria-label="Mostafa Saher">''' + tiles + '''</div>
	</main>
</div>''' + MORE)

# 97 Badge
page(97, 'badge-spin', 'family=Archivo:wght@500..800', '#E9FF70', '''
:root { --line: rgb(0 0 0 / 0.2); --focus: #151515; --f-bg: #fff; --b-bg: #151515; --b-text: #fff; --note: #4A5200; --f-radius: 999px; --b-radius: 999px; }
body { background: #E9FF70; color: #151515; font: 16px/1.5 "Archivo", system-ui, sans-serif; }
::selection { background: #151515; color: #E9FF70; }
''' + HERO2 + '''
h1 { font-size: clamp(2.6rem, 1.2rem + 5.4vw, 6rem); font-weight: 800; line-height: 0.9; letter-spacing: -0.05em; max-width: 9em; }
.hero p.s { margin: 16px 0 22px; max-width: 28em; font-size: 1.1rem; font-weight: 500; }
.signup { max-width: 440px; }
.bg { position: relative; justify-self: center; width: min(400px, 86vw); aspect-ratio: 1; }
.bg svg { position: absolute; inset: 0; width: 100%; height: 100%; --dur: 22s; }
.bg text { font: 700 15.4px "Archivo", sans-serif; letter-spacing: 0.24em; text-transform: uppercase; fill: #151515; }
.bg .core { position: absolute; inset: 15%; border-radius: 50%; background: #151515; overflow: hidden; } .bg .core img { width: 128%; max-width: none; margin: 8% 0 0 -14%; }
.bg:hover svg { animation-duration: 6s; }
.star { position: absolute; right: 2%; top: 4%; width: 74px; aspect-ratio: 1; background: #FF5A36; clip-path: polygon(50% 0, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); --dur: 9s; }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main class="hero">
		<div><h1 data-split data-fx="drop">Certified clear.</h1><p class="s" data-reveal style="--wait:500ms">I’m Mostafa Saher. I teach AI and cloud, one clear step at a time, and I write down what comes up after class.</p><div data-reveal style="--wait:650ms">{{FORM}}</div></div>
		<div class="bg" data-reveal="scale" style="--wait:300ms">
			<svg class="fx-spin" viewBox="0 0 400 400" aria-hidden="true"><defs><path id="ring" d="M200,200 m-176,0 a176,176 0 1,1 352,0 a176,176 0 1,1 -352,0"/></defs><text><textPath href="#ring">Technical instructor · AI and cloud · One clear step at a time · Mostafa Saher · </textPath></text></svg>
			<div class="core">{{IMG}}</div><i class="star fx-spin"></i>
		</div>
	</main>
</div>''' + MORE)

# 98 Hype vs clear
page(98, 'hype-vs-clear', 'family=Inter+Tight:wght@400..800&family=Geist+Mono:wght@400', '#0E0E10', '''
:root { --line: #D9D9D4; --focus: #111; --f-bg: #fff; --b-bg: #111; --b-text: #fff; --note: #666; --f-radius: 999px; --b-radius: 999px; }
body { background: #F4F4F0; color: #111; font: 16px/1.55 "Inter Tight", system-ui, sans-serif; }
::selection { background: #111; color: #F4F4F0; }
.cmp { position: relative; height: min(78svh, 640px); margin-top: 6px; border-radius: 22px; overflow: hidden; touch-action: pan-y; user-select: none; --x: 50%; }
.side { position: absolute; inset: 0; display: grid; align-content: center; padding: clamp(22px, 6vw, 90px); }
.hype { background: #0E0E10; color: #7CFFB2; font: 400 clamp(0.8rem, 0.7rem + 0.5vw, 1.05rem)/1.5 "Geist Mono", monospace; overflow: hidden; }
.hype p { opacity: 0.85; } .hype b { color: #FF5A7A; font-weight: 400; }
.hype::before { content: "THE HYPE"; position: absolute; left: clamp(22px, 6vw, 90px); top: 22px; font-size: 0.75rem; letter-spacing: 0.14em; color: #fff; }
.clear { background: #fff; clip-path: inset(0 0 0 var(--x)); }
.clear::before { content: "THE CLASS"; position: absolute; right: clamp(22px, 6vw, 90px); top: 22px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; }
.clear h1 { margin-left: auto; max-width: 8em; text-align: right; font-size: clamp(2.2rem, 1.2rem + 5vw, 5.6rem); font-weight: 800; line-height: 0.92; letter-spacing: -0.05em; }
.clear figure { position: absolute; left: 4%; bottom: 0; height: 70%; aspect-ratio: 1100 / 1433; } .clear img { height: 100%; width: auto; max-width: none; }
.bar { position: absolute; top: 0; bottom: 0; left: var(--x); width: 3px; margin-left: -1.5px; background: #FFD23F; cursor: ew-resize; }
.bar::after { content: "↔"; position: absolute; left: 50%; top: 50%; width: 46px; height: 46px; margin: -23px; display: grid; place-items: center; border-radius: 50%; background: #FFD23F; color: #111; font-weight: 800; box-shadow: 0 8px 20px -8px #000; }
.under { display: grid; gap: 22px 56px; align-items: end; padding-block: 32px 0; }
.under p { font-size: 1.15rem; font-weight: 500; max-width: 28em; }
@media (min-width: 860px) { .under { grid-template-columns: 1fr 440px; } }
@media (max-width: 700px) { .clear { align-content: start; padding-top: 64px; } .clear figure { height: 52%; left: auto; right: -4%; } .hype { align-content: start; padding-top: 64px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<div class="cmp" id="cmp">
			<div class="side hype" aria-hidden="true"><p>REVOLUTIONARY <b>10X</b> PARADIGM SHIFT. AGENTIC MULTI-CLOUD SYNERGY AT HYPERSCALE. <b>GAME-CHANGING</b> FOUNDATION MODEL DISRUPTS EVERYTHING. SERVERLESS-NATIVE VECTOR-FIRST ZERO-SHOT <b>BREAKTHROUGH</b>. NEXT-GEN AUTONOMOUS ORCHESTRATION LAYER. THIS CHANGES EVERYTHING (AGAIN). <b>UNPRECEDENTED</b> BENCHMARK. ENTERPRISE-GRADE AI-POWERED CLOUD-SCALE TRANSFORMATION. THE FUTURE IS HERE. <b>10X</b> PARADIGM SHIFT. AGENTIC MULTI-CLOUD SYNERGY AT HYPERSCALE.</p></div>
			<div class="side clear"><h1>AI and cloud, one clear step at a time.</h1><figure>{{IMG}}</figure></div>
			<div class="bar" id="bar" role="slider" tabindex="0" aria-label="Drag to compare the hype with the class" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"></div>
		</div>
		<section class="under"><p data-reveal>I’m Mostafa Saher, a technical instructor. Drag the handle: the hype on one side, how I teach it on the other.</p><div data-reveal style="--i:1">{{FORM}}</div></section>
	</main>
</div>''' + MORE, '''
const cmp = document.getElementById('cmp'), bar = document.getElementById('bar'); let v = 50;
const set = (n) => { v = FX.clamp(n, 4, 96); cmp.style.setProperty('--x', v + '%'); bar.setAttribute('aria-valuenow', Math.round(v)); };
let drag = false; const at = (e) => { const r = cmp.getBoundingClientRect(); set((e.clientX - r.left) / r.width * 100); };
cmp.addEventListener('pointerdown', (e) => { drag = true; cmp.setPointerCapture(e.pointerId); at(e); }); cmp.addEventListener('pointermove', (e) => { if (drag) at(e); });
['pointerup', 'pointercancel'].forEach((n) => cmp.addEventListener(n, () => { drag = false; }));
bar.addEventListener('keydown', (e) => { if (e.key === 'ArrowLeft') set(v - 4); if (e.key === 'ArrowRight') set(v + 4); });
if (!FX.RM) { set(92); const t0 = performance.now(); const run = (t) => { if (drag) return; const k = Math.min(1, (t - t0 - 500) / 1600); if (k > 0) set(92 - (1 - Math.pow(1 - k, 3)) * 58); if (k < 1) requestAnimationFrame(run); }; requestAnimationFrame(run); } else set(34);
''')

# 99 Reels
def reel(final, decoys, k):
    return f'<span class="reel" style="--k:{k}"><span class="strip">' + ''.join(f'<i>{d}</i>' for d in decoys) + f'<i class="fin">{final}</i></span></span>'
reels = ' '.join([reel('I teach', ['I hype', 'I sell', 'I guess'], 0), reel('AI and cloud,', ['buzzwords,', 'jargon,', 'magic,'], 1), reel('one clear step', ['ten wild leaps', 'a big blur', 'a firehose'], 2), reel('at a time.', ['all at once.', 'someday.', 'maybe.'], 3)])
page(99, 'reels', 'family=Gabarito:wght@400..900', '#17171C', '''
:root { color-scheme: dark; --line: #2B2B34; --focus: #FFD23F; --f-bg: #22222A; --f-text: #F5F5F8; --f-ph: #9C9CAA; --f-border: 1px solid #33333F; --b-bg: #FFD23F; --b-text: #17171C; --note: #9C9CAA; --err: #FF9B8F; --f-radius: 12px; --b-radius: 8px; }
body { background: #17171C; color: #F5F5F8; font: 16px/1.55 "Gabarito", system-ui, sans-serif; }
::selection { background: #FFD23F; color: #17171C; }
h1 { margin-top: clamp(16px, 6vh, 64px); display: grid; gap: 0.06em; font-size: clamp(2.5rem, 1.2rem + 7.4vw, 8rem); font-weight: 900; line-height: 1.02; letter-spacing: -0.05em; }
.reel { display: block; height: 1.04em; overflow: hidden; border-radius: 0.12em; }
.strip { display: block; } .strip i { display: block; height: 1.04em; font-style: normal; color: #5A5A68; white-space: nowrap; } .strip .fin { color: #F5F5F8; } .reel:nth-child(2) .fin { color: #FFD23F; }
.fx:not(.fx-rm) .strip { animation: spinr 1500ms cubic-bezier(0.2, 0.9, 0.2, 1.04) backwards; animation-delay: calc(300ms + var(--k) * 320ms); }
.strip { transform: translateY(-75%); }
@keyframes spinr { from { transform: translateY(0); filter: blur(3px); } 70% { filter: blur(0); } }
.row2 { display: grid; gap: 22px 48px; align-items: end; padding-block: 36px 0; }
.me { display: flex; gap: 14px; align-items: center; max-width: 30em; font-size: 1.1rem; } .face { flex: none; width: 76px; height: 76px; border-radius: 18px; background: #2B2B34; }
@media (min-width: 860px) { .row2 { grid-template-columns: 1fr 440px; } }
''' + MORECSS, '''
<div class="wrap">{{TOP}}
	<main>
		<h1 aria-label="I teach AI and cloud, one clear step at a time.">''' + reels + '''</h1>
		<div class="row2"><div class="me" data-reveal style="--wait:1900ms"><div class="face">{{IMG}}</div><p>I’m Mostafa Saher, a technical instructor. My newsletter carries what comes up after class.</p></div><div data-reveal style="--wait:2050ms">{{FORM}}</div></div>
	</main>
</div>''' + MORE)

# 100 Quiet craft
page(100, 'quiet-craft', 'family=Geist:wght@400..600&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400', '#FAFAF8', '''
:root { --line: #E6E5DF; --focus: #171715; --f-bg: #fff; --f-border: 1px solid #DEDDD6; --b-bg: #171715; --b-text: #FAFAF8; --note: #74736B; --f-radius: 14px; --b-radius: 10px; --w: 1040px; }
body { background: #FAFAF8; color: #171715; font: 16px/1.6 "Geist", system-ui, sans-serif; }
::selection { background: #171715; color: #FAFAF8; }
.top a { position: relative; } .top a::after { content: ""; position: absolute; left: 0; right: 0; bottom: -3px; height: 1px; background: currentColor; transform: scaleX(0); transform-origin: 100% 50%; transition: transform 350ms var(--ease-out); }
''' + HERO2 + '''
h1 { font: 400 clamp(2.5rem, 1.3rem + 4.4vw, 5rem)/1.02 "Newsreader", serif; letter-spacing: -0.03em; max-width: 10em; --stag: 70ms; --dur: 1200ms; }
h1 em { color: #8A6B3F; }
.hero p.s { margin: 20px 0 24px; max-width: 30em; color: #5E5D56; }
.signup { max-width: 440px; }
.field { transition: box-shadow 300ms var(--ease-out), opacity 160ms ease, filter 160ms ease, transform 300ms var(--ease-out); } .field:focus-within { transform: translateY(-1px); box-shadow: 0 0 0 2px #171715, 0 18px 30px -18px rgb(0 0 0 / 0.35); }
.pic { justify-self: center; width: min(360px, 78%); aspect-ratio: 4 / 5; border-radius: 22px; background: #ECE9E0; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; }
.pic img { width: 108%; max-width: none; transition: scale 900ms var(--ease-out); }
.acc { border-top: 1px solid var(--line); }
.acc details { border-bottom: 1px solid var(--line); }
.acc summary { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-block: 18px; cursor: pointer; list-style: none; font: 400 clamp(1.4rem, 1.1rem + 1.2vw, 2rem)/1.1 "Newsreader", serif; } .acc summary::-webkit-details-marker { display: none; }
.acc summary i { position: relative; flex: none; width: 18px; height: 18px; } .acc summary i::before, .acc summary i::after { content: ""; position: absolute; left: 0; right: 0; top: 50%; height: 1.5px; background: currentColor; transition: rotate 400ms var(--ease-out); } .acc summary i::after { rotate: 90deg; } .acc details[open] summary i::after { rotate: 0deg; }
.acc .body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 450ms var(--ease-out); } .acc details[open] .body { grid-template-rows: 1fr; } .acc .body p { overflow: hidden; color: #5E5D56; max-width: 34em; } .acc details[open] .body p { padding-bottom: 18px; }
.two { display: grid; gap: 28px 64px; padding-block: 56px 8px; }
.li-rows a { transition: padding 350ms var(--ease-out); }
@media (hover: hover) and (pointer: fine) { .top a:hover::after { transform: scaleX(1); transform-origin: 0 50%; } .pic:hover img { scale: 1.04; } .li-rows a:hover { padding-left: 10px; } }
@media (min-width: 860px) { .two { grid-template-columns: 1.2fr 0.8fr; } }
''', '''
<div class="wrap">{{TOP}}
	<main>
		<section class="hero">
			<div><h1 data-split data-fx="blur">I teach AI and cloud, <em>one clear step</em> at a time.</h1><p class="s" data-reveal="fade" style="--wait:700ms">I’m Mostafa Saher, a technical instructor. My newsletter carries what comes up after class.</p><div data-reveal="fade" style="--wait:850ms" data-mag="0.04">{{FORM}}</div></div>
			<div class="pic" data-wipe style="--wait:300ms"><span data-par="-10">{{IMG}}</span></div>
		</section>
		<section class="two">
			<div class="acc" data-reveal>
				<details open name="t"><summary>Thoughts<i></i></summary><div class="body"><p>Notes from the classroom: what students get stuck on, and the explanation that finally made it click.</p></div></details>
				<details name="t"><summary>Opinions<i></i></summary><div class="body"><p>Where I stand on new models, cloud services and the hype around them.</p></div></details>
				<details name="t"><summary>Resources<i></i></summary><div class="body"><p>The labs, docs, courses and tools I actually use, each with a line on why.</p></div></details>
			</div>
			<div data-reveal style="--i:1">{{LINKS_ROWS}}</div>
		</section>
	</main>
	<footer class="foot">{{FOOT}}</footer>
</div>
''')
print('c5 done')
