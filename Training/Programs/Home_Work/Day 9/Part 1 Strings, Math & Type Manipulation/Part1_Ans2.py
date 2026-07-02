flight = "03h45m"
x= int(flight[0:2]) 
y= int(flight[3:5])
z= int((x*60)+y)
#print(f"Total flight time:{z} mins.")
print("Total flight time:", z, "mins")