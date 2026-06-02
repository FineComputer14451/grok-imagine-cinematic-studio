#!/usr/bin/env python3
"""
Grok Imagine Cinematic Studio CLI v3.5.3 — Enhanced Edition
Professional multi-agent cinematic production toolkit with Role Card integration
"""

import typer
import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.markdown import Markdown

try:
    from fpdf import FPDF
except ImportError:
    print("⚠️  fpdf2 not installed. Run: pip install fpdf2 rich typer")
    exit(1)

app = typer.Typer(
    name="cinematic-studio",
    help="🎥 Grok Imagine Cinematic Studio v3.5 — Full 22-Agent Cinematic Production CLI",
    add_completion=False,
    rich_markup_mode="rich"
)

console = Console()

# ============================================================
# CONFIG
# ============================================================
AGENTS_DIR = Path("references/agents")
PROJECT_STATE_FILE = Path(".cinematic_project_state.json")

# Director Signature Presets
DIRECTOR_SIGNATURES = {
    "nolan": "Christopher Nolan style — IMAX, practical effects, non-linear storytelling, Hans Zimmer sound",
    "villeneuve": "Denis Villeneuve — Epic scale, slow-burn tension, breathtaking visuals, Blade Runner 2047 aesthetic",
    "fincher": "David Fincher — Dark, precise, psychological, Se7en / Gone Girl tension",
    "snyder": "Zack Snyder — Hyper-stylized, slow-motion, mythic, 300 / Watchmen energy",
    "deakins": "Roger Deakins — God-tier cinematography, natural light, emotional realism",
    "default": "Cinematic excellence — emotionally powerful, technically perfect, audience-resonant"
}

AGENTS = {
    "Core Leadership": ["Studio Director v3.5", "Mega Production Architect v3.5"],
    "Visual & Camera": [
        "Director of Photography (DoP) v3.5",
        "Post-Production Color Grading Supervisor v3.5",
        "Production Designer / Set Decorator v3.5"
    ],
    "Story & Performance": [
        "Performance & Emotion Director v3.5",
        "Identity Lock Specialist v3.5",
        "Narrative Arc & Pacing Strategist v3.5",
        "Sequence Director v3.5",
        "Cinematic Sequence Extender v3.5"
    ],
    "Technical & Continuity": [
        "Continuity & Consistency Guardian v3.5",
        "Quality Assurance Guardian v3.5",
        "Imagine Prompt Master v3.5",
        "Workflow & Quota Optimizer v3.5"
    ],
    "Audio": [
        "Sonic Architect Native Audio Virtuoso v3.5",
        "Foley Sound Design Specialist v3.5"
    ],
    "Action / VFX / SFX": [
        "Stunt & Action Choreographer v3.5",
        "VFX & SFX Supervisor v3.5"
    ],
    "Marketing & Specialist": [
        "Key Art & Poster Designer v3.5",
        "Trailer & Teaser Director v3.5",
        "Localization & Subtitle Specialist v3.5",
        "ErosForge NSFW Director v3.5 (opt-in)"
    ]
}

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_role_card_path(agent_name: str) -> Path | None:
    """Find the Role Card file for a given agent name."""
    if not AGENTS_DIR.exists():
        return None
    
    for f in AGENTS_DIR.glob("*.md"):
        if agent_name.lower().replace(" ", "_") in f.stem.lower() or f.stem.lower() in agent_name.lower().replace(" ", "_"):
            return f
    return None

def load_project_state() -> dict:
    if PROJECT_STATE_FILE.exists():
        return json.loads(PROJECT_STATE_FILE.read_text())
    return {"project": None, "characters": {}, "locked_variables": {}}

def save_project_state(state: dict):
    PROJECT_STATE_FILE.write_text(json.dumps(state, indent=2))

# ============================================================
# COMMANDS
# ============================================================

@app.command()
def status():
    """Show current studio status"""
    console.print(Panel.fit(
        "[bold cyan]🎥 Grok Imagine Cinematic Studio v3.5[/bold cyan]\n"
        "[green]Status:[/green] Enhanced CLI Active\n"
        "[green]Agents:[/green] 22 Online\n"
        "[green]Role Cards:[/green] Loaded from references/agents/\n"
        "[green]Mode:[/green] Production Ready",
        title="Studio Status",
        border_style="cyan"
    ))

