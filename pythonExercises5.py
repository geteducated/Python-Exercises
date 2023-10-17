
list1 = [10, 21, 4, 67, 10]
list2 = [10, 3, 4, 45, 66, 10]
list3 = [10, 21, 4, 21, 10]


def check(list):
    if(len(list)%2==0):
        print("Num list is NOT a palindrome- length is even")
        return False
    else:
        for i in range(0,len(list)-1):
            if(list[i]==list[len(list)-1-i]):
                
                print("yes- so far it's palindromic")
                #return True
            else:
                print("non palindrome number- odd nums but not reversible")
                #return False
                break
            

choice = int(input("enter '1' for List 1 OR '2' for list 2 OR '3' for list 3: "))
if(choice ==1):
    check(list1)
elif (choice ==2):
    check(list2)
elif (choice ==3):
    check(list3)

