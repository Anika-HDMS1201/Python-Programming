monday_class = {"Amit", "Rohan", "Priya", "Sneha"}
friday_class = {"Priya", "Karan", "Amit", "Vikram"}
consistent_members = monday_class & friday_class
irregular_members = monday_class ^ friday_class
irregular_list = list(irregular_members)
irregular_list.sort()
print(f"Consistent members: {consistent_members}")
print(f"Sorted irregular members: {irregular_list}")