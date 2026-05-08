# Examples of important string methods in Python

txt = "  Hello, Python Programming!  "

# 1. strip() - Removes any leading and trailing whitespace
print("strip():", f"'{txt.strip()}'")

# 2. lower() - Converts the string to lower case
print("lower():", txt.lower())

# 3. upper() - Converts the string to upper case
print("upper():", txt.upper())

# 4. replace() - Replaces a specified value with another value
print("replace():", txt.replace("Python", "World"))

# 5. split() - Splits the string into a list based on a separator
print("split():", txt.split(","))

# 6. find() - Searches for a specified value and returns its position
print("find():", txt.find("Python"))

# 7. count() - Returns the number of times a value occurs
print("count():", txt.count("n"))

# 8. join() - Converts elements of an iterable into a string
words = ["Python", "is", "fun"]
print("join():", " ".join(words))

# 9. startswith() - Returns True if the string starts with a specific value
print("startswith():", txt.strip().startswith("Hello"))

# 10. endswith() - Returns True if the string ends with a specific value
print("endswith():", txt.strip().endswith("!"))
