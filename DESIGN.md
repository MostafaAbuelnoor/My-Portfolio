---
name: Mostafa Saher
description: A night-mode certification exam console for an AWS generative AI instructor.
colors:
  graphite-ground: "#171717"
  graphite-pane: "#1D1D1D"
  graphite-raise: "#262626"
  exhibit-black: "#000000"
  hairline: "#303030"
  hairline-strong: "#4A4A4A"
  cell-off: "#3A3A3A"
  ink: "#F0F0EE"
  ink-muted: "#B8B8B5"
  ink-faint: "#939391"
  offer-amber: "#FFB224"
  offer-amber-hover: "#FFC45A"
  on-offer: "#1B1300"
  pass-green: "#38D98A"
  on-pass: "#03200F"
  fail-red: "#FF6F61"
typography:
  display:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(3rem, 1.6rem + 4.4vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 1.2rem + 4.4vw, 5.25rem)"
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: "-0.04em"
  title:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 1.3rem + 1.4vw, 2.5rem)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  question:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1rem + 0.9vw, 1.75rem)"
    fontWeight: 600
    lineHeight: 1.32
    letterSpacing: "-0.01em"
  lede:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.3vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1.55
  mono-data:
    fontFamily: "Atkinson Hyperlegible Mono, ui-monospace, Cascadia Mono, Consolas, monospace"
    fontSize: "0.875rem"
    fontWeight: 600
    fontFeature: "\"tnum\" 1"
  mono-state:
    fontFamily: "Atkinson Hyperlegible Mono, ui-monospace, Cascadia Mono, Consolas, monospace"
    fontSize: "0.8125rem"
    fontWeight: 400
rounded:
  cell: "1.5px"
  key: "4px"
  control: "6px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  gutter: "clamp(16px, 3.2vw, 48px)"
  bar: "56px"
  nav: "64px"
components:
  button-offer:
    backgroundColor: "{colors.offer-amber}"
    textColor: "{colors.on-offer}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 22px"
    height: "52px"
  button-offer-hover:
    backgroundColor: "{colors.offer-amber-hover}"
    textColor: "{colors.on-offer}"
  button-offer-big:
    backgroundColor: "{colors.offer-amber}"
    textColor: "{colors.on-offer}"
    rounded: "{rounded.control}"
    padding: "0 28px"
    height: "64px"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.graphite-ground}"
    rounded: "{rounded.control}"
    padding: "0 22px"
    height: "52px"
  button-disabled:
    backgroundColor: "transparent"
    textColor: "{colors.ink-faint}"
    rounded: "{rounded.control}"
  option:
    backgroundColor: "{colors.graphite-pane}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 16px 10px 12px"
    height: "52px"
  option-hover:
    backgroundColor: "{colors.graphite-raise}"
  option-key:
    backgroundColor: "transparent"
    textColor: "{colors.ink-muted}"
    typography: "{typography.mono-data}"
    rounded: "{rounded.key}"
    size: "30px"
  option-key-checked:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.graphite-ground}"
  option-key-correct:
    backgroundColor: "{colors.pass-green}"
    textColor: "{colors.on-pass}"
  option-key-wrong:
    backgroundColor: "{colors.fail-red}"
    textColor: "{colors.graphite-ground}"
  cell:
    backgroundColor: "{colors.graphite-ground}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.mono-data}"
    rounded: "{rounded.key}"
    size: "34px"
  cell-answered:
    backgroundColor: "{colors.pass-green}"
    textColor: "{colors.on-pass}"
  pane-bar:
    backgroundColor: "{colors.graphite-pane}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    padding: "6px {spacing.gutter}"
    height: "44px"
  answer-input:
    backgroundColor: "{colors.graphite-pane}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "64px"
  answer-input-focus:
    backgroundColor: "{colors.graphite-raise}"
  report-stamp:
    backgroundColor: "{colors.pass-green}"
    textColor: "{colors.on-pass}"
    typography: "{typography.mono-data}"
    rounded: "{rounded.key}"
    padding: "6px 12px"
---

# Design System: Mostafa Saher

## Overview

**Creative North Star: "The Exam Console"**

