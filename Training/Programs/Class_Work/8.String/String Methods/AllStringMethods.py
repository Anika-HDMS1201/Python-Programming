# examples of all string methods in Python

txt = "hello, and welcome to my world."

# 1. capitalize() - Converts the first character to upper case
print("capitalize():", txt.capitalize())

# 2. casefold() - Converts string into lower case (stronger than lower())
print("casefold():", txt.casefold())

# 3. center() - Returns a centered string
print("center():", txt.center(50, "-"))

# 4. count() - Returns the number of times a specified value occurs in a string
print("count():", txt.count("o"))

# 5. encode() - Returns an encoded version of the string
print("encode():", txt.encode())

# 6. endswith() - Returns true if the string ends with the specified value
print("endswith():", txt.endswith("."))

# 7. expandtabs() - Sets the tab size of the string
tab_txt = "H\te\tl\tl\to"
print("expandtabs():", tab_txt.expandtabs(2))

# 8. find() - Searches the string for a specified value and returns the position of where it was found
print("find():", txt.find("welcome"))

# 9. format() - Formats specified values in a string
price_txt = "For only {price:.2f} dollars!"
print("format():", price_txt.format(price=49))

# 10. format_map() - Formats specified values in a string using a dictionary
point = {'x':4, 'y':-5}
print("format_map():", '{x} {y}'.format_map(point))

# 11. index() - Searches the string for a specified value and returns the position of where it was found
print("index():", txt.index("welcome"))

# 12. isalnum() - Returns True if all characters in the string are alphanumeric
print("isalnum():", "Company12".isalnum())

# 13. isalpha() - Returns True if all characters in the string are in the alphabet
print("isalpha():", "CompanyX".isalpha())

# 14. isascii() - Returns True if all characters in the string are ascii characters
print("isascii():", "Company123".isascii())

# 15. isdecimal() - Returns True if all characters in the string are decimals
print("isdecimal():", "1234".isdecimal())

# 16. isdigit() - Returns True if all characters in the string are digits
print("isdigit():", "50800".isdigit())

# 17. isidentifier() - Returns True if the string is an identifier
print("isidentifier():", "Demo".isidentifier())

# 18. islower() - Returns True if all characters in the string are lower case
print("islower():", "hello world".islower())

# 19. isnumeric() - Returns True if all characters in the string are numeric
print("isnumeric():", "565543".isnumeric())

# 20. isprintable() - Returns True if all characters in the string are printable
print("isprintable():", "Hello! Are you #1?".isprintable())

# 21. isspace() - Returns True if all characters in the string are whitespaces
print("isspace():", "   ".isspace())

# 22. istitle() - Returns True if the string follows the rules of a title
print("istitle():", "Hello, And Welcome To My World!".istitle())

# 23. isupper() - Returns True if all characters in the string are upper case
print("isupper():", "THIS IS NOW!".isupper())

# 24. join() - Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
print("join():", "#".join(myTuple))

# 25. ljust() - Returns a left justified version of the string
print("ljust():", "banana".ljust(20, "O"))

# 26. lower() - Converts a string into lower case
print("lower():", "Hello my FRIENDS".lower())

# 27. lstrip() - Returns a left trim version of the string
print("lstrip():", "     banana     ".lstrip())

# 28. maketrans() - Returns a translation table to be used in translations
mytable = str.maketrans("h", "H")
print("maketrans() & translate():", txt.translate(mytable))

# 29. partition() - Returns a tuple where the string is parted into three parts
print("partition():", "I could eat bananas all day".partition("bananas"))

# 30. replace() - Returns a string where a specified value is replaced with a specified value
print("replace():", "I like bananas".replace("bananas", "apples"))

# 31. rfind() - Searches the string for a specified value and returns the last position of where it was found
print("rfind():", "Mi casa, su casa.".rfind("casa"))

# 32. rindex() - Searches the string for a specified value and returns the last position of where it was found
print("rindex():", "Mi casa, su casa.".rindex("casa"))

# 33. rjust() - Returns a right justified version of the string
print("rjust():", "banana".rjust(20, "O"))

# 34. rpartition() - Returns a tuple where the string is parted into three parts
print("rpartition():", "I could eat bananas all day, bananas are my favorite".rpartition("bananas"))

# 35. rsplit() - Splits the string at the specified separator, and returns a list
print("rsplit():", "apple, banana, cherry".rsplit(", "))

# 36. rstrip() - Returns a right trim version of the string
print("rstrip():", "     banana     ".rstrip())

# 37. split() - Splits the string at the specified separator, and returns a list
print("split():", "welcome to the jungle".split())

# 38. splitlines() - Splits the string at line breaks and returns a list
print("splitlines():", "Thank you for the music\nWelcome to the jungle".splitlines())

# 39. startswith() - Returns true if the string starts with the specified value
print("startswith():", txt.startswith("hello"))

# 40. strip() - Returns a trimmed version of the string
print("strip():", "     banana     ".strip())

# 41. swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("swapcase():", "Hello My Name Is PETER".swapcase())

# 42. title() - Converts the first character of each word to upper case
print("title():", "Welcome to my world".title())

# 43. upper() - Converts a string into upper case
print("upper():", "Hello my friends".upper())

# 44. zfill() - Fills the string with a specified number of 0 values at the beginning
print("zfill():", "50".zfill(10))
