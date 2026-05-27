thistuple = ("apple", "banana", "cherry")
for x in thistuple: #simple
  print(x)



thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #Using indexing
  print(thistuple[i])



thistuple = ("apple", "banana", "cherry")
i = 0 #starting index
while i < len(thistuple): #using while loop {i'll come to that} ending index
  print(thistuple[i],end=" ")
  i = i + 1 #incremental value {mandatory}

print()
x = 1
xx=1
while x<=10:
  print(xx)
  xx+=1
#   x+=1