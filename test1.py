a,b,c = map(int,input('세 정수를 입력하세요 :').split())

#경우의수 6가지
if a<b:
    if a<c: 
        if b<c:
            print(a,b,c)
        else:
            print(a,c,b)
    else : 
        print(c,a,b)
else: #b<a
    if a<c:
        print(b,a,c)
    else: #c<a
        if b<c:
            print(b,c,a)
        else:
            print(c,b,a)


