# Labeled test set: (email_text, actual_label)
# actual_label: "PHISHING" or "LEGITIMATE"

TEST_EMAILS = [
    ("Dear Customer, Your account has been suspended due to unusual activity. Click here immediately to verify your identity within 24 hours or your account will be permanently deleted. http://secure-bank-verify.tk/login Regards, Security Team", "PHISHING"),
    ("URGENT: Your payment could not be processed. Update your payment information immediately to avoid service suspension. Click here: http://192.168.55.21/pay", "PHISHING"),
    ("Congratulations! You have won a prize in our monthly draw. Act now, limited time offer, click here to claim: http://free-prize-claim.ml/win", "PHISHING"),
    ("Security Alert: Unusual activity detected on your account. Confirm your identity immediately or access will be restricted. http://account-secure-verify.ga/confirm", "PHISHING"),
    ("Your account will be permanently deleted unless you verify your identity within 24 hours. Click here now: http://verify-now-account.cf/id", "PHISHING"),
    ("Dear User, urgent action required: your mailbox is full and will be suspended. Click here immediately to restore access. http://mail-restore-secure.tk/fix", "PHISHING"),
    ("You have won a prize! This is a limited time offer, act now to claim your reward before it expires. http://claim-reward-now.gq/win", "PHISHING"),
    ("Restricted access warning: your account shows unusual activity. Verify your identity immediately to avoid permanent suspension. http://identity-check-secure.tk/verify", "PHISHING"),
    ("URGENT security alert - update your payment details immediately or your subscription will be suspended within 24 hours. http://update-payment-now.ml/pay", "PHISHING"),
    ("Your account has unusual activity. Act now and confirm your identity immediately to avoid deletion. http://172.16.254.1/confirm", "PHISHING"),
    ("Hi Sarah, just a reminder that our team meeting is scheduled for tomorrow at 10 AM in Conference Room B. Please bring your project updates. Thanks, John", "LEGITIMATE"),
    ("Hello, attached is the invoice for last month's services. Let us know if you have any questions. Best regards, Accounts Team", "LEGITIMATE"),
    ("Hi team, the project deadline has been moved to next Friday. Please update your task lists accordingly. Thanks, Manager", "LEGITIMATE"),
    ("Dear colleague, please find attached the minutes from yesterday's meeting for your review. Regards, Secretary", "LEGITIMATE"),
    ("Hi, just checking in to see how the report is coming along. Let me know if you need any help. Cheers, Alex", "LEGITIMATE"),
    ("Hello, your order has been shipped and should arrive within 5-7 business days. Thank you for shopping with us.", "LEGITIMATE"),
    ("Hi, reminder that the office will be closed on Monday for the public holiday. Regular hours resume Tuesday.", "LEGITIMATE"),
    ("Dear student, your assignment submission has been received successfully. Grades will be posted within two weeks.", "LEGITIMATE"),
    ("Hi, thanks for attending today's webinar. The recording and slides are attached for your reference.", "LEGITIMATE"),
    ("Hello, this is a reminder that your library books are due for return next week. Thank you.", "LEGITIMATE"),
]