# CHANGELOG

## [v3.2] - 2026-05-25

### Major Upgrades

**Character Consistency Engine v2.0**
- New dedicated **Identity Lock Specialist** agent
- Added **Character DNA Bible** section (10 core identity fields)
- Introduced **Character Drift Score** (0–10) calculated before every QA review
- Anchor Frame Protocol to lock character identity across clips

**Native Sequence Mode**
- New **Sequence Director** agent
- Automatic multi-clip breaking for content longer than 30 seconds
- Built-in **Auto-Stitch Protocol** with proper `LAST_FRAME_RECAP` + `MOMENTUM_VECTOR` chaining
- Sequence Plan section added to Production Bible

**Reference Image Management Layer**
- Clear distinction between Primary Character Reference, Style Reference, and Mood/Environment Reference
- Automatic generation of properly weighted reference prompts
- Support for multiple uploaded images with explicit weighting instructions

**Performance & Emotion System Expansion**
- Added **Emotional Temperature** meter (1–10) per beat
- Deeper micro-expression and body language evolution tracking
- New **Emotional Audio Layer** in Sound Design Bible

**Quality Assurance Guardian v3.2**
- Expanded from 10-point to **12-point Full Bible Review**
- Now includes Character Drift Score and Sequence Feasibility checks
- Stronger enforcement of QA Gate before any generation

**One-Click Execution Commands**
- New set of ready-to-copy commands at the end of every Production Bible:
  - `EXECUTE FIRST CLIP`
  - `GENERATE ALL REFERENCE IMAGES`
  - `START FULL SEQUENCE (X clips)`
  - `REVISE CHARACTER DNA`
  - `SWITCH TO SEQUENCE MODE`

**Director Signature System**
- Optional cinematic voice activation (e.g., "in the style of Denis Villeneuve", "Blade Runner 2049 look")
- Automatically weaves director-specific techniques, color theory, and pacing throughout the bible

### Other Improvements
- Updated all agents to v3.2 with enhanced capabilities
- Improved Studio State Protocol v3.2 (new fields: `character_drift_score`, `sequence_mode`, `reference_images_used`, `director_signature`)
- Better Self-Evaluation Layer (now includes Character Integrity score)
- More professional and consistent formatting across all output

### Files Updated
- `MASTER_PROMPT_v3.2.md` (Full Mode)
- `MASTER_PROMPT_HYBRID_MODE_v3.2.md`
- `MASTER_PROMPT_AGENT_MODE_v3.2.md`

### Roadmap Progress
- ✅ Character Consistency (major focus of v3.2)
- ✅ Native multi-clip sequencing
- ⏳ Web UI (still planned)
- ⏳ Automatic video stitching script (partially addressed via Sequence Mode)
- ⏳ Community Agent Marketplace (format standardized in v3.2)

---

**Previous Versions**

## [v3.1] - 2026-05
- Initial release with 13 agents
- Quality Assurance Guardian v3.0
- Studio State Protocol v3.0
- Self-Evaluation Layer
- Mandatory QA Gate

## [v3.0] - Earlier
- Multi-agent cinematic production system foundation

---

**Note**: All v3.2 prompts are backward compatible with Grok 4.3 Beta. The new Character DNA and Sequence Mode features significantly reduce drift and improve long-form coherence.
