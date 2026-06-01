#!/usr/bin/env python3
"""
Grok Imagine Cinematic Studio — Enhanced Streamlit Web UI v3.5.3
With Live Grok 4.3 API Integration
"""

import streamlit as st
from datetime import datetime
import json
import os
from openai import OpenAI

# ===================== GROK API INTEGRATION =====================
def get_grok_client():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        api_key = st.session_state.get("xai_api_key", "")
    if not api_key:
        return None
    return OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1"
    )
# ================================================================

st.set_page_config(
    page_title="Grok Imagine Cinematic Studio v3.5",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cinematic CSS
st.markdown("""
<style>
    .main { background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%); }
    .stApp { color: #e0e0ff; }
    .stButton>button {
        background: linear-gradient(90deg, #6a00ff, #00d4ff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #00d4ff;
    }
    .metric-card {
        background: rgba(30, 30, 60, 0.8);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #4a4a8a;
    }
    .agent-card {
        background: #1f1f3a;
        border-radius: 10px;
        padding: 12px;
        margin: 6px 0;
        border-left: 4px solid #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎥 Grok Imagine Cinematic Studio v3.5")
st.markdown("**22-Agent Professional Film Production System** • Powered by Grok 4.3 Beta")

# Sidebar
with st.sidebar:
    st.header("🎬 Production Crew")
    st.success("✅ All 22 Agents Online")
    
    with st.expander("View All Agents"):
        agents = [
            "Studio Director", "Mega Production Architect", "Imagine Prompt Master",
            "Identity Lock Specialist", "Director of Photography", "Performance & Emotion Director",
            "VFX & SFX Supervisor", "Production Designer", "Stunt & Action Choreographer",
            "Sonic Architect", "Narrative Strategist", "Foley Specialist",
            "Sequence Director", "Continuity Guardian", "QA Guardian", "Workflow Optimizer",
            "Trailer Director", "Key Art Designer", "Localization Specialist", "Color Grading Supervisor"
        ]
        for agent in agents:
            st.markdown(f"• {agent}")

    st.divider()
    st.subheader("⚙️ Production Settings")
    
    genre = st.selectbox("Genre", ["Sci-Fi", "Psychological Horror", "Action", "Drama", "Cyberpunk", "Epic Fantasy", "Thriller"])
    director = st.selectbox("Director Signature", 
        ["Denis Villeneuve", "Christopher Nolan", "David Fincher", "Roger Deakins", "Zack Snyder", "Default Cinematic"])
    aspect_ratio = st.selectbox("Aspect Ratio", ["16:9 (Cinematic)", "2.39:1 (Anamorphic)", "9:16 (Vertical)", "1:1 (Square)"])
    quality = st.select_slider("Quality", ["Standard", "High", "Ultra", "IMAX"])
    duration = st.slider("Target Duration (seconds)", 15, 180, 60, step=5)
    complexity = st.select_slider("Complexity", ["Low", "Medium", "High", "Extreme"])

    # Live Cost Simulator
    st.subheader("💰 Live Cost Estimate")
    multipliers = {"Low": 1, "Medium": 2, "High": 4, "Extreme": 7}
    est_cost = round(duration * multipliers[complexity] * 0.85, 2)
    est_tokens = int(est_cost * 1250)
    
    col1, col2 = st.columns(2)
    col1.metric("Est. Cost", f"${est_cost}")
    col2.metric("Tokens", f"{est_tokens:,}")

# Main Content
st.header("📝 Project Brief")

story = st.text_area(
    "Describe your cinematic vision",
    placeholder="A cyberpunk detective chases a rogue AI through neon-drenched Tokyo rooftops at midnight...",
    height=150
)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Generate Master Prompt", use_container_width=True):
        if story:
            prompt = f"""# Grok Imagine Cinematic Studio v3.5 — ACTIVATED

**Project:** {story[:80]}...
**Genre:** {genre}
**Director Signature:** {director}
**Duration:** {duration}s | **Quality:** {quality}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

You are now running the full 22-agent Grok Imagine Cinematic Studio v3.5.
Begin production immediately with a Production Bible and first clip concept.
"""
            st.code(prompt, language="markdown")
            st.success("✅ Ready-to-paste prompt generated!")
        else:
            st.warning("Please enter a story description first.")

with col2:
    if st.button("🎬 Simulate Full Production", use_container_width=True):
        if story:
            with st.spinner("Engaging all 22 agents..."):
                import time
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress.progress(i + 1)
            
            st.balloons()
            st.success("✅ Production Complete!")
            
            st.subheader("📊 Production Analytics")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Consistency", "96%")
            m2.metric("Emotional Impact", "94%")
            m3.metric("Visual Coherence", "98%")
            m4.metric("QA Score", "✅ GO")
            
            st.info("All clips passed 16-point QA. Ready for final delivery.")
        else:
            st.warning("Enter a project description first.")

with col3:
    if st.button("📄 Export Production Bible", use_container_width=True):
        if story:
            bible = {
                "title": story[:50] + "...",
                "genre": genre,
                "director_signature": director,
                "duration": f"{duration}s",
                "quality": quality,
                "created": datetime.now().isoformat(),
                "agents": 22,
                "status": "Production Ready"
            }
            st.download_button(
                label="⬇️ Download production_bible.json",
                data=json.dumps(bible, indent=2),
                file_name="production_bible.json",
                mime="application/json"
            )
            st.success("Production Bible ready for download!")
        else:
            st.warning("Please describe your project first.")

# ===================== GROK API SECTION =====================
st.divider()
st.header("🔌 Grok API Integration (Live)")

col_api1, col_api2 = st.columns([2, 1])

with col_api1:
    api_key_input = st.text_input(
        "XAI API Key (or set XAI_API_KEY env var)",
        type="password",
        placeholder="xai-...",
        key="xai_api_key"
    )

with col_api2:
    if st.button("🔑 Test Connection", use_container_width=True):
        client = get_grok_client()
        if client:
            try:
                response = client.chat.completions.create(
                    model="grok-4.3",
                    messages=[{"role": "user", "content": "Say 'Connection successful'"}],
                    max_tokens=10
                )
                st.success("✅ Connected to Grok 4.3!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Connection failed: {e}")
        else:
            st.warning("Please enter your XAI API key")

# Grok-Powered Cinematic Prompt Generator
st.subheader("🎬 Generate Cinematic Prompt with Grok 4.3")

if st.button("✨ Generate with Real Grok API", use_container_width=True):
    if not story:
        st.warning("Please enter a project description above first.")
    else:
        client = get_grok_client()
        if not client:
            st.error("Please enter your XAI API key above.")
        else:
            with st.spinner("Grok 4.3 is crafting your cinematic prompt..."):
                try:
                    response = client.chat.completions.create(
                        model="grok-4.3",
                        messages=[
                            {"role": "system", "content": "You are a world-class cinematic director and prompt engineer for Grok Imagine."},
                            {"role": "user", "content": f"Create a highly detailed, cinematic prompt for this project: {story}. Include camera angles, lighting, mood, and visual style."}
                        ],
                        max_tokens=800,
                        temperature=0.8
                    )
                    generated_prompt = response.choices[0].message.content
                    
                    st.success("✅ Grok 4.3 generated prompt!")
                    st.text_area("Generated Cinematic Prompt", generated_prompt, height=200)
                    st.code(generated_prompt, language="markdown")
                    
                except Exception as e:
                    st.error(f"API Error: {str(e)}")

# Footer
st.divider()
st.caption("Grok Imagine Cinematic Studio v3.5.3 • Enhanced Web UI + Live Grok 4.3 API • June 2026 • SuperGrokPro Recommended")
