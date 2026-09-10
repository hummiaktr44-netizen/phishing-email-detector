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
## Accuracy testing

To validate the detection logic, the tool was tested against a labeled set of 20 sample emails (10 phishing, 10 legitimate), covering common phishing patterns (urgency language, suspicious links, account-suspension threats) and typical everyday work emails.

![accuracy test result](Screenshot%202026-09-11%20015628.png)

**Result: 20/20 (100%) correctly classified** on this test set.

Note: this test set was manually constructed to represent common phishing patterns and typical legitimate emails: it demonstrates that the detection rules work correctly for the patterns they were designed to catch, but a larger, independently sourced dataset would be needed to measure real-world accuracy more rigorously.

## Possible extensions

- Add sender domain / SPF-DKIM header analysis
- Train a lightweight ML classifier on a labeled phishing dataset for comparison
- Add a batch mode to scan multiple `.eml` files at once
