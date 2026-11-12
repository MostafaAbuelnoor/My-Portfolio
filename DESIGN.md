# Design

The visual system of the hub page (`v2/drafts/hub.html`). Product facts live in PRODUCT.md.

## World

Highlighter on a white page. A marker-yellow hero field carries the claim, the portrait and the sign-up; everything after it is white paper with hairline-ruled link rows, closing on one ink panel.

## Colour

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `--marker` | `#FFD426` | same | Hero field, accents on ink, selection |
| `--ink` | `#15140F` | same | Text on marker, buttons, close panel |
| `--on-marker-soft` | `#4D4100` | same | Secondary text on marker (never grey) |
| `--bg` | `#FFFFFF` | `#121210` | Page ground |
| `--text` | `#15140F` | `#F3F1E7` | Body text |
| `--muted` | `#615F55` | `#A6A396` | Descriptions, meta |
| `--line` | `#E7E5DC` | `#2B2A24` | Row and section rules |

The hero stays yellow in dark mode. Yellow is a field or a button fill, never text on white.

## Type

- Headings: Bricolage Grotesque 700, tracking -0.025 to -0.035em, h1 `clamp(2.7rem, 1.2rem + 5.6vw, 5.3rem)` at line-height 0.98.
- Text: Schibsted Grotesk, 17px / 1.6; lead paragraph 1.2rem.
- The white swipe (`.swipe`) sits behind one phrase in the h1 only.

## Layout

- Container 1120px, gutter `clamp(20px, 4.5vw, 40px)`.
- From 860px: sections are a 220px heading column plus content; the portrait is anchored to the hero's bottom-right edge.
- Below 860px: single column, copy and form first, portrait under them.

## Components

- **Subscribe control** (`.signup`): white pill field, 60px, with the button inside. States: focus ring in ink, busy (progress wash across the button), error (message under the field), done (ink pill with a drawn tick). Sixteen-pixel input text so phones do not zoom.
- **Link row** (`.row`): title, optional description, right-aligned meta, arrow. Whole row is the link; 12px radius hover tint.
- **Pills** are for controls only. Panels use a 16px radius. Elevation is a soft offset shadow on the hero field control, nothing else.

## Motion

- Easing `cubic-bezier(0.23, 1, 0.32, 1)`; presses scale to 0.97 in 140ms.
- One entrance on load: hero copy rises in a 70ms stagger, the portrait stands up, the swipe draws left to right. Nothing animates on scroll.
- Hover effects sit behind `(hover: hover) and (pointer: fine)`; reduced motion removes the entrance.
