string= str(input("Enter a string: "))
length= len(string)
print("String length is ", length)

count=0

for count in range(0,length):
    if(string[count].isdigit()):
        print(string[count], end="") ####how to print on same line; end=""
        count+=1
