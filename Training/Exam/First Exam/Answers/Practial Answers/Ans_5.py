total_grade_points  = 0
total_credits = 12
x= input("Name:")
for i in range(4):
    y=input("Enter letter grade for Subject (O, E, A, B, C, F):")
    z=y.upper()
    match z:
        case "O":
            total_grade_points+=30
        case "E":
            total_grade_points+=27
        case "A":
            total_grade_points+=24
        case "B":
            total_grade_points+=21
        case "C":
            total_grade_points+=18
        case "F":
            total_grade_points+=0
        case _:
            print("Invalid Grade")
            continue
sgpa=(total_grade_points/ total_credits)
print(f"{x}'s final SGPA is{sgpa}")


       
    
    
    



    

