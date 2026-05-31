incident = {
    "ip": "192.168.1.10",
    "type": "Brute Force",
    "failed_logins": 7,
    "risk": "HIGH",
    "action": "Block immediately"
}

print("=== SOC INCIDENT REPORT ===")
print("IP Address:", incident["ip"])
print("Attack Type:", incident["type"])
print("Failed Logins:", incident["failed_logins"])
print("Risk Level:", incident["risk"])
print("Action:", incident["action"])
print("===========================")