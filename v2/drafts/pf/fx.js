(() => {
	'use strict';
	const root = document.documentElement;
	const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
	const FINE = matchMedia('(hover: hover) and (pointer: fine)').matches;
	const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
	const lerp = (a, b, t) => a + (b - a) * t;
	const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
	const rnd = (a, b) => a + Math.random() * (b - a);
	root.classList.add('fx');
	if (RM) root.classList.add('fx-rm');

	const ticks = new Set();
	let raf = 0;
	const loop = (t) => { ticks.forEach((f) => f(t)); raf = requestAnimationFrame(loop); };
	const onTick = (f) => { if (RM) return; ticks.add(f); if (!raf) raf = requestAnimationFrame(loop); };
	const ptr = { x: innerWidth / 2, y: innerHeight / 2, nx: 0, ny: 0, moved: false };
	addEventListener('pointermove', (e) => { ptr.x = e.clientX; ptr.y = e.clientY; ptr.nx = e.clientX / innerWidth - 0.5; ptr.ny = e.clientY / innerHeight - 0.5; ptr.moved = true; }, { passive: true });
	window.FX = { RM, FINE, onTick, ptr, lerp, clamp, rnd, $$ };

	/* Split text into words or characters */
	$$('[data-split]').forEach((el) => {
		const mode = el.dataset.split || 'words';
		el.setAttribute('aria-label', el.textContent.replace(/\s+/g, ' ').trim());
		let n = 0;
		const walk = (node) => Array.from(node.childNodes).forEach((c) => {
			if (c.nodeType === 3) {
				const frag = document.createDocumentFragment();
				c.textContent.split(/(\s+)/).forEach((tok) => {
					if (!tok) return;
					if (/^\s+$/.test(tok)) { frag.append(' '); return; }
					const w = document.createElement('span');
					w.className = 'w'; w.setAttribute('aria-hidden', 'true');
					(mode === 'chars' ? Array.from(tok) : [tok]).forEach((part) => {
						const s = document.createElement('span');
						s.className = 'c'; s.style.setProperty('--n', n++); s.textContent = part; w.append(s);
					});
					frag.append(w);
				});
				c.replaceWith(frag);
			} else if (c.nodeType === 1 && c.tagName !== 'BR' && !c.hasAttribute('data-keep')) walk(c);
		});
		walk(el);
	});

	/* In-view trigger */
	const watched = $$('[data-split],[data-reveal],[data-wipe],[data-draw],[data-scramble],[data-inview]');
	const enter = (el) => { el.classList.add('in'); el.dispatchEvent(new CustomEvent('fx:in')); };
	if (RM || !('IntersectionObserver' in window)) watched.forEach((el) => el.classList.add('in'));
	else {
		/* A clipped or masked element reports no intersection, so wipes are watched through their parent. */
		const groups = new Map();
		watched.forEach((el) => { const target = el.hasAttribute('data-wipe') ? el.parentElement : el; if (!groups.has(target)) groups.set(target, []); groups.get(target).push(el); });
		const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { io.unobserve(e.target); groups.get(e.target).forEach(enter); } }), { threshold: 0.08 });
		requestAnimationFrame(() => requestAnimationFrame(() => groups.forEach((_, target) => io.observe(target))));
	}

	/* Scramble */
	$$('[data-scramble]').forEach((el) => {
		const final = el.textContent, pool = 'ABCDEFGHJKLMNPQRSTUVWXYZ0123456789#/<>*';
		if (RM) return;
		el.addEventListener('fx:in', () => {
			let f = 0; const total = final.length * 2 + 12;
			const id = setInterval(() => {
				f++;
				el.textContent = Array.from(final).map((ch, i) => (ch === ' ' || i < (f - 8) / 2) ? ch : pool[Math.random() * pool.length | 0]).join('');
				if (f >= total) { el.textContent = final; clearInterval(id); }
			}, 30);
		});
	});

	/* Typewriter */
	$$('[data-type]').forEach((el) => {
		const words = el.dataset.type.split('|'), once = el.hasAttribute('data-once');
		el.setAttribute('aria-label', words.join(', '));
		if (RM) { el.textContent = words[0]; return; }
		let w = 0, i = 0, del = false;
		el.textContent = ''; el.classList.add('fx-caret');
		const step = () => {
			const word = words[w];
			i += del ? -1 : 1; el.textContent = word.slice(0, i);
			let d = del ? 32 : 62;
			if (!del && i === word.length) { if (once) return; del = true; d = 1500; }
			else if (del && i === 0) { del = false; w = (w + 1) % words.length; d = 280; }
			setTimeout(step, d);
		};
		setTimeout(step, +el.dataset.delay || 500);
	});

	/* Rotating words */
	$$('[data-words]').forEach((el) => {
		const words = el.dataset.words.split('|');
		el.setAttribute('aria-label', words.join(', '));
		el.textContent = '';
		const inner = document.createElement('span');
		inner.className = 'fx-word'; inner.setAttribute('aria-hidden', 'true'); inner.textContent = words[0]; el.append(inner);
		if (RM) return;
		let k = 0;
		setInterval(() => {
			k = (k + 1) % words.length; inner.classList.add('out');
			setTimeout(() => { inner.textContent = words[k]; inner.classList.remove('out'); inner.classList.add('pre'); requestAnimationFrame(() => requestAnimationFrame(() => inner.classList.remove('pre'))); }, 300);
		}, +el.dataset.every || 2200);
	});

	/* Marquee */
	$$('[data-marquee]').forEach((el) => {
		const seg = document.createElement('span'); seg.className = 'fx-seg';
		while (el.firstChild) seg.append(el.firstChild);
		const track = document.createElement('span'); track.className = 'fx-track'; track.append(seg);
		for (let i = 0; i < 3; i++) { const c = seg.cloneNode(true); c.setAttribute('aria-hidden', 'true'); track.append(c); }
		el.append(track);
	});

	/* Pointer tilt */
	$$('[data-tilt]').forEach((el) => {
		if (RM) return;
		if (!FINE) { el.classList.add('fx-sway'); return; }
		const max = +el.dataset.tilt || 10; let tx = 0, ty = 0, cx = 0, cy = 0;
		const host = el.closest('[data-tilt-area]') || el;
		host.addEventListener('pointermove', (e) => { const r = el.getBoundingClientRect(); tx = clamp((e.clientX - r.left) / r.width, -0.5, 1.5) - 0.5; ty = clamp((e.clientY - r.top) / r.height, -0.5, 1.5) - 0.5; el.style.setProperty('--gx', (tx + 0.5) * 100 + '%'); el.style.setProperty('--gy', (ty + 0.5) * 100 + '%'); });
		host.addEventListener('pointerleave', () => { tx = ty = 0; });
		onTick(() => { cx = lerp(cx, tx, 0.1); cy = lerp(cy, ty, 0.1); el.style.transform = `perspective(1000px) rotateY(${(cx * max).toFixed(2)}deg) rotateX(${(-cy * max).toFixed(2)}deg)`; });
	});

	/* Pointer parallax and scroll parallax (use the independent translate property) */
	const pars = $$('[data-par]').map((el) => ({ el, a: +el.dataset.par || 20, x: 0, y: 0 }));
	if (pars.length && FINE) onTick(() => pars.forEach((p) => { p.x = lerp(p.x, ptr.nx * p.a, 0.08); p.y = lerp(p.y, ptr.ny * p.a, 0.08); p.el.style.translate = `${p.x.toFixed(1)}px ${p.y.toFixed(1)}px`; }));
	const spars = $$('[data-spar]'), progs = $$('[data-progress]');
	let dirty = true;
	const mark = () => { dirty = true; };
	addEventListener('scroll', mark, { passive: true }); addEventListener('resize', mark);
	const scrollWork = () => {
		if (!dirty) return; dirty = false;
		const vh = innerHeight, max = Math.max(1, root.scrollHeight - vh);
		root.style.setProperty('--sy', (scrollY / max).toFixed(4));
		spars.forEach((el) => { const r = el.parentElement.getBoundingClientRect(); el.style.translate = `0 ${((r.top + r.height / 2 - vh / 2) * (+el.dataset.spar || 0.15)).toFixed(1)}px`; });
		progs.forEach((el) => { const r = el.getBoundingClientRect(); const mode = el.dataset.progress; const p = mode === 'pin' ? clamp(-r.top / Math.max(1, r.height - vh)) : clamp((vh - r.top) / (vh + r.height)); el.style.setProperty('--p', p.toFixed(4)); });
	};
	if (RM) { root.style.setProperty('--sy', 0); progs.forEach((el) => el.style.setProperty('--p', 1)); } else if (spars.length || progs.length || root.hasAttribute('data-sy')) onTick(scrollWork);

	/* Magnetic controls */
	$$('[data-mag]').forEach((el) => {
		if (!FINE || RM) return;
		let tx = 0, ty = 0, cx = 0, cy = 0; const pull = +el.dataset.mag || 0.35;
		onTick(() => {
			const r = el.getBoundingClientRect(), mx = r.left + r.width / 2 - cx, my = r.top + r.height / 2 - cy;
			const dx = ptr.x - mx, dy = ptr.y - my, near = ptr.moved && Math.hypot(dx, dy) < Math.max(r.width, r.height) * 0.9 + 40;
			tx = near ? dx * pull : 0; ty = near ? dy * pull : 0;
			cx = lerp(cx, tx, 0.15); cy = lerp(cy, ty, 0.15);
			el.style.translate = `${cx.toFixed(1)}px ${cy.toFixed(1)}px`;
		});
	});

	/* Spotlight variables */
	$$('[data-spot]').forEach((el) => {
		el.addEventListener('pointermove', (e) => { const r = el.getBoundingClientRect(); el.style.setProperty('--mx', (e.clientX - r.left) + 'px'); el.style.setProperty('--my', (e.clientY - r.top) + 'px'); }, { passive: true });
	});

	/* Cursor blob */
	if (document.body.hasAttribute('data-cursor') && FINE && !RM) {
		const c = document.createElement('div'); c.className = 'fx-cursor'; document.body.append(c);
		let x = ptr.x, y = ptr.y;
		addEventListener('pointermove', (e) => { c.classList.add('on'); c.classList.toggle('big', !!e.target.closest('a,button,input,[data-big]')); }, { passive: true });
		onTick(() => { x = lerp(x, ptr.x, 0.2); y = lerp(y, ptr.y, 0.2); c.style.transform = `translate(${x.toFixed(1)}px, ${y.toFixed(1)}px)`; });
	}

	/* Canvas backgrounds */
	$$('canvas[data-canvas]').forEach((cv) => {
		const ctx = cv.getContext('2d'), type = cv.dataset.canvas;
		const cols = (cv.dataset.colors || '').split(',').filter(Boolean);
		let w = 0, h = 0, items = [], vis = true, color = '#fff';
		const init = () => {
			const dpr = Math.min(devicePixelRatio || 1, 2), r = cv.getBoundingClientRect();
			w = Math.max(1, r.width); h = Math.max(1, r.height); cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
			color = getComputedStyle(cv).color;
			const area = w * h;
			if (type === 'net') items = Array.from({ length: Math.min(110, Math.round(area / 13000)) }, () => ({ x: rnd(0, w), y: rnd(0, h), vx: rnd(-0.28, 0.28), vy: rnd(-0.28, 0.28) }));
			if (type === 'stars') items = Array.from({ length: Math.min(320, Math.round(area / 3200)) }, () => ({ x: rnd(-1, 1), y: rnd(-1, 1), z: rnd(0.05, 1) }));
			if (type === 'flow') items = Array.from({ length: Math.min(260, Math.round(area / 4200)) }, () => ({ x: rnd(0, w), y: rnd(0, h), life: rnd(40, 200) }));
			if (type === 'snow') items = Array.from({ length: Math.min(120, Math.round(area / 9000)) }, () => ({ x: rnd(0, w), y: rnd(0, h), r: rnd(1, 3.2), v: rnd(0.2, 0.9), o: rnd(0, 6.28) }));
		};
		const local = () => { const r = cv.getBoundingClientRect(); return { x: ptr.x - r.left, y: ptr.y - r.top, on: ptr.moved && FINE }; };
		const draw = (t) => {
			ctx.strokeStyle = ctx.fillStyle = color; ctx.lineWidth = 1;
			if (type !== 'flow') ctx.clearRect(0, 0, w, h);
			const m = local();
			if (type === 'net') {
				items.forEach((p) => { p.x += p.vx; p.y += p.vy; if (p.x < 0 || p.x > w) p.vx *= -1; if (p.y < 0 || p.y > h) p.vy *= -1; });
				for (let i = 0; i < items.length; i++) {
					const a = items[i];
					ctx.globalAlpha = 0.9; ctx.beginPath(); ctx.arc(a.x, a.y, 1.6, 0, 6.3); ctx.fill();
					for (let j = i + 1; j < items.length; j++) { const b = items[j], d = Math.hypot(a.x - b.x, a.y - b.y); if (d < 130) { ctx.globalAlpha = (1 - d / 130) * 0.5; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); } }
					if (m.on) { const d = Math.hypot(a.x - m.x, a.y - m.y); if (d < 190) { ctx.globalAlpha = (1 - d / 190) * 0.9; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(m.x, m.y); ctx.stroke(); } }
				}
			} else if (type === 'stars') {
				const cx = w / 2 + (m.on ? (m.x - w / 2) * 0.1 : 0), cy = h / 2 + (m.on ? (m.y - h / 2) * 0.1 : 0), sp = +cv.dataset.speed || 0.004;
				items.forEach((s) => {
					const pz = s.z; s.z -= sp; if (s.z <= 0.02) { s.x = rnd(-1, 1); s.y = rnd(-1, 1); s.z = 1; return; }
					const x = cx + s.x / s.z * w * 0.5, y = cy + s.y / s.z * w * 0.5, px = cx + s.x / pz * w * 0.5, py = cy + s.y / pz * w * 0.5;
					ctx.globalAlpha = clamp(1.2 - s.z); ctx.lineWidth = (1 - s.z) * 2 + 0.3; ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(x, y); ctx.stroke();
				});
			} else if (type === 'waves') {
				const rows = +cv.dataset.rows || 14;
				for (let k = 0; k < rows; k++) {
					ctx.globalAlpha = 0.15 + 0.6 * (k / rows); ctx.beginPath();
					for (let x = 0; x <= w; x += 12) { const y = h * (0.15 + 0.75 * k / rows) + Math.sin(x * 0.006 + t * 0.0006 + k * 0.5) * (18 + k * 2) + Math.sin(x * 0.013 - t * 0.0004 + k) * 8 + (m.on ? Math.exp(-Math.pow((x - m.x) / 160, 2)) * (m.y - h / 2) * 0.12 : 0); x ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }
					ctx.stroke();
				}
			} else if (type === 'dots') {
				const gap = +cv.dataset.gap || 26;
				for (let y = gap / 2; y < h; y += gap) for (let x = gap / 2; x < w; x += gap) {
					const wave = Math.sin((x + y) * 0.012 - t * 0.0016) * 0.5 + 0.5;
					const near = m.on ? Math.exp(-(Math.pow(x - m.x, 2) + Math.pow(y - m.y, 2)) / 14000) : 0;
					ctx.globalAlpha = 0.18 + wave * 0.25 + near * 0.6; ctx.beginPath(); ctx.arc(x, y, 1.1 + wave * 0.9 + near * 5, 0, 6.3); ctx.fill();
				}
			} else if (type === 'flow') {
				ctx.globalCompositeOperation = 'destination-out'; ctx.globalAlpha = 0.045; ctx.fillRect(0, 0, w, h);
				ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 0.55;
				items.forEach((p) => {
					const a = (Math.sin(p.x * 0.004 + t * 0.00012) + Math.cos(p.y * 0.005 - t * 0.0001)) * 3.1;
					const nx = p.x + Math.cos(a) * 1.5, ny = p.y + Math.sin(a) * 1.5;
					ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(nx, ny); ctx.stroke(); p.x = nx; p.y = ny;
					if (--p.life < 0 || nx < 0 || nx > w || ny < 0 || ny > h) { p.x = rnd(0, w); p.y = rnd(0, h); p.life = rnd(40, 200); }
				});
			} else if (type === 'rings') {
				const cx = w * (+cv.dataset.cx || 0.5), cy = h * (+cv.dataset.cy || 0.5), max = Math.hypot(w, h) * 0.6, n = +cv.dataset.rows || 9;
				for (let k = 0; k < n; k++) { const r = ((t * 0.03 + k * max / n) % max); ctx.globalAlpha = (1 - r / max) * 0.7; ctx.beginPath(); ctx.arc(cx, cy, r, 0, 6.3); ctx.stroke(); }
			} else if (type === 'aurora') {
				const cs = cols.length ? cols : [color];
				cs.forEach((c, k) => {
					ctx.fillStyle = c; ctx.globalAlpha = 0.55; ctx.beginPath(); ctx.moveTo(0, h);
					for (let x = 0; x <= w; x += 24) ctx.lineTo(x, h * (0.3 + 0.18 * k) + Math.sin(x * 0.004 + t * 0.0004 * (k + 1) + k * 2) * h * 0.16 + Math.sin(x * 0.011 - t * 0.0003) * h * 0.05);
					ctx.lineTo(w, h); ctx.closePath(); ctx.fill();
				});
			} else if (type === 'snow') {
				items.forEach((p) => { p.y += p.v; p.x += Math.sin(t * 0.001 + p.o) * 0.3; if (p.y > h + 4) { p.y = -4; p.x = rnd(0, w); } ctx.globalAlpha = 0.35 + p.r / 6; ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.3); ctx.fill(); });
			}
			ctx.globalAlpha = 1;
		};
		init();
		if ('ResizeObserver' in window) new ResizeObserver(() => { init(); if (RM) draw(0); }).observe(cv);
		if (RM) { for (let i = 0; i < (type === 'flow' ? 90 : 1); i++) draw(i * 16); return; }
		if ('IntersectionObserver' in window) new IntersectionObserver((es) => { vis = es[0].isIntersecting; }).observe(cv);
		onTick((t) => { if (vis) draw(t); });
	});

	/* Celebration when a sign-up succeeds */
	const form = document.querySelector('form.signup');
	if (form && !RM) {
		let armed = false;
		form.addEventListener('submit', () => { armed = true; });
		new MutationObserver(() => {
			if (!armed || !form.classList.contains('is-done')) return;
			armed = false;
			const r = form.querySelector('.signup__stack').getBoundingClientRect();
			const cv = document.createElement('canvas'); cv.className = 'fx-burst'; document.body.append(cv);
			const dpr = Math.min(devicePixelRatio || 1, 2); cv.width = innerWidth * dpr; cv.height = innerHeight * dpr;
			const c = cv.getContext('2d'); c.scale(dpr, dpr);
			const st = getComputedStyle(form), palette = [st.getPropertyValue('--b-bg').trim() || '#111', st.getPropertyValue('--focus').trim() || '#888', '#FFD23F', '#FF5A8A', '#3DDC97'];
			const ps = Array.from({ length: 70 }, () => ({ x: r.left + r.width * Math.random(), y: r.top + r.height / 2, vx: rnd(-5, 5), vy: rnd(-11, -3), s: rnd(4, 9), r: rnd(0, 6.3), vr: rnd(-0.3, 0.3), c: palette[Math.random() * palette.length | 0] }));
			const t0 = performance.now();
			const run = (t) => {
				const k = (t - t0) / 1400; c.clearRect(0, 0, innerWidth, innerHeight);
				ps.forEach((p) => { p.vy += 0.32; p.x += p.vx; p.y += p.vy; p.r += p.vr; c.save(); c.translate(p.x, p.y); c.rotate(p.r); c.globalAlpha = clamp(1.4 - k * 1.4); c.fillStyle = p.c; c.fillRect(-p.s / 2, -p.s / 3, p.s, p.s * 0.66); c.restore(); });
				if (k < 1) requestAnimationFrame(run); else cv.remove();
			};
			requestAnimationFrame(run);
		}).observe(form, { attributes: true, attributeFilter: ['class'] });
	}
})();
