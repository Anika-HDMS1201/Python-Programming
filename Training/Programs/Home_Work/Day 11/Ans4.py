# username= input("Enter a username:")
# status =input("Enter the status:")
def create_user(username, status="Active"):
    return f"User: {username} | Status: {status}"
both_arg=create_user("Anika","Not Active")
only_arg=create_user("Angona")
print(both_arg)
print(only_arg)

# little bit help from chatgpt
# def create_user(username, status="Active"):
#     return f"User: {username} | Status: {status}"
# user1 = create_user("Amit", "Inactive")
# user2 = create_user("Sneha")
# print(user1)
# print(user2)