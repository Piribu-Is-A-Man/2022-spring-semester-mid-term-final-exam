num=1
sum=0

while num<1001:
    if num%3==0:
        sum=sum+num
    num+=1

print('1부터 1000까지의 자연수 중 3의배수의 합 : ',sum)
