#!/usr/bin/env python3
"""
Grok Imagine Cinematic Studio CLI v3.5 — Full Expanded Edition
"""

import typer
import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import shutil

try:
    from fpdf import FPDF
except ImportError:
    print("⚠️  fpdf2 not installed. Run: pip install fpdf2 rich typer")
    exit(1)

app = typer.Typer(name="cinematic-studio", help="🎬 Grok Imagine Cinematic Studio v3.5 — Full Expanded CLI", add_completion=False)
console = Console()

# ... (full CLI code from package) ... 

if __name__ == "__main__":
    app()