def my_function(*BJP):
    print("Type:", type(BJP))
    print("First argument:", BJP[0])
    print("Second argument:", BJP[1])
    print("All arguments:", BJP)
    print(BJP[3][4])

my_function("Emil", "Tobias", "Linus", [1,5,4534,6,"Fuck You BJP MF BKL",678,7,])


def my_function2(TMC, *BJP):
    print(TMC) #lund
    for i in BJP: #BJP value chor
        print("Type:", type(BJP))
        print("First argument:", BJP[0])
        print("Second argument:", BJP[1])
        print(BJP[2][4])
        # print("All arguments:", BJP)

my_function2("Lund", "Corruption", "Gunda Gardi", [1,5,"Mewdar board",6,"Fuck You BJP MF BKL",678,7,])


def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))
largestNumber = my_function(465,574,600,52,643,654,500,75)
print(largestNumber)

# **kwargs means passing a dictionary
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


# (single_value, *[list], **{dictionary})
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")