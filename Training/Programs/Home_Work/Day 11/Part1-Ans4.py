#raw_string = input("Enter items separated by commas: ")

def make_list(raw_string):
    items = raw_string.split(",")
    for item in items:
        print("-", item.strip())
raw_string = input("Enter items separated by commas: ")        
make_list(raw_string)

# Little help from chatgpt

        



