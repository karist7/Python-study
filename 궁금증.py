l = [1,2,3]
a = [4,[5,6]]
o=[]
for i in a:
    if type(i) == list:
        o+=i
        print(o)
    else:
        o.append(i)
        print(o)
print(l+a)
