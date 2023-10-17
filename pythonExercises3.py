import array as arr

string=str(input("enter a string:"))
#length=len(string)
#print(length)


for i in range(0,len(string)):
    if(i%2 == 0):
        print(i%2)
        print("index", i, "is", string[i])
