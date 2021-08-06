from random import *
a=1
count = 0
l = [randrange(5,51) for i in range(1,51)]
for i in l:
    print("{}번째 손님 (소요시간 : {}분)".format(a,l[i]))
    a+=1
    if(5<=l[i]<=15):
        count +=1
print("총 탑승 승객: %d"%count)