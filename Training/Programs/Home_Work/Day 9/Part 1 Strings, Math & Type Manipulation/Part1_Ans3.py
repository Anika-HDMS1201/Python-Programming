raw_num = "9876543210"
firstnums=raw_num[0:4]
middlenums=raw_num[4:7]
lastnums=raw_num[7:]
lstfinal=[firstnums,middlenums,lastnums]
x="-".join(lstfinal)
print(x)
"""
Another method simple and efficient
raw_num = "9876543210"
lstfinal = [raw_num[0:4],raw_num[4:7],raw_num[7:]]
x="-".join(lstfinal)
print(x)
"""
