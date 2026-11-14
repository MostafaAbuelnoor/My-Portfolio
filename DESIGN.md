# Design

The visual system of the tile page (`v2/drafts/bento.html`). Product facts live in PRODUCT.md.

## World

A calm board of rounded tiles on a warm-grey ground, after the Portrait profile and Kalstore founder layouts on Mobbin: one statement tile, one portrait tile, one blue newsletter tile, then links and topics. Blue is used once as a field and once as a text accent.

## Colour

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `--bg` | `#F1F1EE` | `#0E0F12` | Page ground |
| `--tile` | `#FFFFFF` | `#181A1F` | Tiles |
| `--text` | `#14151A` | `#EEEFF2` | Text |
| `--muted` | `#62646D` | `#9EA1AC` | Secondary text |
| `--blue` | `#2348E0` | same | Newsletter tile, headline accent (`#8FA6FF` on dark) |
| `--sky` | `#D9E3FA` | `#C9D6F5` | Portrait tile, light in both modes so the black jacket reads |

## Type

Onest. h1 `clamp(2.1rem, 1.2rem + 3.3vw, 3.5rem)` at 600, tracking -0.035em; h2 1.35rem at 600; text 17px / 1.55.

## Layout

- 1080px board, 14px gaps, 28px tile radius (24px on phones), 12 columns from 820px.
- Desktop: statement and newsletter stacked on the left (7 columns), portrait on the right spanning both rows (5 columns); below, link tiles (5) beside the topics tile (7).
- Phone: one column, portrait first.

## Components

- **Subscribe**: white field with an ink button inside, on the blue tile. States: focus halo, busy, error note, done (tick draws in and a confirmation replaces the field).
- **Link tile**: name, handle, arrow; the whole tile is the link.

## Motion

Easing `cubic-bezier(0.23, 1, 0.32, 1)`. Tiles rise in once on load in a 60ms stagger; presses scale down slightly; hover effects only on hover-capable pointers; reduced motion removes the entrance.
