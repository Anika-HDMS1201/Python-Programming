voters = ["V1", "V2", "V1", "V3", "V2"]
clean_list = []
seen = set()
for i in voters:
     if i not in seen:
          clean_list.append(i)
     seen.add(i)
print(clean_list)