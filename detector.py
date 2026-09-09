import re

SUSPICIOUS_KEYWORDS = [
    "verify your account", "suspended", "urgent action required",
    "click here immediately", "confirm your identity", "limited time",
    "account will be permanently deleted", "unusual activity",
    "update your payment", "win a prize", "you have won",
    "act now", "restricted access", "security alert"
]

URGENCY_WORDS = ["immediately", "urgent", "24 hours", "act now", "expire", "suspended"]


def check_suspicious_links(email_text):
    urls = re.findall(r'https?://[^\s]+', email_text)
    flags = []
    for url in urls:
        if re.search(r'\.(tk|ml|ga|cf|gq)(/|$)', url):
            flags.append(f"Suspicious free/low-trust domain: {url}")
        elif re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
            flags.append(f"Raw IP address used as link: {url}")
        elif "-" in url and any(word in url.lower() for word in ["secure", "verify", "login", "account"]):
            flags.append(f"Suspicious lookalike domain pattern: {url}")
    return flags


def check_keywords(email_text):
    text_lower = email_text.lower()
    found = [kw for kw in SUSPICIOUS_KEYWORDS if kw in text_lower]
    return found


def check_urgency(email_text):
    text_lower = email_text.lower()
    found = [w for w in URGENCY_WORDS if w in text_lower]
    return found


def analyze_email(email_text):
    keyword_flags = check_keywords(email_text)
    link_flags = check_suspicious_links(email_text)
    urgency_flags = check_urgency(email_text)

    score = len(keyword_flags) * 2 + len(link_flags) * 3 + len(urgency_flags)

    print("\n--- Phishing Analysis Report ---\n")

    if keyword_flags:
        print("Suspicious phrases found:")
        for kw in keyword_flags:
            print(f"  - \"{kw}\"")
    else:
        print("Suspicious phrases found: None")

    if link_flags:
        print("\nSuspicious links found:")
        for lf in link_flags:
            print(f"  - {lf}")
    else:
        print("\nSuspicious links found: None")

    if urgency_flags:
        print("\nUrgency/pressure language found:")
        for uw in urgency_flags:
            print(f"  - \"{uw}\"")
    else:
        print("\nUrgency/pressure language found: None")

    print(f"\nRisk score: {score}")

    if score >= 6:
        verdict = "LIKELY PHISHING"
    elif score >= 3:
        verdict = "SUSPICIOUS - REVIEW CAREFULLY"
    else:
        verdict = "LIKELY LEGITIMATE"

    print(f"Verdict: {verdict}\n")


if __name__ == "__main__":
    print("=== Phishing Email Detector (Rule-Based) ===\n")
    print("Paste the email text below. Type 'END' on a new line when finished:\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    email_text = "\n".join(lines)
    analyze_email(email_text)