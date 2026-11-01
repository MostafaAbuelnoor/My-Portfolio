/* Shared plumbing for drafts J to O: load gate, scroll reveals, word-by-word lines, signup forms, lerped pointer.
   Each draft keeps its own look and its own send-off; this file only removes repetition. */
window.DraftKit = (() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches && !reduce;

  // add .is-loaded once fonts and the portrait are ready (or after 1.5s regardless)
  function ready(img) {
    let done = false;
    const go = () => { if (done) return; done = true; requestAnimationFrame(() => root.classList.add('is-loaded')); };
    Promise.all([document.fonts ? document.fonts.ready : 0, img && img.decode ? img.decode().catch(() => 0) : 0]).then(go);
    setTimeout(go, 1500);
  }

  // [data-reveal] fades up once; [data-words] lights word by word as it crosses a line 40% up the screen
  function reveals() {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });
    document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));
    document.querySelectorAll('[data-words]').forEach((p) => {
      p.innerHTML = p.textContent.trim().split(/\s+/).map((w) => `<span class="w">${w}</span>`).join(' ');
      const wio = new IntersectionObserver((entries) => {
        entries.forEach((e) => e.target.classList.toggle('is-on', e.isIntersecting || e.boundingClientRect.top < 0));
      }, { rootMargin: '0px 0px -40% 0px', threshold: 1 });
      p.querySelectorAll('.w').forEach((w) => wio.observe(w));
    });
  }

  // signup forms. ENDPOINT stays null in drafts: nothing is sent anywhere.
  const ENDPOINT = null;
  const valid = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  function forms({ selector = 'form[data-signup]', doneLabel = 'Subscribed', message = (v) => `Subscribed. Issues go to ${v}.`, onSuccess = () => {} } = {}) {
    document.querySelectorAll(selector).forEach((form) => {
      const input = form.querySelector('input[type="email"]');
      const msg = form.querySelector('.msg');
      const btn = form.querySelector('button[type="submit"]');
      const label = form.querySelector('.btn__label');
      input.addEventListener('input', () => { form.classList.remove('is-invalid'); msg.classList.remove('is-error'); msg.textContent = ''; input.removeAttribute('aria-invalid'); });
      form.addEventListener('submit', async (ev) => {
        ev.preventDefault();
        if (form.classList.contains('is-done')) return;
        const v = input.value.trim();
        if (!valid(v)) {
          form.classList.add('is-invalid'); msg.classList.add('is-error'); input.setAttribute('aria-invalid', 'true');
          msg.textContent = v ? 'That address is missing something. Check it and try again.' : 'Add your email address first.';
          input.focus(); return;
        }
        form.classList.add('is-busy'); btn.disabled = true;
        await new Promise((r) => setTimeout(r, 450));
        form.classList.remove('is-busy'); form.classList.add('is-done');
        if (label) label.textContent = doneLabel;
        msg.textContent = message(v);
        if (form.hasAttribute('data-hero')) onSuccess(form, v);
        else { scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); setTimeout(() => onSuccess(form, v), 600); }
      });
    });
  }

  // lerped pointer inside an element; cb(x, y, inside) runs only while something is still moving
  function pointer(el, cb, ease = 0.12) {
    if (!finePointer) return;
    let tx = 0, ty = 0, x = 0, y = 0, inside = false, raf = 0, first = true;
    const tick = () => {
      x += (tx - x) * ease; y += (ty - y) * ease;
      cb(x, y, inside);
      raf = Math.abs(tx - x) + Math.abs(ty - y) > 0.3 ? requestAnimationFrame(tick) : 0;
    };
    el.addEventListener('pointermove', (e) => {
      const r = el.getBoundingClientRect(); tx = e.clientX - r.left; ty = e.clientY - r.top;
      if (first) { x = tx; y = ty; first = false; }
      inside = true; el.classList.add('is-hover'); if (!raf) raf = requestAnimationFrame(tick);
    });
    el.addEventListener('pointerleave', () => { inside = false; el.classList.remove('is-hover'); cb(x, y, false); });
  }

  const today = (opts = { day: '2-digit', month: 'short', year: 'numeric' }) => new Date().toLocaleDateString('en-GB', opts);
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  return { reduce, finePointer, ready, reveals, forms, pointer, today, sleep, ENDPOINT };
})();
