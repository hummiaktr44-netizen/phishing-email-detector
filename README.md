# Phishing Email Detector (Rule-Based)

A Python command-line tool that analyzes email text and flags potential phishing attempts by detecting suspicious keywords, untrustworthy links, and urgency-based language patterns commonly used in social engineering attacks.

## Why this project

Phishing remains one of the most common attack vectors, relying on urgency, fear, and deceptive links to manipulate users. This tool automates the first-pass triage an analyst (or a cautious user) would do when reviewing a suspicious email, scoring risk based on three independent signal categories.

## How it works

1. Takes raw email text as input.
2. **Keyword detection** — scans for common phishing phrases (e.g. "verify your account", "suspended", "click here immediately").
3. **Link analysis** — flags suspicious link patterns: low-trust free domains (`.tk`, `.ml`, `.ga`, `.cf`, `.gq`), raw IP addresses used as links, and lookalike domains combining words like "secure" or "verify" with hyphens.
4. **Urgency detection** — flags pressure language ("immediately", "24 hours", "act now") that phishing emails use to rush victims into acting without thinking.
5. Combines all three signals into a weighted risk score and returns a verdict: LIKELY PHISHING, SUSPICIOUS - REVIEW CAREFULLY, or LIKELY LEGITIMATE.

## Example output

**Phishing email:**

![phishing result](Screenshot%202026-09-09%20223329.png)

**Legitimate email:**

![legitimate result](Screenshot%202026-09-09%20223343.png)

## Tech stack

Python, `re` (regular expressions) for pattern matching. No external API or paid service required — fully rule-based and runs offline.

## Run it yourself

```bash
python detector.py
```

## What I learned

This project reinforced how phishing emails follow recognizable patterns — urgency language, suspicious links, and specific manipulative phrases — and how a simple weighted scoring system across independent signal categories can catch a large share of phishing attempts without needing machine learning.

## Possible extensions

- Add sender domain / SPF-DKIM header analysis
- Train a lightweight ML classifier on a labeled phishing dataset for comparison
- Add a batch mode to scan multiple `.eml` files at once
