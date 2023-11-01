# Data Structure course
from queue import Queue

# ############################################### LIST ##################################################

# #CREATING A LIST 
# print ("\n\n *******CREATING A LIST*******") 
# my_list = [] # Create empty list
# print(my_list)
# my_list = [1,2,3,'example',3.132] #Creating a list with data
# print(my_list)


# #ADDING ELEMENT TO A LIST
# print ("\n\n ******* ADDING ELEMENT TO A LIST*******") 
# my_list = [1,2,3]
# print(my_list)
# my_list.append([555,12]) # Add all element pass to list as a single element; so eseentially inserting a list within a list
# print(my_list)
# my_list.extend([234, 'more_example', 265])# Add elements to the list as different element
# print(my_list)
# my_list.insert(1,'insert_example')#insert element in the list at the spicifient index location; in the case, index 1
# print(my_list)


# #DELETING ELEMENT FROM A LIST
# print ("\n\n ******* DELETING ELEMENT FROM A LIST*******")
# my_list = [30,1,2,3,'example',3.132,10,30, 30]
# print(my_list)
# del my_list[5] # delete element at index 5
# print(my_list)
# my_list.remove(30) # Remove the first occurance of an element in list
# print(my_list)
# a = my_list.pop(0)# Pops elemet from the specified index location from the list. If no index is provided, pop will remove the element at the top; in this case, 30
# print('Popped Element',a,'List ramaining:',my_list)
# my_list.clear() # Remove all elements from a list
# print(my_list)


# #ACCESSING ELEMENTS FROM A LIST
# print ("\n\n *******ACCESSING ELEMENT FROM A LIST*******")
# my_list = [1,3,2,'example',3.132, 0,30]
# for element in my_list:
    # print(element)
# print(my_list)
# print(my_list[3])#access index 3 element
# print(my_list[0:2])#access element from 0 to 1 and exclude 2
# print(my_list[::-1]) #access elements in reverse
# print(type(my_list))


#OPERATIONS ON A LIST
# my_list = [1,3,2,'example',3.132, 10,30]
# print(my_list)
# my_list *=2 # Take all the elements of the list and cancatinate it to the original list 
# print(my_list)
# b = all(my_list) # Returns true if all the elements are none 0 and false otherwise
# print(b)
# c = any(my_list) #Return true if any of the elements in the list is greater than zero.
# print(c)


# #OPERATIONS ON A STRING LIST
# my_string = "Hello Python World!"
# print(my_string)
# print(my_string[0:18]) # The start index in inclusive and end index is exclosive
# print (my_string[::-1]) #Access every other elecment in the string starting from 0 index




################################################TUPLES###################################################
# print ("\n\n ******* WORKING WITH TUPLES*******")
# # An ordered collection of element
# # Fields are what we used to the refer to the elements of a tuple
# # No duplicate values are allows in set
# # Tuples are immutable. Once created, it cannot be updated. 
# # Nested list within a tuple can be updated
# # The tuple as a whole can be deleted, but individual element from the tuple cannot be deleted
# # Tuples are define with curve bracket and  List are define using square brackets
# my_tupel = ()
# print (my_tupel)
# my_tupel = (1,2,3,4,5)
# print(my_tupel)



#####################################DICTIONARIES########################################################
# print ("\n\n ******* WORKING WITH DICTIONARIES ****")
# # A dictionary in python can be best define as a key-value pair
# # The keys in a dictionary has to be unique
# # Values can only be access through their keys; trying to index a dictionary using a value will result in an error
# # If a key is not unique in a dectionary, python will only assigned the last value assigned to that key once that dictary is instantiated
# # Dictionary can have a mixture of different type key value pairs
# # Dictionay can have complex data types as value. For example, a list,or tuple
# # The values of dictionaries can be dictionary as well 
# # A dictionary is define using curly braces
# my_dic = {}
# print(my_dic)
# my_dic = {"Jada":"8","Jayla":"3"} # Name and age dictionary, where the key is name and the value is the age
# print(my_dic["Jada"]) # Will print Jada's age
# my_dic2 = {"Jada":"8","Jayla":"3","Jayla":"5", "Jayla":"9"} 
# print(my_dic2) #Python should on the print the last assigned value to Jayla because the key is not unique
# my_dic2["Junior"] = 37 # This should add another key value pair to the my_dic2 dictionary
# my_dic2["Sterling"] = 37
# print(my_dic2)



