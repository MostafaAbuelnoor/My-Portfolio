/* Light and dark for drafts X to AB. Load in <head> before the styles paint.
   The page follows the system setting until the visitor flips the switch; the choice is remembered per draft.
   Every draft styles :root[data-mode="dark"]; without script the page stays light. */
(() => {
  const root = document.documentElement;
  const key = 'draft-mode-' + (root.dataset.draft || 'page');
  const sys = matchMedia('(prefers-color-scheme: dark)');
  let saved = null;
  try { saved = localStorage.getItem(key); } catch (e) {}
  const apply = () => { root.dataset.mode = saved === 'light' || saved === 'dark' ? saved : (sys.matches ? 'dark' : 'light'); };
  apply();
  const listeners = [];
  const sync = () => listeners.forEach((fn) => fn(root.dataset.mode));
  sys.addEventListener('change', () => { if (!saved) { apply(); sync(); } });

  const ICONS = {
    // shown when the page is light: a moon, "switch to dark"
    light: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>',
    // shown when the page is dark: a sun, "switch to light"
    dark: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>',
  };

  window.DraftMode = {
    get: () => root.dataset.mode,
    set(m) {
      saved = m; root.dataset.mode = m;
      try { localStorage.setItem(key, m); } catch (e) {}
      sync();
    },
    onChange: (fn) => listeners.push(fn),
    // any button with [data-mode-toggle] flips light and dark and shows the right icon
    bind() {
      document.querySelectorAll('[data-mode-toggle]').forEach((b) => {
        const paint = (m) => { b.innerHTML = ICONS[m]; b.setAttribute('aria-label', m === 'dark' ? 'Switch to light' : 'Switch to dark'); };
        paint(root.dataset.mode);
        listeners.push(paint);
        b.addEventListener('click', () => {
          const next = root.dataset.mode === 'dark' ? 'light' : 'dark';
          root.classList.add('is-moding');
          window.DraftMode.set(next);
          setTimeout(() => root.classList.remove('is-moding'), 500);
        });
      });
    },
  };
})();
