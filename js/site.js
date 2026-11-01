// Newsletter signup target.
// Leave empty to collect signups with Netlify Forms (they show up under Forms in the Netlify dashboard).
// When you pick a newsletter service, paste its form action URL here, for example
// "https://buttondown.com/api/emails/embed-subscribe/YOUR-USERNAME".
// The form sends a field named "email" plus "interest" (the answer to question 1).
const SIGNUP_ENDPOINT = "";

(function () {
	"use strict";

	const root = document.documentElement;
	const $ = (sel, scope = document) => scope.querySelector(sel);
	const $$ = (sel, scope = document) => Array.from(scope.querySelectorAll(sel));

	/* ---------- Elapsed timer ---------- */

	const clock = $("[data-clock]");
	const started = Date.now();
	const pad = (n) => String(n).padStart(2, "0");

	function tick() {
		const s = Math.floor((Date.now() - started) / 1000);
		const h = Math.floor(s / 3600);
		const m = Math.floor((s % 3600) / 60);
		clock.textContent = (h ? h + ":" + pad(m) : pad(m)) + ":" + pad(s % 60);
	}
	if (clock) setInterval(tick, 1000);

	/* ---------- Answered / current state ---------- */

	const sections = $$("[data-q]");
	const total = sections.length;
	const currentLabel = $("[data-current]");
	const prev = $("[data-prev]");
	const next = $("[data-next]");

	// Exam state: which questions are answered and which are flagged for review.
	const names = { 1: "introduction", 2: "sample question", 3: "free practice exam" };
	const answered = new Set();
	const flagged = new Set($$('[data-flag][aria-pressed="true"]').map((b) => Number(b.dataset.flag)));

	function render(q) {
		const done = answered.has(q);
		const flag = flagged.has(q);
		$$('[data-cell="' + q + '"]').forEach((cell) => {
			cell.classList.toggle("is-answered", done);
			cell.classList.toggle("cell--flagged", flag);
			if (cell.tagName === "A") {
				cell.setAttribute("aria-label", "Question " + q + ", " + names[q] + (done ? ", answered" : "") + (flag ? ", flagged" : ""));
			}
		});
		const row = $('[data-review="' + q + '"]');
		if (row) {
			row.classList.toggle("is-answered", done);
			row.classList.toggle("is-flagged", flag && !done);
			$("[data-review-state]", row).textContent = done ? (flag ? "Answered, flagged" : "Answered") : flag ? "Flagged" : "Not answered";
		}
		const state = $('[data-state="' + q + '"]');
		if (state) {
			state.textContent = done ? "Answered" : "Not answered";
			state.classList.toggle("is-answered", done);
		}
		const button = $('[data-flag="' + q + '"]');
		if (button) {
			button.setAttribute("aria-pressed", String(flag));
			$(".flag__label", button).textContent = flag ? "Flagged" : "Flag for review";
		}
	}

	function markAnswered(q) {
		answered.add(q);
		render(q);
	}

	$$("[data-flag]").forEach((button) => {
		button.addEventListener("click", () => {
			const q = Number(button.dataset.flag);
			if (flagged.has(q)) flagged.delete(q);
			else flagged.add(q);
			render(q);
		});
	});
	sections.forEach((s) => render(Number(s.dataset.q)));

	function setCurrent(q) {
		currentLabel.textContent = q;
		$$(".navbar__grid .cell").forEach((cell) => {
			if (Number(cell.dataset.cell) === q) cell.setAttribute("aria-current", "step");
			else cell.removeAttribute("aria-current");
		});
		const atStart = q <= 1;
		const atEnd = q >= total;
		prev.href = "#q" + Math.max(1, q - 1);
		next.href = "#q" + Math.min(total, q + 1);
		prev.setAttribute("aria-disabled", String(atStart));
		next.setAttribute("aria-disabled", String(atEnd));
		prev.tabIndex = atStart ? -1 : 0;
		next.tabIndex = atEnd ? -1 : 0;
	}

	// The current question is whichever section crosses the middle of the viewport.
	const visible = new Map();
	const io = new IntersectionObserver(
		(entries) => {
			entries.forEach((e) => visible.set(Number(e.target.dataset.q), e.isIntersecting));
			const q = [...visible].filter(([, on]) => on).map(([n]) => n).sort((a, b) => a - b)[0];
			if (q) setCurrent(q);
		},
		{ rootMargin: "-45% 0px -45% 0px" }
	);
	sections.forEach((s) => io.observe(s));
	setCurrent(1);

	/* ---------- Question 1: what are you preparing for? ---------- */

	const interestFeedback = {
		"claude-exam": "Then the free practice exam is for you. Reserve it below.",
		"build-on-aws": "The newsletter covers building with Bedrock, SageMaker and Claude.",
		"aws-cert": "The newsletter covers certification prep for generative AI on AWS.",
		looking: "Welcome. The sample question below takes about thirty seconds.",
	};
	const feedback = $("[data-interest-feedback]");
	const interestField = $("[data-interest-field]");

	$$('input[name="interest"]').forEach((input) => {
		input.addEventListener("change", () => {
			feedback.textContent = interestFeedback[input.value] || "";
			if (interestField) interestField.value = input.value;
			markAnswered(1);
		});
	});

	/* ---------- Question 2: sample question ---------- */

	const sample = $("[data-sample]");
	if (sample) {
		const submit = $("[data-sample-submit]", sample);
		const hint = $("[data-sample-hint]", sample);
		const options = $('[data-options="sample"]', sample);
		const explanation = $("[data-explanation]", sample);
		const verdict = $("[data-verdict]", sample);

		sample.addEventListener("change", () => {
			submit.disabled = false;
			hint.textContent = "Press Enter or click to check";
		});

		sample.addEventListener("submit", (event) => {
			event.preventDefault();
			const chosen = $("input:checked", options);
			if (!chosen || options.classList.contains("is-marked")) return;

			const chosenLabel = chosen.closest(".option");
			const right = chosenLabel.hasAttribute("data-correct");
			options.classList.add("is-marked");
			$("[data-correct]", options).classList.add("is-correct");
			if (!right) chosenLabel.classList.add("is-wrong");
			$$("input", options).forEach((i) => (i.disabled = true));

			verdict.textContent = right ? "Correct." : "Not quite. The answer is A.";
			verdict.classList.add(right ? "is-pass" : "is-fail");
			submit.hidden = true;
			hint.hidden = true;
			explanation.hidden = false;
			explanation.classList.add("is-in");
			verdict.focus({ preventScroll: true });
			const calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
			explanation.scrollIntoView({ block: "nearest", behavior: calm ? "auto" : "smooth" });
			markAnswered(2);
		});
	}

	/* ---------- Keyboard: A–D answers the question in view ---------- */

	document.addEventListener("keydown", (event) => {
		if (event.ctrlKey || event.metaKey || event.altKey) return;
		const tag = (event.target.tagName || "").toLowerCase();
		if (tag === "input" && event.target.type !== "radio") return;
		if (tag === "textarea" || tag === "select" || event.target.isContentEditable) return;

		const index = "abcd".indexOf(event.key.toLowerCase());
		if (index < 0) return;

		const q = Number(currentLabel.textContent);
		const group = $('[data-q="' + q + '"] .options');
		if (!group || group.classList.contains("is-marked")) return;
		const input = $$("input[type=radio]", group)[index];
		if (!input || input.disabled) return;

		event.preventDefault();
		input.checked = true;
		input.focus({ preventScroll: true });
		input.dispatchEvent(new Event("change", { bubbles: true }));
	});

	/* ---------- Splitter: drag to resize the exhibit pane ---------- */

	const splitter = $("[data-splitter]");
	if (splitter) {
		const min = 30;
		const max = 60;
		const setSplit = (pct) => {
			const v = Math.round(Math.min(max, Math.max(min, pct)));
			root.style.setProperty("--split", v + "%");
			splitter.setAttribute("aria-valuenow", v);
		};
		const pane = splitter.parentElement;

		splitter.addEventListener("pointerdown", (event) => {
			splitter.setPointerCapture(event.pointerId);
			splitter.classList.add("is-dragging");
		});
		splitter.addEventListener("pointermove", (event) => {
			if (!splitter.hasPointerCapture(event.pointerId)) return;
			const box = pane.getBoundingClientRect();
			setSplit(((event.clientX - box.left) / box.width) * 100);
		});
		const stop = (event) => {
			if (splitter.hasPointerCapture(event.pointerId)) splitter.releasePointerCapture(event.pointerId);
			splitter.classList.remove("is-dragging");
		};
		splitter.addEventListener("pointerup", stop);
		splitter.addEventListener("pointercancel", stop);
		splitter.addEventListener("keydown", (event) => {
			const now = Number(splitter.getAttribute("aria-valuenow"));
			const step = event.shiftKey ? 10 : 2;
			if (event.key === "ArrowLeft") setSplit(now - step);
			else if (event.key === "ArrowRight") setSplit(now + step);
			else if (event.key === "Home") setSplit(min);
			else if (event.key === "End") setSplit(max);
			else return;
			event.preventDefault();
		});
	}

	/* ---------- Question 3: signup ---------- */

	const form = $("[data-signup]");
	if (!form) return;

	const email = $("#email", form);
	const error = $("[data-signup-error]", form);
	const button = $("[data-signup-submit]", form);
	const label = $("[data-signup-label]", form);
	const report = $("[data-report]");
	const review = $(".review");
	const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

	function showError(message) {
		error.innerHTML = message;
		email.setAttribute("aria-invalid", "true");
	}

	function clearError() {
		error.textContent = "";
		email.removeAttribute("aria-invalid");
	}

	email.addEventListener("input", () => {
		if (email.getAttribute("aria-invalid") === "true" && emailPattern.test(email.value.trim())) clearError();
	});

	function send(data) {
		if (SIGNUP_ENDPOINT) {
			// Newsletter services answer cross-origin posts opaquely; a resolved request counts as sent.
			return fetch(SIGNUP_ENDPOINT, { method: "POST", body: data, mode: "no-cors" });
		}
		return fetch("/", {
			method: "POST",
			headers: { "Content-Type": "application/x-www-form-urlencoded" },
			body: new URLSearchParams(data).toString(),
		}).then((res) => {
			if (!res.ok) throw new Error("Signup failed with status " + res.status);
		});
	}

	form.addEventListener("submit", (event) => {
		event.preventDefault();
		const value = email.value.trim();

		if (!value) {
			showError("Type your email address so I know where to send the exam.");
			email.focus();
			return;
		}
		if (!emailPattern.test(value)) {
			showError("That address looks incomplete. Check for the @ and a domain, like name@example.com.");
			email.focus();
			return;
		}

		clearError();
		email.value = value;
		button.disabled = true;
		button.classList.add("is-busy");
		label.textContent = "Reserving…";

		send(new FormData(form))
			.then(() => {
				form.hidden = true;
				$("[data-report-email]", report).textContent = value;
				report.hidden = false;
				report.classList.add("is-in");
				root.classList.add("is-subscribed");
				review.classList.add("is-sweeping");
				flagged.delete(3);
				markAnswered(3);
				report.focus({ preventScroll: true });
			})
			.catch(() => {
				button.disabled = false;
				button.classList.remove("is-busy");
				label.textContent = "Reserve my free copy";
				showError('The signup didn’t go through. Try again in a moment, or email me at <a href="mailto:mostafasaher@gmail.com">mostafasaher@gmail.com</a>.');
			});
	});
})();
