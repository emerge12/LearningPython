 ################################### DATA STRUCTURE AND ALGORITHM##############################

from queue import Queue
from collections import deque

print("Instantiating a queue............")
olympics = Queue(5) # Create a queue with five elements
print(type(olympics) )
print("\n")

print("Adding elements to queue........")
olympics.put("United States") # adding the elements to the queue
olympics.put("United Kinqdom")
olympics.put("Germany")
olympics.put("Jamacia")
olympics.put("Ghana")
print("\n")


# Checking the queue size and if the queue is full or empty
print("quareying queue...........")
print("Is queue empty? " + str(olympics.empty()))
print("Is queue full? " + str(olympics.full()))
print("What's the queue size? " + str(olympics.qsize()))
print("\n")

# To de-queue or remove and element(s) from the queue, the get() function is used
# The queue is first in first out data structure, therefore the first element that is added is the first element that will get removed when get function is called
print("De-queuing..........")
print(olympics.get()) # USA is remove; USA was the first element added to the queue
print(olympics.get()) # United Kinqdom is remove
print(olympics.get()) # Germany is remove
print("\n")

# The qsize method returns the count of the amount of element added to the queue
print("Checking remaining elements in queue.............")
print("What's the queue size? " + str(olympics.qsize()))
print("\n")

#Implementing a queue using a list structure
class myQueue:
    def __init__(self):
        """ Create a new queue"""
        self.items =[]
        
    def is_empty(self):
        """ Return true if queue is empty"""
        return len(self.items) == 0
        
    def enqueue(self, item):
        """ Add a new item to the end of the queue"""
        self.items.append(item)
     
    def dequeue(self):
        """ Remove an element from the beginning of the queue"""
        return self.item.pop(0)
        
    def size(self):
        """ Return the size of the queue """
        return len(self.items)
        
    def peek(self):
        """ Return the element from the front of the queue"""
        if self.is_empty():
            raise Exception("Nothing to peek")  
        return self.items[0]
        
        
        
        
olympics = myQueue()
print(type(olympics))

olympics.enqueue("Jamacia")
olympics.enqueue("kingston")
print(olympics.items)
print(olympics.peek()) # Returns the element from the front of the queue
print(olympics.size()) # Returns the element from the front of the queue


#Implementing a stock data structure using a list. A stock is a last in first out datastructure
# The end of a python list and the top of a stack is pretty much the same
print("\n")
print("Implementing a stack data structure")
stack = []
stack.append("Jamaica") # The append function adds an item to the end of list which is essently what happen when an item is added to stock
stack.append("Manchester")
stack.append("Kingston")
stack.append("Clarendon")
stack.append("USA")
stack.append("India")
stack.append("China")
print(stack)
print("\n")
print("Remove the last element from the stack")
print(stack.pop()) # when pop function is invoke on a list without an index being pass, the last element is return from the list
        

print("\n")
print("Implementing a custom stack")

class  stack:

    def __init__(self):
        """Creat a new stack"""
        self.stack = []
        
    def is_empty(self):
        """Check is the stack is empty"""
        return len(self.stack) == 0
        
    def push(self, data):
        """Add an element to the stack"""
        self.stack.append(data)
        
    def pop(self):
        """Remove element from the top of a stack"""
        if self.is_empty():
            raise Exception ("Nothing to pop")
        return self.stack.pop(len(self.stack)-1)
        
    def peek(self):
        """ Have a look at the top of the stack"""
        if self.is_empty():
            raise Exception ("Nothing to peek")
        return self.stack(len(self.stack)-1)
        
    def size(self):
        """ Returns the len of the stack"""
        return len(self.stack)
        
        
olympics = stack()
print(olympics)
olympics.push("Jamaica") # All element to the stack
olympics.push("Ghana")
olympics.push("Senegal")
olympics.push("Germany")
olympics.push("France")
print(olympics.size()) # Return the stack size
print(olympics.is_empty()) #Check if stack is empty
print(olympics.pop()) # Remove the last/top element from the stock
print(olympics.size()) # check size of stack after the top element was removed
print(olympics.pop())
print(olympics.pop())



print("\n")
print("Implementing your own custom linked list. Example 01")

class Node:
    """ A node in a singly-linked list"""
    def __init__(self,dataval = None, nextval = None):
        self.dataval = dataval
        self.nextval = nextval
        
    def __repr__(self): # Stands for the representation of the object
        return repr(self.dataval)
        

