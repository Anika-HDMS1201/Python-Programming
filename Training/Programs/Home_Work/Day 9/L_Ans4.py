all_tasks = {"UI", "API", "DB", "Testing"}
completed = {"UI", "DB"}
pending= all_tasks-completed
print (f"Tasks left to do:{pending}")