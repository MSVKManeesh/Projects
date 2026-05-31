ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "192.168.1.10"]
suspicious_ip = "192.168.1.10"

for ip in ips:
    print("Checking IP:", ip)
    if ip == suspicious_ip:
        print("ALERT: Suspicious IP Found!", ip)
        print("Action: Block immediately!")
    else:
        print("Safe. No threat detected.")
    print("---")