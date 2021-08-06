min = 2
max = 10
peo = 100
memo = {}

def a(b,c):
    key = str([b,c])
    if key in memo:
        return memo[key]
    elif b<0:
        return 0
    elif b==0:
        return 1
    #재귀처리
    count = 0
    for i in range(c,max+1):
        count += a(b-i,i)

    memo[key] = count
    return count
print(a(peo,min))

#이건 잘 모르겠다. 다시 한 번 생각해봐야한다.