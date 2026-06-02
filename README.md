<p align="center">
  <img src="assets/banner.jpg" alt="Grok Imagine Cinematic Studio Banner" width="100%">
</p>

# 🎬 Grok Imagine Cinematic Studio v3.5

**The most advanced multi-agent cinematic production system for Grok 4.3**

Transform any story into emotionally powerful, production-ready cinematic video with perfect character consistency, persistent memory, and a full **22-agent** professional film crew.

[![Version](https://img.shields.io/badge/version-3.5-blue)](https://github.com/FineComputer14451/grok-imagine-cinematic-studio)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Grok](https://img.shields.io/badge/Grok-4.3-purple)](https://x.ai)

---

## ✨ What's New in v3.5

- **22 Specialized Agents** with full v4.0 personalities and structured Role Cards
- **Authoritative Role Cards** in `references/agents/` — Complete Core Mission, v3.5/v4.0 Upgrades, Decision Frameworks, Specialized Protocols, and Activation Triggers
- **Full Python CLI** — Memory management, Production Bible generation, PDF reports, cost simulation, and project initialization
- **Streamlit Web UI** — Visual project input, Role Card browser, Memory / Character DNA management, live cost estimator, and rich Production Bible export
- **13 Professional Production Bible Examples** across major genres (Sci-Fi, Drama, Thriller, Erotic, Fantasy, Horror Comedy, Period, etc.)
- **Persistent Character Memory Bank** with cross-session support
- **Native Extend-from-Frame** + advanced long-form cinematic sequencing (60–120s+)
- **Pre-Generation Cost Simulator** + real-time quota optimization
- **Improved CI Workflow** with dynamic Role Card validation

---

## 🚀 Quick Start

### 1. Fastest: Master Prompt Activation
1. Copy the content of [`MASTER_PROMPT_v3.5.md`](MASTER_PROMPT_v3.5.md)
2. Paste into a new Grok 4.3 chat
3. Type: `Activate Grok Imagine Cinematic Studio v3.5`

### 2. Recommended: Python CLI (Power Users)
```bash
pip install -r requirements.txt
python tools/cinematic_studio_cli.py --help

# Examples
python tools/cinematic_studio_cli.py status
python tools/cinematic_studio_cli.py create-bible --story "Your cinematic vision here"
python tools/cinematic_studio_cli.py memory add --name "Elena Voss" --value "Silver-gray hair, quiet confidence..."
```

### 3. Most Visual: Streamlit Web UI
```bash
pip install -r requirements-streamlit.txt
streamlit run web_ui/app.py
```

---

## 🏗️ System Architecture

```
Studio Director v3.5
├── references/agents/          # Authoritative 22 Role Cards (recommended)
├── tools/cinematic_studio_cli.py   # Full-featured CLI + Memory + PDF reports
├── web_ui/app.py                 # Streamlit frontend with Memory management
├── examples/                     # 13 ready-to-use Production Bible templates
├── MASTER_PROMPT_v3.5.md         # Main activation prompt
└── .grok/skills/                 # Custom Grok skills
```

**Key Components:**
- `references/agents/` — **Single source of truth** for all 22 Role Cards
- `tools/cinematic_studio_cli.py` — CLI with memory, bible generation, and reporting
- `web_ui/app.py` — Modern web interface with live simulation and Memory section
- `examples/` — Diverse, high-quality Production Bible templates

---

## 🎥 The 22-Agent Professional Film Crew

### Core Leadership
- **Studio Director v3.5**
- **Mega Production Architect v3.5**

### Visual & Camera
- **Director of Photography (DoP) v3.5**
- **Post-Production Color Grading Supervisor v3.5**
- **Production Designer / Set Decorator v3.5**

### Story & Performance
- **Performance & Emotion Director v3.5**
- **Identity Lock Specialist v3.5**
- **Narrative Arc & Pacing Strategist v3.5**
- **Sequence Director v3.5**
- **Cinematic Sequence Extender v3.5**

### Technical & Continuity
- **Continuity & Consistency Guardian v3.5**
- **Quality Assurance Guardian v3.5**
- **Imagine Prompt Master v3.5**
- **Workflow & Quota Optimizer v3.5**

### Audio
- **Sonic Architect Native Audio Virtuoso v3.5**
- **Foley Sound Design Specialist v3.5**

### Action, VFX & SFX
- **Stunt & Action Choreographer v3.5**
- **VFX & SFX Supervisor v3.5**

### Marketing & Distribution
- **Key Art & Poster Designer v3.5**
- **Trailer & Teaser Director v3.5**
- **Localization & Subtitle Specialist v3.5**

### Specialist (Opt-in)
- **ErosForge NSFW Director v3.5** — Activate explicitly with `ACTIVATE EROSFORGE`

---

## 📁 Project Structure

```
Grok-Imagine-Cinematic-Studio/
├── references/agents/          # Authoritative Role Cards (use this)
├── agents/                     # Legacy agent definitions
├── examples/                     # 13 Production Bible templates
├── tools/                        # cinematic_studio_cli.py
├── web_ui/                       # Streamlit app
├── .github/workflows/            # CI with Role Card validation
├── MASTER_PROMPT_v3.5.md
├── Quick_Start_Guide.md
└── AGENT_INDEX.md                # Quick reference for all 22 agents
```

---

## 🔗 Useful Links

- [Quick Start Guide](Quick_Start_Guide.md)
- [Agent Index](references/agents/AGENT_INDEX.md)
- [Production Bible Template](Project_Bible_Template.md)
- [CHANGELOG](CHANGELOG.md)

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

*Grok Imagine Cinematic Studio v3.5 — Built for professional cinematic storytelling with Grok 4.3*

*Last updated: June 2026*