number = [1,2,3,4,5,6]

def reverse(list):
    a=[]
    for i in list:
        a.append(list[(len(list)-i)])
    yield a

print(next(reverse(number)))
#print(reverse(number))