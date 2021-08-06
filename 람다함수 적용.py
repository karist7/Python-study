numbers = list(range(1,10+1))

print(list(filter(lambda x:x%2==1,numbers)))
print(list(filter(lambda x:3<=x<7,numbers)))
print(list(filter(lambda x:x*x<50,numbers)))

