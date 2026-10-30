# CRO Experiment Prioritization & Statistical Power Scorecard

> Prioritize high-impact A/B tests and calculate required sample sizes and test durations before writing a single line of code.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a professional CRO experiment prioritization system: 1) Extended ICE/PIE scoring framework incorporating Traffic Feasibility and Technical Effort, 2) Python sample size calculator (`calc_power.py`) computing required sample sizes and test duration (days) given baseline conversion rate and desired MDE, 3) Complete Markdown experiment planning template.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `examples/ecommerce-experiment-roadmap.md`
- `examples/sample_cro_backlog.csv`
- `framework/prioritization-rubric.md`
- `LICENSE`
- `models/cro-experiment-backlog.xlsx`
- `playbooks/sample-size-calculator.py`
- `README.md`
- `src/calc_power.py`
- `templates/experiment-design-document.md`
- `templates/ice-pie-scoring-model.md`
- `tests/test_calculator.py`
- `tests/test_power.py`
- `tests/test_sample_size.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/calc_power.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "cro",
  "repository": "cro-experiment-prioritization-scorecard",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Statistical Power Requirements:** Enforces minimum sample size calculation before launching split tests, preventing tests with insufficient statistical power.
- **ICE vs P.I.E. Hybrid Scoring:** Combines Potential, Importance, and Ease with regional implementation risk multipliers.
- **Guardrail Metric Tracking:** Prioritization models require explicit guardrail metrics (e.g. Return Rate, Unsubscribe Rate) to prevent destructive short-term conversion gains.

---

## 📚 Primary Documentation & Verifiable References

- [Evan Miller: Sample Size Calculator for A/B Testing](https://www.evanmiller.org/ab-testing/sample-size.html) - Mathematical formulation for minimum sample sizes in binomial split testing.
- [Sean Ellis: ICE Experiment Prioritization Framework](https://growthhackers.com/) - Standard methodology for scoring Impact, Confidence, and Ease in growth experimentation.
- [WiderFunnel: The PIE Framework for CRO Prioritization](https://widerfunnel.com/) - Prioritization matrix for enterprise conversion optimization programs.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
