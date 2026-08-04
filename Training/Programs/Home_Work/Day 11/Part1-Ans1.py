# full_name=input("Enter Full Name:")
def  clean_name(full_name):
    clean = full_name.strip().title()
    first_name=clean.split(" ")[0]
    return first_name
full_name=input("Enter Full Name:")
print(clean_name(full_name))