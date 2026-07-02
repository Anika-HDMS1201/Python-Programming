ext = ".py"
match ext:
    case ".py":
        print("Python")
    case ".cs":
        print("C#")
    case _:
        print("Unknown File")