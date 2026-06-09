#Task_1
weight_kg = 72
height_m = 1.75
BodyMassIndex= (weight_kg/(height_m**2))
if BodyMassIndex <= 18.5:
    print("Underweight")
    if BodyMassIndex <= 24.9:
        print("Normal")
    else:
        print("Overweight")
   

