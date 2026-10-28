# Content Format Intelligence

Last researched: 2026-10-27. Status: foundational taxonomy, not a performance ranking.

## Purpose

A reusable, research-backed library of the ways a media property can package its content. Every media property should choose formats based on audience psychology, topical fit, cultural conventions, quality, cost, and experiments, not on an a priori preference for AI talking heads.

## Files
- `catalog.csv`: 149 initial components, spanning live action, faceless, podcast, animation, programmatic visuals, synthetic formats, interactive content, commerce, and platform surfaces.
- `format-template.md`: deeper research / experimentation template for an individual format.
- `research-sources.md`: source bibliography, evidence boundaries, and research queue.

## Five combinable layers

1. **Presentation**: the viewer-facing scene or communication convention. Example: close-camera monologue, two-host conversation, real street interview.
2. **Story engine**: how information or entertainment unfolds. Example: mystery, opinion, tutorial, transformation, documentary, comparison.
3. **Visual treatment**: how scenes and meaning are rendered. Example: archive + B-roll, kinetic text, animated graphics, Remotion or equivalent HTML/CSS/JS render, animation, generated video.
4. **Engagement mode**: the intended audience interaction. Example: comment reply, community prompt, quiz, reaction, co-creation.
5. **Distribution surface**: where and in what native publishing container it appears. Example: short vertical video, long-form video, live, carousel, text post, broadcast channel, podcast.

A format may span layers in practice. A content strategy should link several components rather than inventing endless combination names. This is why the format catalog should be **broad and composable**. A 'podcast clip with animated subtitles and a polarizing question' is not three mutually exclusive formats.

## Psychological layer

For every format selection, specify:
- **Scroll-stop reason**: stimulus, curiosity, emotional relevance, surprise, recognition, credible utility.
- **Stay reason**: open question, story progression, proof, social tension, aesthetic absorption, or anticipated outcome.
- **Satisfaction / payoff**: what reward is actually delivered. Never promise a revelation and withhold it.
- **Share reason**: helpfulness, identification, signaling taste, humor, awe, bonding, status.
- **Follow reason**: expected recurring value, trustworthy voice, seriality, companionship, identity alignment.
- **Commercial permission**: which product introductions fit audience expectations without eroding trust.
- **Risks**: exaggerated claims, false intimacy, fabricated evidence, burnout, insensitive targeting, deceptive synthetic footage.

Use the mechanism vocabulary in `../psychology/framework.md`. All mechanism tags in the initial catalog are **hypotheses**, not proven causal effects for any given audience.

## Research expansion protocol

For each high-priority format:
1. Find at least 5 distinctive working examples across at least 3 properties, with links, account, post date, platform, visual structure, and qualitative observations.
2. Sample failures as well as successes to avoid survivorship bias.
3. Record audience and niche context. Do not generalize from one creator or one platform.
4. Identify the creative promise, story structure, shot grammar, pacing, visuals, audio, authenticity requirements, and production method.
5. Distinguish observed platform signals from creator guesses or our hypotheses; store date and confidence.
6. Assess human versus agent feasibility and calculate an estimated marginal production cost for a *comparable quality bar*.
7. Design an A/B test that changes one meaningful variable while preserving creative quality.
8. Add new formats when a meaningful new presentation, storytelling, visual, or participation grammar emerges. Avoid duplicate synonyms.
9. Review time-sensitive platform features and creative norms at least quarterly; flag stale claims.
10. Add performance evidence to properties and performance tracking; don't silently overwrite original research.

## Feasibility labels

The CSV column `automation_feasibility_initial` is an unvalidated preliminary heuristic:
- `high`: much of the pipeline can plausibly be programmed, composed, or generated, subject to human quality review.
- `medium`: some controllable or repeated production, but taste, visual continuity, or quality may be fragile.
- `low`: dependent on real-world access, real participants, live events, or filming. AI can assist, but cannot replace authentic source material.

These are **not** automated-success predictions.

## Non-negotiables

- Do not disguise synthetic interviews, fabricated testimonials, or reenactments as real reporting.
- Respect consent, likeness and voice rights, copyrighted source material, and platform disclosure policies.
- No fake engagement, fabricated interaction, or misrepresentation of a character as a real human.
- Optimize for fulfilled expectations and sustained trust, not exploitative retention.
- Every property uses an empirically validated *portfolio* of formats rather than one compulsory house style.

## Hook and payoff crosswalk
Every deployed format combination also needs an explicit attention, retention, payoff and relationship design. See [engagement-design.md](engagement-design.md), [36 hook families](../psychology/hook-library.csv), and [the progression/payoff playbook](../psychology/retention-and-payoff-playbook.md). These tactical records are hypotheses; they do not imply the format automatically produces a ranking benefit. A format may be effective with no spoken CTA and restrained pacing.
