cart = {}
subtotal = 0
while True: #infinite loop
    item = input("Enter item name (or type 'pay' to finish): ")
    if item.lower() == "pay" :
        break
    else :
        price = float(input("Price : "))
        cart[item] = price #if item name is not present then create a new one
        subtotal += price #sum of subtotal + price where subtotal previous value +  new value + price
gst = subtotal * (18/100)
total = subtotal + gst

print(f"Subtotal : {subtotal:.2f}")
print(f"GST(18%) {gst:.2f}")
print(f"Final Total : {total:.2f}")