max = 0
a=0
b=0
for i in range(1,100):
    j = 100 - i
    if max < i*j:
        a=i
        b=j
        max = a*b




print(a,b,max)