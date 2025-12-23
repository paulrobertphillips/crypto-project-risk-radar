from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass(frozen=True)
class Project:
    project_id: str
    name: str
    chain: str                      # e.g., "Ethereum", "Solana", "Base"
    category: str                   # e.g., "DeFi", "L2", "Infra", "Meme", "NFT"
    website: Optional[str] = None
    docs_url: Optional[str] = None
    repo_url: Optional[str] = None
    launch_date: Optional[str] = None  # ISO string for simplicity

    # Lightweight, educational fields (dummy-friendly)
    has_whitepaper: bool = False
    has_public_repo: bool = False
    team_identified: bool = False
    audit_reported: bool = False

    # Optional numeric hints (can remain None until later milestones)
    tvl_usd: Optional[float] = None
    fdv_usd: Optional[float] = None
    volume_24h_usd: Optional[float] = None

@dataclass(frozen=True)
class RiskReport:
    project_id: str
    name: str
    overall_risk_score: float            # 0..100 (higher = riskier)
    risk_breakdown: Dict[str, float]     # factor -> score contribution
    notes: List[str]                     # human-readable explanations
