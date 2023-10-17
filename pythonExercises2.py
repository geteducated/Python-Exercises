import random

sum=0
for i in range(0,10):
    num= random.randrange(0,100,1)
    sum= num+sum
    print("number", i,":", num, "current sum:",sum)
