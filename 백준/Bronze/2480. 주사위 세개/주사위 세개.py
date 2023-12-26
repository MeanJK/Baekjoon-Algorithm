Anum, Bnum, Cnum = map(int, input().split())
if Anum == Bnum == Cnum:
    Hnum = 10000 + Anum * 1000
    print(Hnum)
elif Anum == Bnum:
    Hnum = 1000 + Anum * 100
    print(Hnum)
elif Bnum == Cnum:
    Hnum = 1000 + Bnum * 100
    print(Hnum)
elif Anum == Cnum:
    Hnum = 1000 + Anum * 100
    print(Hnum)
else:
    if Anum > Bnum > Cnum or Anum > Cnum > Bnum:
        Hnum = Anum * 100
        print(Hnum)
    elif Bnum > Anum > Cnum or Bnum > Cnum > Anum:
        Hnum = Bnum * 100
        print(Hnum)
    else:
        Hnum = Cnum * 100
        print(Hnum)