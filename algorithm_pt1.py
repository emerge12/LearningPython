#Sorting Algorithm
data = [4,7,1,2,8,12,6,10, 80,0, 9,11, 3,90,15,14]
def print_list(num_list):
    print(num_list)
    
# Selection Sort algorithm sorts a list of item in place in an accesinding order
# It's unprdictable how element of the same value will be handled
# Time complexity of O(N^2)
# Space complexity is O(1)
def selection_sort(arry):
    curr_min = 0
    for i in range(0, len(arry)-1): # Interate up to second to last element
        curr_min = i
        for j in range(i+1, len(arry)):
            if arry[j] < arry[curr_min]: # Start with the assumption that the minimum value in the array is at index zero
                                         # then compare that value with other values as you traverse the array, if a smaller value
                                         # is found, then index of curr_min is updated
                curr_min = j
        arry[i], arry[curr_min] = arry[curr_min], arry[i] #Finally, the minimum value is place the 
    print_list(arry)
  


selection_sort(data)
   
# The bobble sort is a in place algorithm where larger element bubbles to the bottom of the list
# The bubble sort in great, but it not the most efficient algorithm because it will still execute until the end end it the fo loop even if the sort in complete in one iteration
# To make the bubble sort more efficient, a sort counter can be introduce. Therefore, once all elements are sort, you can exit the loop
# Other variration of the bubble sort algorithm can be accomplish by starting at the opposite end and bubble the smaller number to the beggining of the list
# Time complexity of O(N^2)
# Space complexity is O(1)
def bubble_sort(arry):
    lentgh = len(arry)
    for i in range(lentgh-1, 0, -1):
        for j in range(i):
            if arry[j] > arry[j+1]:
                arry[j+1], arry[j] = arry[j], arry[j + 1]
    print_list(arry)
            

bubble_sort(data)


# Insertion sort is also an in-place algorithm.The algorithm works by comparing the intem left of the current
#.... item of interest. If the item is less, then a swap is performed. This action is perform until array is  completely sorted 
# The insertion sort is a stable sort, as entities bubble to the correct position in the sublist that is sorted. The list original
#.....of entities are maintained for for equal element
def insertion_sort(arry):
    for i in range(0, len(arry)-1):
        for j in range(i+1, 0,-1):
            if arry[j] < arry[j-1]:
                arry[j], arry[j-1] = arry[j-1], arry[j]
        print(list(range(i+1, 0,-1)))
    print_list(arry)
    
insertion_sort(data)


# Shell sort is a divide and conquor algorithm
# Sehll sort uses insertion sort, and the entire list is divided and those sublists are sorted
# Getting the exact complexity of the shell sort is hard because it depends on the increment values chosen
# Also it's not clear what the best increment values is 
# The complexity of shell sort is better than insertion sort as the final interation with increment = 1has to work with a nearly sorted list
# The complexity os shell sort is somewhere between O(N) and O(N^2)
# Different values of increments produce different complexity
# For incmrement 2^k - 1 for K = 1, 2, 3.....
# The complexity is O(N^3/2)
# The algorithm is adaptive since its base on insertion sort, which is addaptive
# Space complexity is O(1)
# The effiecientcy of the shell sorting depends on the gap sequence, the better the gap sequence less time will taken to sort the array
# When Gap is equal to one, shell sort will works the same as insertion sort
# There are many method to caculate gap
print("Starting shell sort algorithm..........")
def shell_short(arry):
    length = len(arry)
    gap = length / 2
    print("This is gap", gap)
    break
    while gap > 0:
        for i in range(gap,length):
            temp = arry[i]
            j = i
            while j >= gap and arry[j-gap] > temp:
                arry[j] = arry[j-gap]
                j -= gap
            arry[j] = temp
            
            print('Gap', gap)
            print_list(arry)
        gap = gap // 2
    
shell_short(data)