@app.command()
def version():
    """Show CLI version"""
    console.print("[bold]cinematic-studio[/bold] v3.5.3-enhanced (June 2026)")

@app.command(name="list-agents")
def list_agents():
    """List all 22 agents grouped by category"""
    table = Table(title="🎬 Grok Imagine Cinematic Studio — 22 Agents", box=box.ROUNDED)
    table.add_column("Category", style="bold cyan", no_wrap=True)
    table.add_column("Agents", style="white")

    for category, agents in AGENTS.items():
        agent_list = "\n".join([f"• {a}" for a in agents])
        table.add_row(category, agent_list)

    console.print(table)
    console.print("\n[italic dim]Total: 22 specialized agents ready for production[/italic dim]")

@app.command(name="list-role-cards")
def list_role_cards():
    """List all available Role Cards in references/agents/"""
    if not AGENTS_DIR.exists():
        console.print("[red]references/agents/ directory not found[/red]")
        return

    cards = sorted(AGENTS_DIR.glob("*.md"))
    table = Table(title="📋 Available Role Cards", box=box.SIMPLE)
    table.add_column("Role Card", style="cyan")
    table.add_column("File", style="dim")

    for card in cards:
        table.add_row(card.stem.replace("_", " "), str(card))

    console.print(table)
    console.print(f"\n[green]Total Role Cards:[/green] {len(cards)}")

@app.command(name="show-role-card")
def show_role_card(
    agent: str = typer.Argument(..., help="Agent name or partial match (e.g. 'Identity Lock' or 'ErosForge')")
):
    """Display a specific Role Card"""
    card_path = get_role_card_path(agent)
    
    if not card_path or not card_path.exists():
        console.print(f"[red]Role Card not found for:[/red] {agent}")
        return

    content = card_path.read_text()
    console.print(Panel(Markdown(content[:3000]), title=f"📋 {card_path.stem}", border_style="blue", expand=False))

@app.command(name="generate-prompt")
def generate_prompt(
    story: str = typer.Argument(..., help="Your story, scene, or project description"),
    signature: str = typer.Option("default", "--signature", "-s", help="Director style"),
    output: str = typer.Option(None, "--output", "-o", help="Save to file")
):
    """Generate a high-quality ready-to-paste prompt"""
    sig_text = DIRECTOR_SIGNATURES.get(signature.lower(), DIRECTOR_SIGNATURES["default"])

    prompt = f"""# Grok Imagine Cinematic Studio v3.5 — ACTIVATED

**Project:** {story}
**Director Signature:** {sig_text}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

You are now running the full **22-agent** Grok Imagine Cinematic Studio v3.5 with complete Role Cards loaded from `references/agents/`.

Please begin by:
1. Confirming activation
2. Asking for my first creative decision, or
3. Immediately building a detailed Production Bible using the Mega Production Architect

Use the full power of the 22 specialized agents with their Role Cards.
"""

    if output:
        Path(output).write_text(prompt)
        console.print(f"[green]✅ Prompt saved to[/green] {output}")
    else:
        console.print(Panel(prompt, title="📜 Ready-to-Paste Prompt", border_style="green"))

@app.command(name="cost-simulate")
def cost_simulate(
    duration: int = typer.Option(60, "--duration", "-d", help="Target duration in seconds"),
    complexity: str = typer.Option("medium", "--complexity", "-c", help="low / medium / high / extreme")
):
    """Estimate generation cost and quota usage"""
    multipliers = {"low": 1, "medium": 2, "high": 4, "extreme": 7}
    base_cost = duration * multipliers.get(complexity, 2) * 0.8

    table = Table(title="💰 Estimated Production Cost", box=box.SIMPLE)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="bold green")

    table.add_row("Duration", f"{duration}s")
    table.add_row("Complexity", complexity.title())
    table.add_row("Estimated Tokens", f"~{int(base_cost * 1200):,}")
    table.add_row("Est. Cost (USD)", f"${base_cost:.2f}")

    console.print(table)

