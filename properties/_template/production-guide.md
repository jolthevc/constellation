# Production Guide
property_id: PROP-XXX | Reviewed by:

## Target finish
Platform/native surface and aspect ratio, resolution, length range, accessibility / captioning, delivery file naming, audio loudness spec as applicable, and quality benchmarks. Verify platform technical specs when deploying.

## Approved workflow
Research -> brief with alternative hooks -> script/storyboard -> production asset manifest -> generate/edit -> voice and visual continuity pass -> accuracy/rights/disclosure pass -> preview and edit -> human approval -> post -> log analytics.

## Toolchain (choose only when needed)
- Writing and research:
- Voice generation: approved voice ID/license; pronunciation/cadence instructions; no unauthorized real-person cloning.
- Images/illustration:
- Generated video:
- Real B-roll/archival/screen recordings, licensing and attribution:
- Programmatic render (HTML/CSS/JS/Remotion), where suitable:
- Editing, captions, graphics, sound:
- Publishing mechanisms (manual first; authorized integrations only):

## Prompt / asset recipes
Canonical reusable prompts with version number; negative prompts; lighting and wardrobe consistency; sound design; editing pattern; image/video rights; exact output checks. Save short prompts here, large artifacts in external storage.

## Shot grammar
Hooks, framing, camera moves, real vs synthetic scenes, visual transitions, retention rhythm, payoff depiction, optional Easter eggs or callbacks. Match editorial strategy; never create accidental uncanny or fabricated reality.

## Asset manifest contract
Use `asset_id`, `content_id`, `type`, `uri`, `rights_holder`, `license`, `consent_status`, `created_at`, `source`, `approved_for_use`. Store as JSON/CSV within approved private storage. Do not commit source media and secret URLs to Git.

## QC
Check every scene for visual/voice continuity, source credibility, factual claims, title/caption alignment, satisfying payoff, caption legibility, accessible comprehension, music/IP clearance and synthetic media transparency.

## Economics
Per-content time and variable cost by production step, revisions and bottlenecks. Record estimates as estimates until measured.
