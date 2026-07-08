logs =[
    "192.168.0.1  | INFO | Boot successful", 
    "10.0.0.5  | ERROR | Timeout connection", 
    "192.168.0.1  | INFO | User logged in", 
    "172.16.0.8  | ERROR | Database locked", 
    "10.0.0.5  | ERROR | Retry failed" 
]
error_messages=[]
trouble_ips= set()

for i in logs:
    i.split("|")
Ip_Address=i.split("|")[0]


#Message=logs[3]
#    if logs[i]=="ERROR":
print(Ip_Address)

    

