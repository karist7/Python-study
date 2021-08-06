counter = 0
def factorial(n):
    global counter
    counter +=1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return factorial(n-1)+factorial(n-2)


print(factorial(10))
print(counter)