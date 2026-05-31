with open("auth.log", "r") as f:
    lines = f.readlines()

print("Total log lines found:", len(lines))

for line in lines:
    print(line)