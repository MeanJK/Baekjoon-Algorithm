Anum, Bnum = int(input()), int(input())
if Anum > 0 and Bnum > 0:
    print("1")
elif Anum < 0 and Bnum > 0:
    print("2")
elif Anum < 0 and Bnum < 0:
    print("3")
else:
    print("4")