The site is a night-mode certification test console. Every surface borrows the working furniture of a proctored exam: a sticky exam bar with a question counter and an elapsed timer, split item panes (exhibit on the left, stem on the right) divided by a draggable splitter, keyed A–D option rows, a flag-for-review toggle, a numbered review grid, and a fixed Previous / cells / Next bar. Scrolling moves through questions; success shows as a score report. The world is the interface, not a costume over one.

Material is flat and hairlined. Depth comes from three stepped graphite tones and 1px rules, never from shadow, glow, gradient or card. Colour prints flat at full saturation and carries state, not decoration: amber is the offer and the flag, green is answered and correct, red is a wrong answer or an error. Everything else is hue-free graphite and near-white ink. Density is calm: one question per viewport-tall item, generous gutters, large display type in the stem.

Motion is quiet and functional: 140ms state transitions, a single rise for revealed content, and one authored moment when a signup succeeds (the review cells fill green in sequence and the score report rises). Reduced motion collapses all of it.

**Key Characteristics:**
- Graphite ground, black exhibit panes, 1px hairline structure.
- Flat, fully saturated state colour: amber offer/flag, green pass, red fail.
- One typeface family: Atkinson Hyperlegible Next for all prose and UI, Atkinson Hyperlegible Mono only for machine-read values.
- Exam-console components are the vocabulary: exam bar, pane bars, keyed options, review cells, bottom nav.
- The MS mark is drawn from review-grid cells, with the final cell as the amber flag.

## Colors

A hue-free graphite night palette with three flat, saturated state colours that each mean exactly one thing.

### Primary
- **Offer Amber** (offer-amber): the call to action and the review flag. Fills the offer buttons, the flagged-cell corner, the pressed flag toggle, the input focus ring, text selection and the caret. Hover lifts to **Offer Amber Hover** (offer-amber-hover); text on amber is **Amber Ink** (on-offer), a near-black warm brown.

### Secondary
- **Pass Green** (pass-green): answered and correct. Fills answered review cells, the correct option key, the Pass stamp on the score report, the "Answered" state text, the feedback bullet, and the mark's flag cell after a signup. Text on green is **Pass Ink** (on-pass).

### Tertiary
- **Fail Red** (fail-red): a wrong answer and nothing decorative. Marks the wrong option and the fail verdict, and in the signup form the invalid-input border and error message.

### Neutral
- **Graphite Ground** (graphite-ground): page ground, exam bar, bottom nav, empty review cells.
- **Graphite Pane** (graphite-pane): pane bars, option rows at rest, the answer input, the review column.
- **Graphite Raise** (graphite-raise): hover and checked option rows, focused input, inline code chips.
- **Exhibit Black** (exhibit-black): exhibit panes that hold the portrait and data; the photo's black background runs into it.
- **Hairline** (hairline): every structural rule: bar edges, pane dividers, splitter, table rows.
- **Hairline Strong** (hairline-strong): control outlines (options, keys, cells, inputs, nav steps), table head rule, scrollbar thumb.
- **Cell Off** (cell-off): the unlit cells of the MS mark only.
- **Ink** (ink): primary text, headings, checked state, focus outlines.
- **Ink Muted** (ink-muted): secondary text, lede, pane-bar text, explanation body.
- **Ink Faint** (ink-faint): hints, fine print, state text at rest, table headers, footer meta.

### Named Rules
**The One Meaning Rule.** Amber means offer or flag, green means answered or correct, red means wrong or error. A colour never appears outside its meaning, and never as decoration.

**The Flat Print Rule.** State colours print as flat fills or 1px strokes at full saturation. No gradients, tints, glows or translucent washes.

**The Hue-Free Ground Rule.** Grounds, panes and rules are neutral grey or pure black; they carry no blue or warm cast.

## Typography

**Display Font:** Atkinson Hyperlegible Next (with Segoe UI, system-ui)
**Body Font:** Atkinson Hyperlegible Next (with Segoe UI, system-ui)
**Label/Mono Font:** Atkinson Hyperlegible Mono (with ui-monospace, Cascadia Mono, Consolas)

