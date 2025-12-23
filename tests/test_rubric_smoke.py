from crypto_risk_radar.models import Project
from crypto_risk_radar.rubric import score_project

def test_score_is_deterministic():
    p = Project(project_id="x", name="X", chain="Ethereum", category="DeFi")
    r1 = score_project(p)
    r2 = score_project(p)
    assert r1.overall_risk_score == r2.overall_risk_score

def test_score_range():
    p = Project(project_id="y", name="Y", chain="", category="")
    r = score_project(p)
    assert 0.0 <= r.overall_risk_score <= 100.0
