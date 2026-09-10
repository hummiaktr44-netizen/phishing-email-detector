from detector import check_keywords, check_suspicious_links, check_urgency
from test_emails import TEST_EMAILS


def predict(email_text):
    keyword_flags = check_keywords(email_text)
    link_flags = check_suspicious_links(email_text)
    urgency_flags = check_urgency(email_text)

    score = len(keyword_flags) * 2 + len(link_flags) * 3 + len(urgency_flags)

    if score >= 6:
        return "PHISHING"
    elif score >= 3:
        return "PHISHING"  # count "suspicious" as phishing for this binary test
    else:
        return "LEGITIMATE"


def run_test():
    correct = 0
    total = len(TEST_EMAILS)
    results = []

    for email_text, actual_label in TEST_EMAILS:
        predicted_label = predict(email_text)
        is_correct = predicted_label == actual_label
        if is_correct:
            correct += 1
        results.append((actual_label, predicted_label, is_correct))

    print("=== Phishing Detector Accuracy Test ===\n")
    print(f"{'Actual':<12} {'Predicted':<12} {'Result'}")
    print("-" * 36)
    for actual, predicted, is_correct in results:
        mark = "CORRECT" if is_correct else "WRONG"
        print(f"{actual:<12} {predicted:<12} {mark}")

    accuracy = (correct / total) * 100
    print("-" * 36)
    print(f"\nAccuracy: {correct}/{total} = {accuracy:.1f}%")


if __name__ == "__main__":
    run_test()