class LinkedList:
            
    def __init__(self):
        """ Creating a new singly-linked list"""
        self.head = None
        
        
    def __repr__(self):
        """Creating a string representation of the data in the list"""
        nodes = []
        curr  = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.nextval
        return '[' + '->'.join(nodes) + ']'
        
        
        
    def prepend(self, dataval):
        """ Insert a new element at the beginning of the list"""
        self.head = Node(dataval = dataval, nextval = self.head)
        
     
    def append(self, dataval):
        
        """ Inserting new element at the end of the list"""
        if not self.head:
            self.head = Node(dataval = dataval)
            return
        curr = self.head
        while curr.nextval:
            curr = curr.nextval
        curr.nextval =Node(dataval = dataval)
        
        
    def add_after(self, middle_dataval, dataval):
        """ Insert a new element after the node with middle_dataval"""
        if middle_dataval is None:
            print("Data to insert after not specified")
            return
        curr = self.head
        while curr and curr.dataval != middle_dataval:
            curr = curr.nextval
        new_node = Node(dataval = dataval)
        new_node.nextval = curr.nextval
        curr.nextval = new_node
        
        
    def find(self, data):
        """ Search for the first element with dataval matching
            data. Return the element of None is not found"""
        curr = self.head
        while curr and curr.dataval != data:
            curr = curr.nextval
        return curr
                
        
    def remove(self, data):
        """ Remove the first occurance of the data in the list"""
        curr = self.head
        prev = None
        
        while curr and curr.dataval != data: # This loop will interate until the data is found or not found
            prev = curr # If the node to be removed is the head node, then prev would remain at none and 
            curr = curr.nextval
        if prev is None:
            self.head = curr.nextval # If prev is None, simple advance the head pointer to the next Node
        elif curr:
            prev.nextval = curr.nextval
            curr.nextval = None
                    
print("\n")
print("Implementing a linked list using deque. Example 02")
# When initializing a list, you can pass any iteratable obeject as the input
lList = deque("abcd")
lList.append("e") # Adding element to the end of the list 
lList.append("f") 
print(lList)
print(lList.pop()) # Remove the elemement from the end of the list
lList.appendleft("f") # Appends f to the left/beginning of the list
lList.appendleft("x")
print(lList)
print(lList.popleft()) # Remove element from the left/beginning of the list


print("\n")
print("Implementing custom lisked list. Example 03")


class LinkedList2:
    def __init__(self):
        self.head = None
        
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nxt
        nodes.append("None")
        return " ->".join(nodes)
        
        
        
class Node2:
    
    def __init__(self, data):
        self.data = data
        self.nxt  = None
        
    def __repr__(self):
        return self.data



lList = LinkedList2()
firstNode  = Node2("4")
secondNode = Node2("b")
thirdNode  = Node2("c")
lList.head = firstNode
firstNode.nxt = secondNode
secondNode.nxt = thirdNode
thirdNode.nxt = None
print(lList)

print("\n")
print("Implementing custom lisked list. Example 04")

class LinkedList3:
    # This init function give you the ability to create a list from any interatable object
    # by adding an optional paremeter to the init method and corresponding code
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node3(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.nxt = Node3(data=elem)
                node = node.nxt
        
    # Return a string representation of the data in the node
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nxt
        nodes.append("None")
        return " ->".join(nodes)

    # Iterate linked list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nxt
    
    # Insert node at the beginning of the list 
    def prepend_list(self, node):
        node.nxt = self.head
        self.head = node;
    
    # Insert node at the end of the list
    def append_list(self, node):
        curr = self.head
        while curr.nxt is not None:
            curr = curr.nxt
        curr.nxt = node
    
    # Inserting new node after a specified node.
    def add_after_node(self, data, node):
        if self.head is None:
           raise Exception("Linked list is empty")
        curr = self.head
        while curr.nxt is not None and curr.data != data:
            curr = curr.nxt
        node.nxt = curr.nxt
        curr.nxt = node
        
    # Inserting a new not before a specified node
    def add_before_node(self, data, node):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        if self.head.data == data:
            return self.prepend_list(node)
        prev_node = self.head
        for nd in self:
            if nd.data == data:
                prev_node.nxt = node
                node.nxt = nd
                return
            prev_node = nd
        raise Exception("Node with specified data was not found!")
        
    #Removing node from a list
    def remove_node(self, data):
        if self.head == None: # If the list empty
            raise Exception("Linked list is empty")
        
        if self.head.data == data:
            self.head = self.head.nxt
            return

        prev_node  = self.head
        for node in self:
            if node.data == data:
                prev_node.nxt = node.nxt
                return
            prev_node = node
        raise Exception("Node with specified data not fount")
        
    # Indexing linked list
    def find_node(self, index):
        if self.head == None: # If the list empty
            raise Exception("Linked list is empty")
        count = 0
        for node in self:
            if count == index:
                return node.data
            count +=1
        raise Exception("Index out of bound")
        
        
    def reverse(self):
        """ Reverse the list in place"""
        curr = self.head
        prev_node = None
        while curr:
            next_node = curr.nxt #Pointer to next node after current
            curr.nxt = prev_node # Reverse pointer to whatever the previous next is pointing to
            prev_node = curr 
            curr = next_node
        self.head = prev_node
                    
    
       
           
class Node3:
    
    def __init__(self, data):
        self.data = data
        self.nxt  = None
        
    def __repr__(self):
        return self.data
        
       
        
lList  = LinkedList3()
lList.prepend_list(Node3("1"))
lList.prepend_list(Node3("2"))
lList.prepend_list(Node3("3"))
lList.append_list(Node3("1"))
lList.append_list(Node3("8"))
lList.append_list(Node3("6"))
lList.append_list(Node3("5"))
print(lList)
lList.reverse()
print(lList)
lList.add_after_node("6", Node3("10"))
lList.add_before_node("8", Node3("15"))
print(lList)
lList.remove_node("10")
lList.reverse()
print(lList)
print(lList.find_node(0))

print("\n")
print("Implementing custom double lisked list. Example 05")


class Node4:

    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.pre_node  = None
        
          
        
class LinkedList4:
    def __init__(self):
        self.head = None
        
        
        
        
        
        
        
        