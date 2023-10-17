string= str(input("Enter a string: "))
length= len(string)
print("String length is ", length)

count=0
a=0
while(count<=length-1):
    if(string[count].isalpha() == True):
        a+=1
    elif(string[count].isdigit() == True):
        a+=1
    elif(string[count].isalpha() == False and string[count].isdigit() == False):
        a+=1
    count+=1

print("Character count: ", a)
