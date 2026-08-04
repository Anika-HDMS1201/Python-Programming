# phone=input("Enter 10-digit phone number:")
def mask_number(phone):
    x=phone[6:10]
    return "******"+x
phone=input("Enter 10-digit phone number:")
print(mask_number(phone))