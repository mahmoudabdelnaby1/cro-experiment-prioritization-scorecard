"""
CRO Experiment Statistical Power & Sample Size Calculator
Zero-dependency statistical power calculations for proportion A/B tests:
- Computes required sample size per variant for two-tailed z-test
- Accounts for baseline conversion rate, relative MDE (Minimum Detectable Effect)
- Calculates estimated test duration based on daily traffic and allocation
"""
import math
import json
import argparse
from typing import Dict, Any

# Standard z-critical values
Z_ALPHA_HALF = 1.96  # alpha = 0.05 (95% confidence)
Z_BETA = 0.842      # beta = 0.20 (80% power)

def calculate_ab_sample_size(baseline_cr: float, relative_mde: float, daily_traffic: int, alpha_confidence: float = 0.95, power: float = 0.80) -> Dict[str, Any]:
    p1 = baseline_cr
    p2 = p1 * (1.0 + relative_mde)
    
    if p1 <= 0 or p1 >= 1 or p2 <= 0 or p2 >= 1:
        return {"error": "Conversion rates must be strictly between 0 and 1"}
        
    p_bar = (p1 + p2) / 2.0
    
    # Evan Miller two-sample proportion formula approximation
    z_a = 1.96 if alpha_confidence == 0.95 else 2.576
    z_b = 0.842 if power == 0.80 else 1.282
    
    numerator = ((z_a * math.sqrt(2 * p_bar * (1 - p_bar))) + (z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))) ** 2
    denominator = (p2 - p1) ** 2
    
    sample_size_per_variant = math.ceil(numerator / denominator)
    total_required = sample_size_per_variant * 2
    
    # Calculate days required
    days_required = math.ceil(total_required / daily_traffic) if daily_traffic > 0 else 999
    
    return {
        "baseline_cr_pct": round(baseline_cr * 100, 2),
        "target_cr_pct": round(p2 * 100, 2),
        "relative_mde_pct": round(relative_mde * 100, 1),
        "sample_size_per_variant": sample_size_per_variant,
        "total_sample_size": total_required,
        "daily_traffic": daily_traffic,
        "estimated_duration_days": days_required,
        "feasibility": "FEASIBLE" if days_required <= 28 else "TOO_SLOW_RECOMMEND_HIGHER_MDE"
    }

def main():
    res = calculate_ab_sample_size(0.03, 0.15, 2500)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
