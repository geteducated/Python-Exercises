def getNums():
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    return num1, num2
    

def getProd(num1, num2):
    prod=num1*num2
    return prod

def prodFilter(prod,num1,num2):
    if(prod <= 1000):
        print(prod,"is the product of num1 and num2 and is less than 1000")
    else:
        sum=int(num1+num2)
        print(sum,"is the sum of num1 and num2 and their product is over 1000")

        
num1, num2= getNums()
prod=getProd(num1, num2)  
prodFilter(prod,num1,num2)
