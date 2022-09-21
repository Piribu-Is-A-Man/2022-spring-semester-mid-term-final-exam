sum = 0

for i in range(1000):
    if i%3==0:
        sum=sum+i
    else:
        if i%5==0:
            sum=sum+i

print('총합 : ',sum)