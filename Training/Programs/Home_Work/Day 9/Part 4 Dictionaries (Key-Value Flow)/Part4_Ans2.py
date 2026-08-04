grade_points = {
    "Math": 9.0,
      "Python": 8.5, 
      "SQL": 7.0
      }
total = 0
for i in grade_points.values():
    #X= grade_points.values()
    total+= i
gpa= total /len(grade_points)
print (f"The GPA is {gpa:.2f}")

#Little help was taken for line no 7(didn't know).