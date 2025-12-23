import json
from pathlib import Path
from crypto_risk_radar.io import load_projects_json

def test_load_projects_json(tmp_path: Path):
    payload = [{"project_id": "a", "name": "A", "chain": "Ethereum", "category": "DeFi"}]
    p = tmp_path / "projects.json"
    p.write_text(json.dumps(payload), encoding="utf-8")
    projects = load_projects_json(p)
    assert len(projects) == 1
    assert projects[0].project_id == "a"
