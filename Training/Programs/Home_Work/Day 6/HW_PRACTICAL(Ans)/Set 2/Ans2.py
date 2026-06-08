logs = ["[INFO] App started", "[ERROR] Null reference","[WARNING] UI lag", "[ERROR] Connection timeout"]
logs2 = []
for x in logs:
    if "[ERROR]" in x:
        logs2.append(x)
        print(x)