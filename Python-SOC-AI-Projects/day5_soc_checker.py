def check_ip(ip_address, failed_logins):
    print("Checking IP:", ip_address)
    if failed_logins > 3:
        print("ALERT: Brute Force Detected!!")
        print("Failed attempts:", failed_logins)
        print("Action: Block", ip_address, "immediately!!")
    else:
        print("Safe. No threat detected.")
    print("---")

check_ip("192.168.1.10", 7)
check_ip("10.0.0.5", 1)
check_ip("172.16.0.99", 5)