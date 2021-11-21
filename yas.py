l=["GAINT-TEDDY-BEAR","GIRAFFE","CAT","MEGA-BEAR","DOG","LION","BILLY-BEAR"]
n=input()
if n not in l:
    print("ITEM UNAVAILABLE")
else:
    l.remove(n)
    j=0
    s=""
    for i in l:
        j=j+1
        tem=str(j)
        s=s+tem+"."+i
    print(s)