**Character:** A legibility face built for readers with low vision, pushed to 800 and tight tracking for headlines so it reads as a confident exam paper; its mono sibling gives counters and data the look of a test console readout.

### Hierarchy
- **Display** (800, fluid 3–6rem, 0.92): the item-1 greeting only; balanced wrapping.
- **Headline** (800, fluid 2.5–5.25rem, 0.96): the signup question; max 13em.
- **Title** (800, fluid 1.75–2.5rem, 1.05): score-report title and footer name.
- **Question** (600, fluid 1.25–1.75rem, 1.32): question stems; max 34em.
- **Lede** (400, fluid 1.0625–1.25rem, 1.55): the sentence under a display or headline, in Ink Muted; max 34–36em.
- **Body** (400, 1.0625rem, 1.55): option text (1.4 line-height), explanations, report body.
- **Label** (600, 0.9375rem): pane-bar tags, flag toggle, nav steps, option legend (1.125rem), answer label (1rem).
- **Mono Data** (600 or 400, 0.875rem, tabular figures): counter, timer, option keys, cells, stamp, data-log table (0.9375rem).
- **Mono State** (400, 0.8125rem): "Not answered / Answered / Flagged" state text.

### Named Rules
**The Machine Voice Rule.** Mono is reserved for values a console would print: timer, counters, cell numbers, option keys, state text, data logs, code and the result stamp. Headings, prose and buttons are never mono.

**The Three Weights Rule.** Only 400, 600 and 800 of Next (and 400, 600 of Mono) are loaded; use only those.

## Layout

The page is a stack of viewport-tall items between a sticky exam bar (56px; 52px under 900px) and a fixed bottom nav (64px). Each item fills `100svh` minus both bars. Horizontal padding is the fluid gutter everywhere.

Items split into panes. The intro item is exhibit | 1px splitter | stem, with the exhibit at a default 44% that the reader can drag between 30% and 60% (keyboard-operable). The sample item is exhibit | stem at the same split. The signup item is a wide stem beside a 300–380px review column. Every pane opens with a 44px pane bar. Stem content caps at 760px and centres vertically; the signup column caps at 1040px.

Spacing follows an 8/12/16/24/32/48 rhythm: 8px between option rows and grid cells, 12–16px inside controls, 24–32px between a lede or question and what follows, 40–48px before option groups and the answer form.

Responsive behaviour:
- **1100px and up:** intro options sit in a 2x2 grid.
- **899px and down:** all items collapse to one column; the splitter hides; the portrait crops to min(34svh, 360px); on the intro the offer button rises above the question; the review column moves under the form; the footer stacks left-aligned.
- **560px and down:** the exam bar drops the "Question" word and timer icon; nav steps and the flag become 44px icon-only squares; the answer row stacks with a full-width button; the data log steps down to 0.8125rem.

## Elevation & Depth

The system is flat. There are no drop shadows. Depth is tonal and linear: Exhibit Black sits below Graphite Ground, which sits below Graphite Pane, which sits below Graphite Raise, and 1px hairlines separate every region. Sticky and fixed bars are distinguished only by their hairline edge and opaque ground.

The one `box-shadow` in the build is an inset 1px ring that doubles the border of the current nav cell; it is a stroke, not elevation.

### Named Rules
**The No-Lift Rule.** Nothing floats. Hover and selection change tone and stroke, never shadow or scale. The only movement on press is a 1px downward nudge on buttons.

## Shapes

Rectilinear with small, consistent corners. Controls (buttons, option rows, input, nav steps) use a 6px corner; small squares (option keys, review cells, flag toggle, stamp, kbd) use 4px; the cells of the MS mark use 1.5px. Borders are always 1px, except the keycap's 2px bottom edge. The flagged cell carries a small amber triangle clipped into its top-right corner. Verdict and feedback markers are small squares (8–12px), never circles. Icons are 2px-stroke line SVGs at 16–18px with round caps.

## Components

