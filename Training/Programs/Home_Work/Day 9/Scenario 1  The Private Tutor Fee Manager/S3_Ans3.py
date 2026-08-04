raw_sql_data = " 101|Amit | MCA , 102 | Sneha|MBA , 103|Rohan|BCOM "

id_no=[]
name=[]
course=[]
sql_data1=raw_sql_data.strip()
sql_data2=sql_data1.split(",")
# print(sql_data2)
for i in sql_data2:
    # x=i.split("|")
    id_no =i.split("|")[0]
    name=i.split("|")[1]
    course=i.split("|")[2]

    print(f"ID: {id_no}, Name: {name}, Course: {course}")

#print("============================")

# raw_sql_data = " 101|Amit | MCA , 102 | Sneha|MBA , 103|Rohan|BCOM "

# sql_data1 = raw_sql_data.strip()
# sql_data2 = sql_data1.split(",")

# for i in sql_data2:

#     parts = i.split("|")

#     id_no = parts[0].strip()
#     name = parts[1].strip()
#     course = parts[2].strip()

#     print(f"ID: {id_no}, Name: {name}, Course: {course}")


    
