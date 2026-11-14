# Design

The visual system of the minimal page (`v2/drafts/minimal.html`). Product facts live in PRODUCT.md.

## World

A quiet single column of text, after emilkowal.ski, paco.me and nicksaraev.com. No imagery, no colour accent; hierarchy comes from ink against grey.

## Colour

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `--bg` | `#FCFCFB` | `#111110` | Page ground |
| `--text` | `#171716` | `#EDEDEA` | Names, headings, links |
| `--muted` | `#6B6B67` | `#9C9C96` | Running text, meta |
| `--line` | `#E6E6E2` | `#2A2A28` | Rules, field border, underlines |
| `--button` | `#171716` | `#EDEDEA` | Subscribe button |

## Type

Geist, one size (16px / 1.65) for everything except 14px meta and notes. Headings are weight 500 at body size.

## Layout

One 560px column, centred, 24px gutters, 64px between blocks, top padding `clamp(48px, 12vh, 120px)`.

## Components

- **Subscribe**: 44px bordered input plus solid button, 10px radius. States: focus (ink border), busy (button dims), error (red note), done (drawn tick and a confirmation line replace the field).
- **Link row**: name left, handle right in grey, hairline rules above and below.

## Motion

Easing `cubic-bezier(0.23, 1, 0.32, 1)`. Blocks fade up once on load in a 60ms stagger; button presses scale to 0.97; hover effects only on hover-capable pointers; reduced motion removes the entrance.
