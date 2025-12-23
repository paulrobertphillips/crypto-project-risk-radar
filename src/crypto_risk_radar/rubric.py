from __future__ import annotations
from typing import Dict, List, Tuple
from crypto_risk_radar.models import Project, RiskReport

# Simple, transparent rubric:
# - Missing basics increases risk
# - Presence of basics reduces risk
# Score 0..100 (higher riskier)

RUBRIC_WEIGHTS: Dict[str, float] = {
    "no_whitepaper": 20.0,
    "no_public_repo": 20.0,
    "anonymous_team": 15.0,
    "no_audit": 15.0,
    "unknown_chain_or_category": 10.0,
    "missing_links": 10.0,
    "very_new_project": 10.0,  # placeholder; treated via launch_date presence only at M1
}

def score_project(p: Project) -> RiskReport:
    breakdown: Dict[str, float] = {}
    notes: List[str] = []

    if not p.has_whitepaper:
        breakdown["no_whitepaper"] = RUBRIC_WEIGHTS["no_whitepaper"]
        notes.append("No whitepaper indicated.")
    if not p.has_public_repo:
        breakdown["no_public_repo"] = RUBRIC_WEIGHTS["no_public_repo"]
        notes.append("No public code repository indicated.")
    if not p.team_identified:
        breakdown["anonymous_team"] = RUBRIC_WEIGHTS["anonymous_team"]
        notes.append("Team not identified.")
    if not p.audit_reported:
        breakdown["no_audit"] = RUBRIC_WEIGHTS["no_audit"]
        notes.append("No audit reported.")

    if not p.chain or not p.category:
        breakdown["unknown_chain_or_category"] = RUBRIC_WEIGHTS["unknown_chain_or_category"]
        notes.append("Chain and/or category missing.")

    if not (p.website and p.docs_url):
        breakdown["missing_links"] = RUBRIC_WEIGHTS["missing_links"]
        notes.append("Website and/or documentation link missing.")

    if not p.launch_date:
        breakdown["very_new_project"] = RUBRIC_WEIGHTS["very_new_project"]
        notes.append("Launch date missing; treating as higher uncertainty.")

    total = sum(breakdown.values())
    total = max(0.0, min(100.0, total))

    return RiskReport(
        project_id=p.project_id,
        name=p.name,
        overall_risk_score=total,
        risk_breakdown=breakdown,
        notes=notes,
    )
