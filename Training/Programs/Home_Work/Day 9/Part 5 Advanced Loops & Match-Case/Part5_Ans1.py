comment = "This item is an absolute fake and a scam."
banned = ["scam", "trash", "fake"]
for i in comment:
    if i in banned:
        print("Comment flagged")
        break
    else:
        print("Comment approved")