### Buttons
Heavy, flat and decisive.
- **Shape:** gently squared (6px), 52px tall, 22px side padding; the big variant is 64px tall with 28px padding.
- **Offer:** Offer Amber fill with Amber Ink text; hover lifts to Offer Amber Hover. The only amber button; it always leads to or submits the signup.
- **Ink:** Ink fill with Graphite Ground text; hover goes to pure white. Used for in-question actions ("Check my answer").
- **Disabled:** transparent with a Hairline Strong outline and Ink Faint text.
- **Hover / Focus / Active:** 140ms colour transitions; 2px Ink focus outline at 3px offset; 1px downward press.

### Option Rows
The keyed A–D answer rows are the signature control.
- **Rest:** Graphite Pane fill, Hairline Strong 1px border, 6px corner, 52px min height; a 30px mono key square (4px corner) then the answer text.
- **Hover:** border to Ink Faint, fill to Graphite Raise.
- **Checked:** border Ink, fill Graphite Raise, key inverts to Ink with Graphite Ground letter.
- **Marked:** after checking, the correct row takes a Pass Green border and filled green key; a wrong pick takes Fail Red; the rest drop to 50% opacity.
- Keyboard: A–D select; the hint uses keycap `kbd` styling.

### Inputs / Fields
- **Style:** the answer input is 64px tall (58px on small screens), Graphite Pane fill, Hairline Strong border, 6px corner, 1.3125rem text.
- **Focus:** border and 2px outline turn Offer Amber, fill to Graphite Raise.
- **Error:** Fail Red border with a bold Fail Red message below.

### Navigation
- **Exam bar (top, sticky):** three columns: mark and name, mono "Question n of 3" with the current number in Ink 600, mono elapsed timer with a clock icon.
- **Bottom nav (fixed):** Previous and Next steps (42px, outlined, 6px corner; icon-only 44px squares under 560px) around a row of review cells; the current cell gets an Ink double stroke; disabled steps fade to 35%.

### Review Cells
34px mono squares with a 4px corner. At rest: Graphite Ground fill, Hairline Strong border, Ink Muted number. Answered: Pass Green fill and border with Pass Ink number. Flagged: amber corner triangle. Transitions are 300ms ease-out. Shared by the bottom nav and the review column, and the same cell is the building block of the MS mark.

### Pane Bars and Flag Toggle
Every pane starts with a 44px Graphite Pane bar with a hairline bottom edge: exhibit bars name the exhibit ("Exhibit 1" in Ink 600, description in Ink Muted); stem bars carry mono state text and the flag toggle. The flag is a ghost button that gains a Hairline Strong border on hover and turns Offer Amber with a filled flag when pressed.

### Score Report
The success state. A hairline-topped block with a Pass Green mono stamp reading the result ("Pass"), a Title-scale heading and Body text. It rises (520ms, 360ms delay) while the review cells fill green in 90ms steps. The stamp states a result; it is not a section label.

### Footer Lockup
The large MS mark (56–96px tall) over the name at Title scale and the role in Ink Muted; meta and underlined links sit right-aligned, closing with "End of exam".

## Do's and Don'ts

### Do:
- **Do** build new surfaces from the console vocabulary: exam bar, split panes with 44px pane bars, keyed options, review cells, bottom nav.
- **Do** keep colour to its single meaning: Offer Amber for the offer and flags, Pass Green for answered and correct, Fail Red for wrong answers and errors.
- **Do** separate regions with 1px Hairline rules and stepped graphite tones.
- **Do** use Atkinson Hyperlegible Mono only for timer, counters, cells, option keys, state text, data and code.
- **Do** use 140ms colour transitions for state, the 420ms ease-out rise (cubic-bezier(0.16, 1, 0.3, 1)) for revealed content, and respect prefers-reduced-motion.
- **Do** keep every tap target at least 44px on small screens.

### Don't:
- **Don't** use drop shadows, glows, gradients or card containers.
- **Don't** tint grounds, panes or exhibits with a hue; they stay neutral grey or black.
- **Don't** use amber, green or red decoratively or for anything outside its meaning.
- **Don't** set headings, buttons or prose in mono.
- **Don't** add a second authored animation; the signup success sequence is the one moment.
- **Don't** use round portraits, pill-shaped cards or friendly-creator styling; corners stay at 6px or less.
