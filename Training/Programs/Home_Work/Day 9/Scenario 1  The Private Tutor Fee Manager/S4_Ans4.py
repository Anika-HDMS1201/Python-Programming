form_signups = ["amit99", "priya_d", "rahul.c", "amit99"]
direct_invites = ["sneha22", "rahul.c", "karan_x"]
revoked_user = "karan_x"

lst_1=set(form_signups)
lst_2=set(direct_invites)
all_testers=lst_1.union(lst_2)
safe=all_testers.discard("karan_x")
final_lst=list(all_testers)
print(final_lst)
