def merge_guest_lists(vip, *regular_guests):
    guest_list = [vip]
    guest_list.extend(regular_guests)
    return guest_list
result = merge_guest_lists("Anika", "Romit", "Chitta", "Deep")
print(result)

# help from chatgpt
