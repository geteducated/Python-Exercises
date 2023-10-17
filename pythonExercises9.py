string= str(input("Enter a string of letters, digits, and special symbos: "))

length = len(string)
print("String length: ",length)

alphaCheck= string.isalpha()
numCheck= string.isdigit()
print(alphaCheck, numCheck)

a=0
b=0
c=0
##
##for count in range(0,length):
##     
##    if(string[count].isalpha() == True):
##        a+=1
##        print("Letter count: ", a)
##    elif(string[count].isdigit() == True):
##        b+=1
##        print("Number count: ", b)
##    elif(string[count].isalpha() == False and string[count].isdigit() == False):
##        c+=1
##        print("Symbol count: ", c)
##    count+=1   

count=0
while(count<=length-1):
    if(string[count].isalpha() == True):
        a+=1
    elif(string[count].isdigit() == True):
        b+=1
    elif(string[count].isalpha() == False and string[count].isdigit() == False):
        c+=1
    count+=1

print("Letter count: ", a)
print("Number count: ", b)
print("Symbol count: ", c)
