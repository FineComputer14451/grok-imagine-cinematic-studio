#!/usr/bin/env python3
"""
Grok Imagine Cinematic Studio — Streamlit Web UI v3.5.5
Aligned with 22-Agent System + Role Card Integration
"""

import streamlit as st
from datetime import datetime
import json
import os
from pathlib import Path
from openai import OpenAI

# ===================== CONFIG =====================
AGENTS_DIR = Path("../references/agents")

def get_grok_client():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        api_key = st.session_state.get("xai_api_key", "")
    if not api_key:
        return None
    return OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

# ===================== PAGE SETUP =====================
st.set_page_config(
    page_title="Grok Imagine Cinematic Studio v3.5",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cinematic Styling
st.markdown("""
<style>
    .main { background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%); }
    .stApp { color: #e0e0ff; }
    .stButton>button {
        background: linear-gradient(90deg, #6a00ff, #00d4ff);
        color: white; border: none; border-radius: 12px;
        padding: 12px 28px; font-weight: 600; transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 20px #00d4ff; }
    .section-header { color: #00d4ff; margin-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.title("🎥 Grok Imagine Cinematic Studio v3.5")
st.markdown("**22-Agent Professional Cinematic Production System** • Powered by Grok 4.3 + Full Role Cards")

# ===================== SIDEBAR =====================
with st.sidebar:
    st.header("🎬 Production Crew")
    st.success("✅ 22 Agents + Role Cards Active")

    # Full Agent List
    with st.expander("View All 22 Agents", expanded=True):
        agents = [
            "Studio Director", "Mega Production Architect",
            "Director of Photography", "Post-Production Color Grading Supervisor", "Production Designer / Set Decorator",
            "Performance & Emotion Director", "Identity Lock Specialist", "Narrative Arc & Pacing Strategist",
            "Sequence Director", "Cinematic Sequence Extender",
            "Continuity & Consistency Guardian", "Quality Assurance Guardian",
            "Imagine Prompt Master", "Workflow & Quota Optimizer",
            "Sonic Architect Native Audio Virtuoso", "Foley Sound Design Specialist",
            "Stunt & Action Choreographer", "VFX & SFX Supervisor",
            "Key Art & Poster Designer", "Trailer & Teaser Director",
            "Localization & Subtitle Specialist", "ErosForge NSFW Director (opt-in)"
        ]
        for agent in agents:
            st.markdown(f"• {agent}")

    # Role Card Browser
    st.subheader("📋 Role Cards")
    if AGENTS_DIR.exists():
        role_cards = sorted([f.stem.replace("_", " ") for f in AGENTS_DIR.glob("*.md") if "AGENT_INDEX" not in f.stem])
        selected = st.selectbox("Browse Role Card", ["Select..."] + role_cards)
        if selected != "Select...":
            card_file = AGENTS_DIR / (selected.replace(" ", "_") + ".md")
            if card_file.exists():
                with st.expander(f"📖 {selected}", expanded=True):
                    st.markdown(card_file.read_text()[:2000] + "...")
    else:
        st.warning("references/agents/ not found")

    # Memory / Character DNA Section
    st.subheader("🧠 Memory / Character DNA")
    
    # Initialize memory in session state
    if "memory" not in st.session_state:
        st.session_state.memory = {}
    
    with st.expander("Add New Memory Entry", expanded=False):
        mem_name = st.text_input("Name / Character", placeholder="Elena Voss or PROJECT_THEME")
        mem_value = st.text_area("Description / DNA", placeholder="Silver-gray hair, quiet confidence, recently exploring desire...", height=80)
        
        if st.button("💾 Save Memory Entry", use_container_width=True):
            if mem_name and mem_value:
                st.session_state.memory[mem_name] = mem_value
                st.success(f"✅ Saved: {mem_name}")
                st.rerun()
            else:
                st.warning("Please provide both Name and Description")
    
    # Display existing memory
    if st.session_state.memory:
        with st.expander(f"📋 Saved Entries ({len(st.session_state.memory)})", expanded=True):
            for name, value in st.session_state.memory.items():
                st.markdown(f"**{name}**")
                st.caption(value[:150] + "..." if len(value) > 150 else value)
            
            if st.button("🗑️ Clear All Memory", use_container_width=True):
                st.session_state.memory = {}
                st.rerun()
    else:
        st.caption("No memory entries yet. Add characters, themes, or project variables above.")

    st.divider()

    # Production Settings
    st.subheader("⚙️ Settings")
    genre = st.selectbox("Genre", ["Sci-Fi", "Psychological Horror", "Action", "Drama", "Cyberpunk", "Intimate Drama", "Thriller"])
    director = st.selectbox("Director Signature", 
        ["Denis Villeneuve", "Christopher Nolan", "David Fincher", "Roger Deakins", "Zack Snyder", "Default"])
    duration = st.slider("Duration (seconds)", 15, 180, 60, step=5)
    complexity = st.select_slider("Complexity", ["Low", "Medium", "High", "Extreme"])

    # Live Cost Simulator
    st.subheader("💰 Live Cost Estimate")
    multipliers = {"Low": 1, "Medium": 2, "High": 4, "Extreme": 7}
    est_cost = round(duration * multipliers[complexity] * 0.85, 2)
    col1, col2 = st.columns(2)
    col1.metric("Est. Cost", f"${est_cost}")
    col2.metric("Tokens", f"{int(est_cost * 1250):,}")

# ===================== MAIN AREA =====================
st.header("📝 Project Brief")

story = st.text_area(
    "Describe your cinematic vision",
    placeholder="A cyberpunk detective chases a rogue AI through neon-drenched Tokyo rooftops at midnight...",
    height=140
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Generate Master Prompt", use_container_width=True):
        if story:
            prompt = f"""# Grok Imagine Cinematic Studio v3.5 — ACTIVATED

**Project:** {story[:120]}...
**Genre:** {genre}
**Director Signature:** {director}
**Duration:** {duration}s | **Complexity:** {complexity}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

You are now running the full **22-agent** Grok Imagine Cinematic Studio v3.5 with Role Cards loaded from `references/agents/`.

Please begin by confirming activation and building a detailed Production Bible.
"""
            st.code(prompt, language="markdown")
            st.success("✅ Prompt ready to copy")
        else:
            st.warning("Please enter a description first.")

with col2:
    if st.button("🎬 Simulate Full Production", use_container_width=True):
        if story:
            with st.spinner("Engaging all 22 agents..."):
                import time
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.012)
                    progress.progress(i + 1)

            st.balloons()
            st.success("✅ Simulation Complete")

            st.subheader("📊 Structured Production Summary")

            # Generate structured simulation output
            st.markdown(f"""
**Project:** {story[:80]}...

**Genre:** {genre}  
**Director Signature:** {director}  
**Target Duration:** {duration}s  
**Complexity:** {complexity}

---

### Production Phases (Simulated)

**Phase 1: Pre-Production**
- **Mega Production Architect** → Production Bible generated
- **Identity Lock Specialist** → Character DNA locked
- **Production Designer** → World & set references created

**Phase 2: Core Production**
- **Director of Photography** + **Performance & Emotion Director** → Key sequences directed
- **Cinematic Sequence Extender** → Long-form expansion applied
- **Continuity Guardian** + **QA Guardian** → Consistency & quality checks passed

**Phase 3: Polish & Delivery**
- **Sonic Architect** + **Foley Specialist** → Audio design completed
- **Key Art Designer** + **Trailer Director** → Marketing assets generated
- **Quality Assurance Guardian** → Final 16-point QA: **PASSED**

---

### Quality Metrics
""")

            col_a, col_b, col_c, col_d = st.columns(4)
            col_a.metric("Character Consistency", "96%")
            col_b.metric("Emotional Impact", "94%")
            col_c.metric("Visual Coherence", "97%")
            col_d.metric("Overall QA Score", "✅ GO")

            st.info("This is an enhanced simulation. For real multi-agent generation, use the Grok API button below or the CLI.")
        else:
            st.warning("Enter a project description first.")

with col3:
    if st.button("📄 Export Production Bible", use_container_width=True):
        if story:
            bible = {
                "project_title": story[:80],
                "genre": genre,
                "director_signature": director,
                "target_duration_seconds": duration,
                "complexity": complexity,
                "total_agents": 22,
                "role_cards_source": "references/agents/",
                "locked_variables": {
                    "PROJECT_TITLE": story[:60],
                    "GENRE": genre,
                    "DIRECTOR_SIGNATURE": director,
                    "DURATION": f"{duration}s"
                },
                "key_agents_involved": [
                    "Mega Production Architect",
                    "Identity Lock Specialist",
                    "Director of Photography",
                    "Performance & Emotion Director",
                    "Cinematic Sequence Extender",
                    "Quality Assurance Guardian"
                ],
                "recommended_phases": [
                    "Pre-Production (Bible + Character DNA)",
                    "Core Production (Direction + Extension)",
                    "Polish & Delivery (Audio + Marketing + QA)"
                ],
                "created": datetime.now().isoformat(),
                "version": "3.5.5",
                "status": "Ready for production",
                "notes": "Generated via Grok Imagine Cinematic Studio Web UI. Use CLI for advanced memory & PDF reports."
            }
            st.download_button(
                "⬇️ Download production_bible.json",
                data=json.dumps(bible, indent=2),
                file_name="production_bible.json",
                mime="application/json"
            )
            st.success("✅ Rich Production Bible exported")
        else:
            st.warning("Describe your project first.")

# ===================== GROK API SECTION =====================
st.divider()
st.header("🔌 Live Grok 4.3 Integration")

with st.expander("API Settings", expanded=False):
    st.text_input("XAI API Key", type="password", key="xai_api_key")

if st.button("✨ Generate Prompt with Real Grok 4.3", use_container_width=True):
    if not story:
        st.warning("Please enter a project description first.")
    else:
        client = get_grok_client()
        if not client:
            st.error("Please provide your XAI API key in the sidebar settings.")
        else:
            with st.spinner("Grok 4.3 is crafting your cinematic prompt..."):
                try:
                    response = client.chat.completions.create(
                        model="grok-4.3",
                        messages=[
                            {"role": "system", "content": "You are an expert cinematic prompt engineer for the 22-agent Grok Imagine Cinematic Studio."},
                            {"role": "user", "content": f"Create a detailed cinematic prompt for: {story}. Include lighting, camera work, mood, and visual style."}
                        ],
                        max_tokens=850,
                        temperature=0.7
                    )
                    st.success("✅ Prompt generated by Grok 4.3")
                    st.text_area("Generated Prompt", response.choices[0].message.content, height=200)
                except Exception as e:
                    st.error(f"API Error: {e}")

# Footer
st.divider()
st.caption("Grok Imagine Cinematic Studio v3.5.5 • 22 Agents + Role Cards • Live Grok 4.3 API • June 2026")