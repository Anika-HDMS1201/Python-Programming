#With the while loop we can execute a set of statements as long as a condition is true

i = 1 #starting
while i < 6: #ending
    print(i) #body
    i += 1 #jumping


#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


i = 0
while i < 6: #0-5
    i += 1 
    if i == 3:
        continue
    print(i) #1 2 4 5 6

#The else block will NOT be executed if the loop is stopped by a break statement.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")