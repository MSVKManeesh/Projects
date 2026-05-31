failed_logins = 1
ip_address = "10.52.4.100"

if failed_logins > 3:
    print("ALERT: Brute Force Attack Detected!")
    print("Suspicious IP:", ip_address)
    print("Failed attempts:", failed_logins)
    print("Action: Block this IP immediately!")
else:
    print("All clear. No threat from", ip_address)