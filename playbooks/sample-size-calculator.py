#!/usr/bin/env python3
import math
import sys

def calculate_sample_size(baseline_cvr, mde, power=0.80, alpha=0.05):
    # Standard normal deviates
    z_alpha = 1.96 # 95% confidence
    z_beta = 0.84  # 80% power
    p1 = baseline_cvr
    p2 = baseline_cvr * (1 + mde)
    p_bar = (p1 + p2) / 2
    n = ((z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / ((p2 - p1) ** 2)
    return math.ceil(n)

if __name__ == "__main__":
    n = calculate_sample_size(0.025, 0.15)
    print(f"Required Sample Size Per Variant (Baseline 2.5%, MDE 15%): {n:,} visitors")
