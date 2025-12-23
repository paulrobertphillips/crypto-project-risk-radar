from __future__ import annotations
import json
from pathlib import Path
from typing import List
from crypto_risk_radar.models import Project

def load_projects_json(path: str | Path) -> List[Project]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing input file: {p}")

    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expected a JSON list of project objects.")

    projects: List[Project] = []
    for obj in data:
        if not isinstance(obj, dict):
            raise ValueError("Each project must be a JSON object.")
        projects.append(Project(**obj))
    return projects
