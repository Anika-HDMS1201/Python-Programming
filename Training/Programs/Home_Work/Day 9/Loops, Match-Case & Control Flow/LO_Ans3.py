battery = 100
while battery>0:
    battery-=15
    print(battery)
    if battery<20:
        print("Plug in charger")
        break
    