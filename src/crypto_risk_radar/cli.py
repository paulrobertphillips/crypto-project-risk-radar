from __future__ import annotations
import argparse
from crypto_risk_radar.io import load_projects_json
from crypto_risk_radar.rubric import score_project
from crypto_risk_radar.report import save_reports_json

def main() -> None:
    parser = argparse.ArgumentParser(description="Crypto Project Risk Radar (educational; not financial advice)")
    parser.add_argument("--input", required=True, help="Path to projects JSON")
    parser.add_argument("--output", default="results/reports.json", help="Path to output JSON")
    args = parser.parse_args()

    projects = load_projects_json(args.input)
    reports = [score_project(p) for p in projects]
    save_reports_json(reports, args.output)

    # Minimal CLI feedback (keep prints out of core logic)
    print(f"Wrote {len(reports)} reports to {args.output}")

if __name__ == "__main__":
    main()
