#이중 for문을 사용하여 숫자를 입력 받기

num = int(input('숫자를 입력하세요 : '))

for i in range(num):
    for j in range(num-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()
