# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Plain static HTML/CSS/JS, hosted on Netlify (existing setup; no build step).

## Users
Primary: students and individual contributors (ICs) looking to get trained on AWS generative AI. Secondary: employers and recruiters evaluating Mostafa as a portfolio. Corporate training buyers are explicitly not the target.

## Product Purpose
Personal site for Mostafa Saher, an AWS Certified Instructor and consultant. It shows current work and lets individual learners find and engage with his training, while doubling as a portfolio for employers and recruiters.

## Positioning
AWS generative AI (Bedrock and SageMaker) instruction and consulting, with a focus on the Gulf region.

## Operating Context
Live at mostafasaher.com (Netlify). Soft launch: a single page whose main job is collecting learner emails. Old portfolio content can be removed; starting from scratch is approved. research.md in the parent folder surveys comparable instructor sites (credential badges, audience counts, newsletter as conversion hub) and is input, not a decision.

## Capabilities and Constraints
- No framework or build step.
- Enrollment for now = newsletter signup. Mostafa collects emails and shares resources with subscribers. Courses may come later; not part of this launch.
- Newsletter topic: generative AI on AWS (Bedrock, SageMaker) and Claude, including certification prep.
- Email delivery goes through a newsletter service (Buttondown, Kit, Mailchimp or similar). Which one is undecided; the form must be easy to point at its endpoint later.
- Signup incentive: a free practice exam for the Claude Foundation exam (Mostafa's wording; confirm the official exam name). It is not written yet, so the site may only promise it as coming, never link a file that doesn't exist.
- Launch page content: short intro, Mostafa's photo on the left of the hero with a hello and what he does on the right, then a large email signup area below.
- Existing assets: headshot photos (LinkedIn Photo_black.png is the current portrait, on a black background), project images, tech icons, resume PDF.
- Undecided: course platform, pricing display, later site sections.

## Brand Commitments
Name: Mostafa Saher. Needs a logo mark with the name (none exists yet). Mostafa wants a dark site with a strong, contrasting palette (purple not required) and explicitly rejects bright, cream, friendly-creator looks like aliabdaal.com, while liking its structure: photo left, hello and intro right, then a featured block.

## Evidence on Hand
Real project images and a resume PDF in the repo. No testimonials, student counts, subscriber counts, or speaking credentials have been confirmed; do not fabricate them. Certifications and speaking history must be supplied by Mostafa.

## Product Principles
- Lead with the specific niche (AWS GenAI), not a generic developer pitch.
- Serve learners first; make the portfolio credible to recruiters without targeting corporate buyers.
- Show only real, supplied credentials, numbers and work.
- Keep it fast and simple to maintain as static files.

## Accessibility & Inclusion
No specific standard stated. Existing page already respects dark/light color-scheme preference.
