d = {
    1:1,
    2:1
}
def f(n):
    if n in d:
        return d[n]
    else:
        o = f(n-1)+f(n-2)
        d[n] = o
        return o
print(f(10))
print(f(20))
print(f(30))
print(f(40))