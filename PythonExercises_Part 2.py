import numpy as np

def prob1():
    list= ["apple", "nannas", "coconut", "peaches", "eggplant", "bacon"]
    list.remove("peaches")#remove item in index4
    list.insert(1, "peaches")#add item to 2nd position
    list.append("peaches")#add item to end
    print(list)

# prob1()

def prob2():
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'john': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

    # copy of the roll_number list to avoid modifying it during iteration
    roll_number_copy = roll_number.copy()

    for num in roll_number_copy:
        if num not in sample_dict.values():
            roll_number.remove(num)

    print("Updated roll_number list:", roll_number)


#prob2()

def prob3():
    sample_list= [87, 45, 41, 65, 94, 41, 99, 94]
    set_list =set(sample_list) #set() is to store data and removes duplicates
    sample_tuple= tuple(set_list) #turned set() into tuple
    print("minimum of tuple: ",min(sample_tuple))
    print("maximum of tuple: ",max(sample_tuple))

# prob3()

def prob4():
    alpha_list= ["a","b","c","d"]
    num_list= [1,2,3,4]
    num_list.reverse() #4321

    for x in zip(alpha_list, num_list): #zip puts corresponding elements in a tuple
        print(x)

#prob4()

def prob5():
    alpha_list = ["a", "b", "c", "d"]
    num_list = [1, 2, 3, 4]
    zipped_list= []

    for x in zip(alpha_list, num_list): #zip puts corresponding elements in a tuple
        print(x)
        zipped_list.append(x) #each zipped tuple is appended to a list

    print(dict(zipped_list)) #zipped_list typecasted as dictionary

#prob5()

def prob6():
    my_set= {1,2,3,4}
    my_list= ["a", "b", "c", "d"]
    set(my_list) #turning list into set
    new_set= my_set.union(my_list) #combining two sets
    print(new_set) #set prints elements in different order every run

#prob6()

def prob7():
    tuple1= ("a", "b", "c", "d")


    indices_to_copy = (1, 3) # Copying elements at index 1 and 3
    copied_elements = tuple(tuple1[i] for i in indices_to_copy) #list comprehension

    print("Original Tuple:", tuple1)
    print("Copied Elements:", copied_elements)


#prob7()

def prob8(): #includes prob9
    class Vehicle:
        #initialized the parameters of vehicle class
        def __init__(self, name, max_speed, mileage):
            self.name= name
            self.max_speed= max_speed
            self.mileage= mileage

        def display_info(self): #created a method
            print("Vehicle name:", self.name)
            print("Max speed:", self.max_speed, "mph")
            print("Mileage:", self.mileage, "mpg")

    class Bus(Vehicle): #child class using Vehicle class
        pass #pass parameters, variables, and members to class Bus

    car = Vehicle("Honda", 120, 157000) #created an instance of a vehicle
    car.display_info() #applied method

    bus = Bus("short bus", 50, 123)
    bus.display_info()

#prob8() #Includes prob 9



def prob10():
    class Vehicle:
        #initialized the parameters of vehicle class
        def __init__(self, name, max_speed, mileage):
            self.name= name
            self.max_speed= max_speed
            self.mileage= mileage

        def display_info(self): #created a method
            print("Vehicle name:", self.name)
            print("Max speed:", self.max_speed, "mph")
            print("Mileage:", self.mileage, "mpg")

    class Bus(Vehicle): #child class using Vehicle class
        def __init__(self, name, max_speed, mileage, seats=50): #seats was defaulted here
            Vehicle.__init__(self, name, max_speed, mileage) #vehicle attributes were passed here
            self.seats = seats #attribute was added


        def display_info(self):
            print("Seating Capacity:", self.seats)

    bus = Bus("short bus", 3E10, 123,) #no argument for seats required
    bus.display_info()

#prob10()


def prob11():
    arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16) #set to unsigned int16
    print(arr1)
    print("Shape:", arr1.shape)
    print("Dimensions:", arr1.ndim)
    print("Length of each element int the array in bytes:", arr1.itemsize)

#prob11()


def prob12():
    start = 100
    stop = 200
    diff = 10
    arr= np.arange(start, stop, diff).reshape(5,2)
        #start, stop, and step values of each element are arranged
        #.reshape turns from 1 dimension to 5x2

    print(arr)

#prob12()


def prob13():
    arr1 = np.array([[5, 6, 9], [21, 18, 27]])
    arr2 = np.array([[15, 33, 24], [4, 7, 1]])
    result = arr1+arr2
    print("Sum of arr1 and arr2 is:\n", result)

    result_sqrd = np.square(result) #each element is squared
    print("Square of each element is:\n", result_sqrd)

#prob13()