@app.command(name="create-bible")
def create_bible(
    title: str = typer.Argument(..., help="Project title"),
    genre: str = typer.Option("Cinematic", "--genre", "-g"),
    output: str = typer.Option("production_bible.json", "--output", "-o")
):
    """Generate a more complete Production Bible"""
    state = load_project_state()
    
    bible = {
        "title": title,
        "genre": genre,
        "created": datetime.now().isoformat(),
        "version": "3.5.1",
        "studio": "Grok Imagine Cinematic Studio v3.5",
        "locked_variables": {
            "PROJECT_TITLE": title,
            "GENRE": genre,
            "DIRECTOR_SIGNATURE": "Cinematic excellence"
        },
        "agents_active": 22,
        "status": "Ready for production",
        "role_cards_loaded": str(AGENTS_DIR) if AGENTS_DIR.exists() else "Not found"
    }

    Path(output).write_text(json.dumps(bible, indent=2))
    
    state["project"] = bible
    save_project_state(state)

    console.print(f"[green]✅ Production Bible created and saved to project state:[/green] {output}")

@app.command()
def memory(
    action: str = typer.Argument(..., help="add / list / load"),
    name: str = typer.Option(None, "--name", "-n", help="Character or variable name"),
    value: str = typer.Option(None, "--value", "-v", help="Value to store")
):
    """Manage project memory and character DNA"""
    state = load_project_state()

    if action == "add":
        if not name or not value:
            console.print("[red]Please provide --name and --value[/red]")
            return
        state["characters"][name] = value
        save_project_state(state)
        console.print(f"[green]✅ Saved memory for[/green] {name}")

    elif action == "list":
        if not state.get("characters"):
            console.print("[yellow]No memory entries yet[/yellow]")
            return
        table = Table(title="🧠 Project Memory")
        table.add_column("Name", style="cyan")
        table.add_column("Value", style="white")
        for k, v in state["characters"].items():
            table.add_row(k, str(v)[:80])
        console.print(table)

    elif action == "load":
        if name and name in state.get("characters", {}):
            console.print(Panel(state["characters"][name], title=f"Memory: {name}"))
        else:
            console.print("[yellow]Memory entry not found[/yellow]")

    else:
        console.print("[red]Unknown action. Use: add / list / load[/red]")

@app.command(name="report")
def report(
    output: str = typer.Option("production_report.pdf", "--output", "-o", help="Output PDF filename")
):
    """Generate a basic PDF production report"""
    state = load_project_state()
    project = state.get("project", {})

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, "Grok Imagine Cinematic Studio — Production Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 8, f"Project: {project.get('title', 'Untitled')}", ln=True)
    pdf.cell(0, 8, f"Genre: {project.get('genre', 'N/A')}", ln=True)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 8, "Status: Production in progress with 22-agent studio", ln=True)

    pdf.output(output)
    console.print(f"[green]✅ PDF Report generated:[/green] {output}")

@app.command(name="validate")
def validate():
    """Run basic local validation (similar to CI)"""
    console.print("[bold]🔍 Running local validation...[/bold]\n")

    issues = 0

    if not AGENTS_DIR.exists():
        console.print("[red]❌ references/agents/ directory missing[/red]")
        issues += 1
    else:
        card_count = len(list(AGENTS_DIR.glob("*.md")))
        console.print(f"[green]✅ Found {card_count} Role Cards in references/agents/[/green]")

    core_files = ["MASTER_PROMPT_v3.5.md", "README.md", "Quick_Start_Guide.md"]
    for f in core_files:
        if Path(f).exists():
            console.print(f"[green]✅ {f} present[/green]")
        else:
            console.print(f"[yellow]⚠️  {f} missing[/yellow]")
            issues += 1

    if issues == 0:
        console.print("\n[bold green]✅ Validation passed[/bold green]")
    else:
        console.print(f"\n[yellow]Validation completed with {issues} issues[/yellow]")

@app.command()
def activate():
    """Print the official activation command"""
    console.print(Panel(
        "[bold]Activate Grok Imagine Cinematic Studio v3.5[/bold]\n\n"
        "Load the master prompt first, then paste the activation command.",
        title="🚀 Activation",
        border_style="magenta"
    ))

if __name__ == "__main__":
    app()