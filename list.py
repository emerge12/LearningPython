# - What is a list?
# - A list if a collection of items in a particular order. In python square bracket ([]) indicates a list. 
# - It is good practice to make the name of a list plural. For example, names, digits, letters as list is a collection of things
# - Items in a list are separated by commas
# - A list is an order collection. This means the element of the collection have a specific order. The order is independent of the value
# - Python has a special way of asking for the last element in the list by using -1. This convention extend to other negative numbers too
# - for instance, -2 will return the second to lass element, and a -3 will return the third to last element. 0

#bicycles list 
bicycles = ['trek', 'cannondale','redline','specialized']
print(bicycles)# Prints the list
print(f"{bicycles[0].title()}, is the first item in the list")  # request the first item in the list
print(f"{bicycles[-1].title()}, is the last item in the list")  # request the last item in the list


# Changing, adding, and removing elements from a list
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

motocycles[0] = 'ducati' # Replacing the item in position 0
print(motocycles)

motocycles.append('honda')
print(motocycles)

motocycles.insert(0, 'rr') # The method insert "rr" at index 0 and shift all ther other elements to the right
print(motocycles)

del motocycles[0] # - Remove item in position 0 from the list
print(motocycles)

# - Removing item using the pop method. Pop allows you to remove an used the item(store value )
# - The Pop method remove the last item in the list
# - Item from any position can be pop from a list by passing the index of that element to the pop method.
# - If you know the name or value of the element you want to remove, but you don't know the its index, used the remove method
# - The remove() method only delete the first occurance of the value you specify. If there is more that one occurance
# - you'll have to call the method more that once or used a loop.

lst_motorcycle = motocycles.pop()
print(f"{lst_motorcycle.title()} is the last motorcycle in the list!")
print(motocycles)

# Pop the first item from the list
lst_motorcycle = motocycles.pop(0)
print(f"{lst_motorcycle.title()} is the first item from the remaining list!")
print(f"{motocycles} is the current list")

# Remove item yamaha from the list
too_expensive = 'yamaha'
lst_motorcycle = motocycles.remove(too_expensive)
print(lst_motorcycle)
#print(f"{too_expensive.title()} was removed from an unknown index position using the remove() method")
print(motocycles)


# - ORGANIZING A LIST
# - The sort() method changes list permanently 
# - The sort(reverse = True) method changes list permanently in reverse order
# - the sorted(list) method changes list temporarily
# - the sorted(list, reverse = True) method changes list temporarily in reverse order



# Sorting list in alphabetical order
print('..............Sorting list permanently using the sort() method')
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# Sorting list in reverse order
print('..................Sorting list permanently in the reverse order using the sort(reverse= True) method the reverse = True parameter')
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)


# Sorting list in reverse order
print('................Sorting list temporarily using the sorted() method')
cars = ['bmw','audi','toyota','subaru']
print(f" This list {sorted(cars)} is temporarily sorted")
print(f" This list {sorted(cars, reverse= True)} is temporarily sorted in reverse order")
print(cars)


#- PRINTING A LIST IN REVERSE ORDER
# - To reverse the original order of list, you can use th reverse() method
# - The reverse method changes the order of the list permanently, however, you revert to the original order by calling the reverse() method again
cars = ['bmw','audi','toyota','subaru']
print('..............printing and reversing the original list')
print(cars)
cars.reverse()
print(cars)


# - FINDING THE LENGTH OF LIST 
# - The length of list can be quickly find using the len() method

cars = ['bmw','audi','toyota','subaru']
print(f" There are {str(len(cars))} cars in the list.")


# - AVOIDING INDEX ERROR WHEN WORKING WITH A LIST


