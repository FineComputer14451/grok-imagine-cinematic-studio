# Grok Imagine Cinematic Studio — UPGRADE GUIDE

**From v3.4 → v3.5 (Skill Update)**

**Date:** June 2026

---

## Overview

This guide helps you upgrade your Grok Imagine Cinematic Studio setup from **v3.4** to the new **v3.5** skill version. The v3.5 update significantly expands the system from 20 to **22 specialized agents**, introduces a complete Role Card system, and improves activation workflows.

---

## What’s New in v3.5

### 1. Agent Expansion (20 → 22)
Two powerful new agents have been added:

| New Agent | Role |
|-----------|------|
| **Production Designer / Set Decorator v3.5** | Environment DNA, Prop Memory Bank, world-building consistency, and set continuity |
| **Localization & Subtitle Specialist v3.5** | Cultural adaptation, SDH subtitles, multi-language support, and tone preservation |

### 2. Complete Role Card System
- Every agent now has an **authoritative v3.5 Role Card** (detailed `.txt` + quick `.md` summary)
- Located in `references/agents/`
- Each card includes: Core Mission, v3.5 Upgrades, Sophisticated Elements (DNA systems), Decision Framework, Output Format, and Activation Command

### 3. Improved Activation System
- New comprehensive **Agent Activation Instructions** section
- Full table of all 22 activation commands
- Powerful new patterns: `ACTIVATE ONLY ...`, mode commands (`MAXIMUM_CONSISTENCY_MODE`, `HIGH_ACTION_MODE`, etc.)
- Better organization with grouped agent categories

### 4. Documentation Overhaul
New and updated files:
- `Agent_Role_Definitions.md` — Clean single-page overview of all 22 agents
- `Quick_Start_Guide.md` — Completely updated with 22-agent workflow
- `CHANGELOG.md` — New v3.5 Skill Update entry
- `UPGRADE_GUIDE.md` — This file (you’re reading it)

---

## Migration Steps

### Step 1: Update Your Skill
Replace your current `grok-imagine-cinematic-studio` skill with the latest v3.5 version (or let the system auto-update if using the latest Grok build).

### Step 2: Activate the New Studio
Run this command in a new chat:
```
Activate Grok Imagine Cinematic Studio v3.5
```

### Step 3: Update Your Workflows (Recommended)
- Replace old activation commands with the new standardized ones (see table in `SKILL.md`)
- Start using the new specialists:
  - `ACTIVATE PRODUCTION_DESIGNER` for environment work
  - `ACTIVATE LOCALIZATION_SPECIALIST` for subtitles and cultural adaptation

### Step 4: Explore the New Role Cards
Browse `references/agents/` to see the full v3.5 Role Cards for every agent. These are now the authoritative source for each specialist’s capabilities.

### Step 5: Update Existing Projects (Optional but Recommended)
For ongoing projects:
1. Say: `"Update Project Bible to v3.5 standards"`
2. Re-activate key agents with the new commands
3. Run `RUN QA REVIEW` to ensure continuity with the new system

---

## Breaking Changes

- Old activation commands like `ACTIVATE KEY_ART` have been standardized to `ACTIVATE KEY_ART_DESIGNER`
- The system now defaults to **22 agents** (previously 20)
- Some v3.4 Role Cards have been significantly expanded in v3.5

**No breaking changes** to core functionality — all previous workflows will continue to work.

---

## Recommended New Workflow

After upgrading, we recommend adopting this pattern:

1. **Primary Activation** — Always start with `Activate Grok Imagine Cinematic Studio v3.5`
2. **Use Specialist Commands** — Activate specific agents only when needed
3. **Reference Role Cards** — Check `references/agents/[agent-name].md` for exact capabilities
4. **Use New Patterns** — Try `ACTIVATE ONLY ...` and mode commands for focused work

---

## Need Help?

- See `Quick_Start_Guide.md` for the full updated workflow
- See `Agent_Role_Definitions.md` for a clean overview of all 22 agents
- See `SKILL.md` for the complete activation command table

---

**Welcome to Grok Imagine Cinematic Studio v3.5!**

The system is now more powerful, better organized, and ready for professional cinematic productions.

*Upgrade completed — June 2026*