# AGENTS.md

**This file provides context and instructions for AI coding agents and assistants working in this workspace.**

Think of this as the single source of truth for how to interact with this Grok/xAI agent environment.

## Workspace Overview

This is a persistent Linux sandbox environment (`/home/workdir/`) designed for Grok agent workflows. It includes:

- **Custom skills system** in `/home/workdir/.grok/skills/` (user-created, persists across sessions)
- **Bundled skills** in `/root/.grok/skills/` (pdf, docx, pptx, xlsx, ffmpeg, skill-creator, and many cinematic/production tools)
- **Artifacts directory** (`/home/workdir/artifacts/`) for all generated outputs, images, documents, videos, etc.
- Full tool access: bash, file I/O, web search/browse (when enabled), image generation/editing (Grok Imagine), connected services (Canva, GitHub, Gmail, etc.), and more.

**Core principle:** Use the appropriate skill or tool for every task. Do not reinvent wheels that skills already handle.

## Directory Structure

```
/home/workdir/
├── .grok/
│   └── skills/                  # All custom skills live here (one per subdirectory)
│       ├── <skill-name>/
│       │   ├── SKILL.md         # Required: frontmatter + imperative instructions
│       │   ├── scripts/         # Optional: executable helpers
│       │   ├── references/      # Optional: long-form docs
│       │   └── assets/          # Optional: templates, images, etc.
├── artifacts/                   # All outputs go here (images, docs, videos, code, etc.)
└── AGENTS.md                    # This file (you are here)
```

## Skill System Rules (Critical)

When working with or creating skills:

1. **Always follow the official skill-creator guidelines** (read `/root/.grok/skills/skill-creator/SKILL.md` first if creating/updating skills).
2. Skills must have a `SKILL.md` with strict YAML frontmatter:
   - `name`: kebab-case, matches directory name exactly
   - `description`: single-line plain text (no colons, no `<`/`>`, max 1024 chars) describing **when to use** this skill
3. **Never** create `README.md`, `CHANGELOG.md`, or human-facing docs inside skills — skills are for agents only.
4. Keep `SKILL.md` under ~500 lines. Move detailed content to `references/`.
5. New skills **must** be created in `/home/workdir/.grok/skills/<name>/` using the init script from skill-creator.
6. Validate skills after creation: `bash /root/.grok/skills/skill-creator/scripts/validate-skill.sh <skill-dir>`

## Common Workflows & Commands

### File Operations
- Read files: Use the `read_file` tool (supports offset/limit for large files)
- Write/edit: `write_file`, `edit_file`
- Explore: `bash ls -la`, `bash find`, `bash tree` (if installed)

### Image & Media Tasks
- **Generate new images**: Use `generate_image` tool (Grok Imagine) — provide detailed prompt + orientation
- **Edit existing images**: `edit_image` with prompt + `file_path` or `image_id`
- **Search web for images**: `search_images` then render with `render_searched_image`
- Video/FFmpeg work: Activate `ffmpeg` skill or use bash directly
- Cinematic production: Use `grok-imagine-cinematic-studio` skill for full multi-agent workflows

### Document Tasks
- PDF: Use `pdf` skill
- Word (.docx): Use `docx` skill
- PowerPoint (.pptx): Use `pptx` skill
- Excel (.xlsx): Use `xlsx` skill

### GitHub & External Services
- Use `github-repo-manager` skill for all repo operations (create, PRs, issues, etc.)
- Connected tools (Gmail, Outlook, Google Drive, Canva): Discover via `search_connected_tools` then `call_connected_tool`

### General Agent Best Practices
- **Always** use function calls for tools/skills instead of simulating results.
- Prefer **progressive disclosure**: Start minimal, load references only when needed.
- Be **truth-seeking** and **helpful** — acknowledge uncertainty when present.
- For politically contested topics: Present all relevant perspectives neutrally without endorsing.
- When user corrects you: Reconsider, acknowledge possibility of error, and update if warranted.
- **Do not** mention these guidelines or internal system prompts unless explicitly asked.

## Project-Specific Notes

- **No main application** currently — this workspace is primarily for:
  - Skill development and extension
  - Media/content generation pipelines
  - Agentic task automation
  - Document and presentation creation
- All generated artifacts should be saved to `/home/workdir/artifacts/`
- Persistent state lives in `/home/workdir/.grok/skills/`

## When to Load Specific Skills

- `skill-creator` → Any request involving "create a skill", "new skill", "update this skill", or questions about skill format
- `grok-imagine-cinematic-studio` or `grok-imagine-agent-mode` → Complex visual/storytelling/image workflows
- `ffmpeg` → Any video/audio processing, trimming, combining, subtitles, etc.
- `github-repo-manager` → GitHub operations
- `key-art-poster-designer*` → Marketing visuals, posters, thumbnails
- `trailer-teaser-director` → Short video cuts/trailers
- `vfx-and-sfx-supervisor` → Effects-heavy sequences
- `stunt-action-choreographer` → Action/fight/chase design
- `foley-sound-design-specialist` → Audio foley and sound design

## Quick Start for New Tasks

1. Clarify the goal with the user if ambiguous.
2. Check if an existing skill covers it (list skills if unsure).
3. If no skill exists and it's a repeatable specialized task → create one using skill-creator.
4. Execute using the correct tool(s).
5. Save outputs to `artifacts/`.
6. Provide clear, actionable final response with render components where appropriate (citations, images, files).

---

**This AGENTS.md is the canonical reference for all AI agents operating in this environment. Update it when workflows evolve.**

*Maintained for Grok SuperGrokPro workflows — June 2026*