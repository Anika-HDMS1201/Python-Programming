logs = [ 
    "192.168.0.1  | INFO | Boot successful", 
    "10.0.0.5  | ERROR | Timeout connection", 
    "192.168.0.1  | INFO | User logged in", 
    "172.16.0.8  | ERROR | Database locked", 
    "10.0.0.5  | ERROR | Retry failed" 
] 
error_messages = []
trouble_ips  = set() #MF

for i in logs:
    parts = i.split("|")#ip address / log type / Message
    ip_address = parts[0].strip()
    log_type = parts[1].strip()
    message = parts[2].strip()
    if log_type == "ERROR" :
        error_messages.append(message)
        trouble_ips.add(ip_address)
    elif log_type == "INFO":
        pass
print(f"Trouble IPs : {trouble_ips}") #MF
print(f"Error Message : {error_messages}")