#####################################DATA STRUCTURES AND ALGORITHMS######################################
print ("\n\n **************** DATA STRUCTURES AND ALGORITHIMS *******************")
# Data structures are ways to organize information in such a way that you can do usefull things with it
# Data structure are absolute representation of a data from the point of view of the implemetor, while obstract data type are mathematical models
# There three different matrix for measuing the efficiency of an algorithim: Time, Space, and Network(bandwidth by the algorithim)
# What is complexity? Complexity is a measure of how reasource requirement change as the size of the problem gets larger
# What is the maximum number of basic operations that might have to performed based on the input?
# An algorithm whose complexity does not change with input size, has a big of O(1); Which means the execution time remains constant
# The complexity of an algorithm is O(N) if the time taken by the algorithm increases linearly when N increases
# The complexity of an algorithm is O(N^2: Big of N square) if the time taken by the algorithm increases quadrically when N increases
print ("\n\n ************** CONSTANT TIME COMPLEXITY O(1) *******************")
def addition(num1, num2):
   num_interations = 0 # Keep count of the number of interation as function input changes
   total = num1 + num2
   num_interations +=1
   print("The sum of %d and %d is %d \nTotal number of interation =%d" %(num1, num2,total, num_interations))
        
addition(8,5)  # Call add function

print("\n")
def check_oddeven(number):
    count = 0
    num_interations = 0
    if (number % 2 == 0):
        num_interations +=1
        print("%d is an even number" %number)
    else:
        num_interations +=1
        print("%d is an odd number" %number)
    print("Total number of interation = %d" %(num_interations))    
    
check_oddeven(57) # Call adde even function
print("\n")


def find_square(number):
    num_interations = 0
    square = number**2
    num_interations+=1
    print("Square of %d is %d \nTotal number of interations = %d" %(number, square, num_interations))

find_square(5) # Call function


print ("\n\n ************** LINEAR TIME COMPLEXITY O(N) *******************")

def check_prime1(number):
    num_interations = 0
    for i in range(2, number): #Prime numbers are number that are only devisible by itself and one, therefore exclude 1 and number interest and check the numbers in between
        # print("i is %d" %i) - i starts interating from 2
        num_interations+=1
        
        if number%i == 0:
            print("%d is not a prime number \nTotal number of interation =%d" %(number, num_interations))
            
            return
    print("%d is a prime number \nTotal number of iteration = %d" %(number, num_interations)) 
check_prime1(1845)    
    
print("\n") # Create space between function call
def find_maxval(num_list):
        maxval = num_list[0]
        num_interations =0
        for i in range(len(num_list)):
            num_interations += 1 #Increment to the next element in the list before comparing with maxval
            
            if maxval < num_list[i]:
                maxval = num_list[i]
                
        print("Maximum value of the list = %d \nTotal number of interations = %d" %(maxval, num_interations))
find_maxval([2,78,9,89,450])

def find_factorial(number:int):
    fact = 1
    num_interations = 0
    if(number < 1 or type(number) != int):
        print("Invalid datatype")
        return
    for i in range(1, number +1): # The range function goes up to, but does not include the last number, therefore a plus is added to fix this
        fact = fact * i
        num_interations += 1
    print(" The factorial of %d = %d \n Total of interation = %d" %(number, fact, num_interations))
 
find_factorial(6)
print("\n") # Create space between function call

def two_for_loops(number):
    total = 0
    num_interations = 0
    for i in range(number):
        num_interations +=1
        total = total + i
    
    for i in range(100):
        num_interations +=1
        total = total + i
        
    print("Total interations is: %d" %num_interations)
    
two_for_loops(20) 
print("\n") # Create space between function call


# print ("\n\n ************** QUADRATIC TIME COMPLEXITY O(N*N) *******************")
# def print_pairs(number_list):
    # num_interations = 0
    # n = len(number_list)
    
    # for i in range(n):
        # for j in range(n):
            # print(number_list[i], number_list[j])
            # num_interations +=1
    # print("To,tal interaions are %d" %num_interations)        
# print_pairs([6,8,12])
# print("\n") # Create space between function call

# print ("\n\n ************** QUADRATIC TIME COMPLEXITY O(N*M) *******************")
# def find_prime(lower, upper):
    # num_interations = 0
    # for num in range(lower, upper):
        # for i in range(2, int(num/2)):
            # num_interations +=1
            
            # if(num % i) == 0:
                # break
        # else:
            # print(num)
            # num_interations +=1
    # print("Total interaions are %d" % num_interations)
# find_prime(2,4)
# print("\n") # Create space between function call

# def print_combination(n, m):
    # num_interations = 0
    
    # for i in range(n):
        # for j in range(m):
            # print(i,j)
            # num_interations +=1
    # print("Total interaions are %d" %num_interations)
# print_combination(5,8)
# print ("\n\n ************** LINKED LIST *******************")









