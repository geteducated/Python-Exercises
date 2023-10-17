
list1 = [10, 21, 4, 45, 66, 93]
list2 = [10, 21, 4, 45, 66, 10]


def check(list):
    if(list[0] == list[len(list)-1]):
        print("True- first and last nums match")
        return True
    else:
        print("False- first last nums mismatch")
        return False

choice = int(input("enter '1' for list1 or '2' for list2: "))
if(choice ==1):
    check(list1)
elif (choice ==2):
    check(list2)


#check if first and last are the same. 
