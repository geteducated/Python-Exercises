#display all prime numbers within a range
import math

num = int(input("Enter num to check if it is a prime num: "))


if(num>1):
    for a in range(1,num):
        a+=1
        
        if(num%a==0 and a!=1 and a!=num):#check if prime num
            print("Not a prime number. Number ", num ," contains factors other than 1 and ",num,".")#display prime num
            break
        else:
            print(num," is a prime number")
            break
        
else:
    print("Number must be greater than 1.")
