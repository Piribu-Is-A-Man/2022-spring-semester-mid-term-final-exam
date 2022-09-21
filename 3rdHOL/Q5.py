scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
count=0

for i in range(10):
    sum+=scores[i]
    count+=1

avg = sum/count

print('평균 : ',avg)