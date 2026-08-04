ping_history = [45, 52, 60, 150, 48, 999, 50, 42]
stable_connection=[]
for i in ping_history:
    if i == 999:
        print("Server Disconnected")
        break
    elif i>100:
        print("Lag Spike Detected")
        continue
    else:
        stable_connection.append(i)
print(stable_connection)


    