"""data = "Aritra:85,Sneha:92, Rohan:34,Priya:78"
x=data.split(",")
for i in x:
    print([i])"""


data = "Aritra:85, Sneha:92, Rohan:34, Priya:78"

students = []
scores = []

items = data.split(", ")

for item in items:
    name, score_str = item.split(":") #new for U

    students.append(name)
    scores.append(int(score_str))

print("students =", students)
print("scores =", scores)
