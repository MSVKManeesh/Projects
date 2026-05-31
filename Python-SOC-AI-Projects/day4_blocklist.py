blocklist = ["192.168.1.10", "10.0.0.5", "172.16.0.99"]

print("Original Blocklist:", blocklist)
print("Total:", len(blocklist))
print("---")

# Add a new suspicious IP
blocklist.append("192.168.1.55")
print("After adding new IP:", blocklist)
print("Total:", len(blocklist))
print("---")

# Remove a cleared IP
blocklist.remove("10.0.0.5")
print("After removing cleared IP:", blocklist)
print("Total:", len(blocklist))
print("---")

# Check if an IP is in the blocklist
check_ip = "192.168.1.10"
if check_ip in blocklist:
    print("ALERT:", check_ip, "is in the blocklist!!")
else:
    print("Safe:", check_ip, "is not blocked.")