role = "User"
age = 20
match role:
    case "user" if age>=18:
        print("Adult User")
    case _:
        print("Restricted")
            