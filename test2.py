x,y = map(int,input('점의 좌표 x, y를 입력하시오 :').split())

if x>0:
    if y>0:
        print('1사분면에 있음')
    else:
        print('4사분면에 있음')
else:
    if y>0:
        print('2사분면에 있음')
    else:
        print('3사분면에 있음')