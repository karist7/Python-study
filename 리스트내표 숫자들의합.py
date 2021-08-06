out =[i for i in range(1,100+1)
    if"{:b}".format(i).count("0")==1]
for i in out:
    print("{}:{}".format(i,"{:b}".format(i)))
print(sum(out))