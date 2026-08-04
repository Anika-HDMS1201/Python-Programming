stock = [["Laptops", 5], ["Mice", 0], ["Keyboards", 12], ["Webcams", 0]]
for i in range(len(stock)):
    if stock[i][1]==0:
        stock[i][1]="RESTOCK"
        print(stock)     
    