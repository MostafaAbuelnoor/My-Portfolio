(() => {
	const KEY = 'ms-subscribed';
	const form = document.querySelector('form.signup');
	if (!form) return;
	const input = form.querySelector('input[type="email"]');
	const note = form.querySelector('.note');
	const DEFAULT = note.textContent;

	const markDone = () => {
		form.classList.remove('is-busy');
		form.classList.add('is-done');
		form.querySelector('.done').removeAttribute('aria-hidden');
		form.querySelectorAll('.field input, .field button').forEach((el) => { el.disabled = true; });
	};
	const fail = (html) => { form.classList.remove('is-busy'); note.dataset.state = 'error'; note.innerHTML = html; };

	try { if (localStorage.getItem(KEY) === '1') markDone(); } catch (e) {}

	input.addEventListener('input', () => {
		if (note.dataset.state === 'error') { note.dataset.state = ''; note.textContent = DEFAULT; }
	});

	form.addEventListener('submit', async (event) => {
		event.preventDefault();
		if (form.classList.contains('is-busy') || form.classList.contains('is-done')) return;
		input.value = input.value.trim();
		if (!input.value) { fail('Enter your email address to subscribe.'); input.focus(); return; }
		if (!input.checkValidity()) { fail('That email doesn’t look right. Check it and try again.'); input.focus(); return; }
		form.classList.add('is-busy');
		note.dataset.state = '';
		note.textContent = 'Subscribing…';
		try {
			const response = await fetch('/', {
				method: 'POST',
				headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
				body: new URLSearchParams(new FormData(form)).toString(),
			});
			if (!response.ok) throw new Error(String(response.status));
			try { localStorage.setItem(KEY, '1'); } catch (e) {}
			markDone();
		} catch (error) {
			fail('That didn’t go through. Try again, or <a href="mailto:mostafasaher@gmail.com?subject=Subscribe">email me</a> and I’ll add you.');
		}
	});

	document.querySelectorAll('[data-focus-signup]').forEach((link) => {
		link.addEventListener('click', (event) => {
			if (input.disabled) return;
			event.preventDefault();
			input.scrollIntoView({ block: 'center', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
			input.focus({ preventScroll: true });
		});
	});

	document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });
})();
