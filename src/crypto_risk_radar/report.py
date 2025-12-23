from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable
from crypto_risk_radar.models import RiskReport

def save_reports_json(reports: Iterable[RiskReport], path: str | Path) -> None:
    out = [
        {
            "project_id": r.project_id,
            "name": r.name,
            "overall_risk_score": r.overall_risk_score,
            "risk_breakdown": r.risk_breakdown,
            "notes": r.notes,
        }
        for r in reports
    ]
    Path(path).write_text(json.dumps(out, indent=2), encoding="utf-8")
