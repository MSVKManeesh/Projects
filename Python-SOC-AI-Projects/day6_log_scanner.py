with open("auth.log", "r") as f:
    lines = f.readlines()

print("=== SOC LOG SCANNER ===")
print("Total lines:", len(lines))
print("---")

failed_count = 0

for line in lines:
    if "FAILED" in line:
        print("SUSPICIOUS:", line.strip())
        failed_count = failed_count + 1

print("---")
print("Total failed attempts found:", failed_count)