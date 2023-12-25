Anum = int(input())
if (Anum % 4 == 0 and Anum % 100 != 0) or Anum % 400 == 0:
    print("1")
else:
    print("0")