'''Singly Linked List:
Algorithm:
1. create Node
2. Insert the data into the nodes
3. Connection between these nodes 
4. Traverse all the nodes'''

# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# def traverse():
#     curr = node1
#     while curr:
#         print(curr.data,end = " -> ")
#         curr = curr.next
#     print("None")

# traverse()

# Operations:
# 1. Insertion: 3 ways 
    # a) Insertion at the beginning 
    # b) I nsertion at the end 
    # c) Insertion at the specified node
# 2. Deletion 
# 3. Traverse
# 4. Update

# a) Insertion at the beginning in the singly linked list:
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def insert_begin(head, data):
#         new_node = Node(data)
#         new_node.next = head
#         return new_node
#     def traverse(head):
#         curr = head
#         while curr:
#             print(curr.data, end =" -> ")
#             curr = curr.next
#         print("None")

#     head = None
#     head = insert_begin(head, 10)        
#     head = insert_begin(head, 20)  
#     head = insert_begin(head, 30)  
#     print("Insertion at the beginning")

# 

        
  
# Insertion at the end in the singly linked list 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_begin(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node


# def insert_end(head, data):
#     new_node = Node(data)

#     if head is None:
#         return new_node

#     curr = head

#     while curr.next:
#         curr = curr.next

#     curr.next = new_node
#     return head


# def traverse(head):
#     curr = head

#     while curr:
#         print(curr.data, end=" -> ")
#         curr = curr.next

#     print("None")


# head = None

# head = insert_begin(head, 10)
# head = insert_begin(head, 20)
# head = insert_begin(head, 30)

# print("Insertion at the begin")
# traverse(head)

# print()

# print("Insertion at the End")
# head = insert_end(head, 400)
# traverse(head)





# **** Deletion at the beginning the linked list singly** ******

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def insert_begin(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node

# def deletion_begin(head):
#     if head is None:
#         print("Error")
#         return
#     new_head = head.next
#     del head
#     return new_head

# def insert_end(head, data):
#     new_node = Node(data)

#     if head is None:
#         return new_node

#     curr = head

#     while curr.next:
#         curr = curr.next

#     curr.next = new_node
#     return head


# def traverse(head):
#     curr = head

#     while curr:
#         print(curr.data, end=" -> ")
#         curr = curr.next

#     print("None")


# head = None

# head = insert_begin(head, 10)
# head = insert_begin(head, 20)
# head = insert_begin(head, 30)

# print("Insertion at the begin")
# traverse(head)

# print()

# print("Insertion at the End")
# head = insert_end(head, 400)
# traverse(head)

# class Node: 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None 
 
 
# def insert_begin(head, data): 
#     new_node = Node(data) 
#     new_node.next = head 
#     return new_node 
 
 
# def deletion_begin(head): 
#     if head is None: 
#         print("Error") 
#         return None
#     new_head = head.next 
#     del head 
#     return new_head 
 
 
# def insert_end(head, data): 
#     new_node = Node(data) 
 
#     if head is None: 
#         return new_node 
 
#     curr = head 
 
#     while curr.next: 
#         curr = curr.next 
 
#     curr.next = new_node 
#     return head 
 
 
# def traverse(head): 
#     curr = head 
 
#     while curr: 
#         print(curr.data, end=" -> ") 
#         curr = curr.next 
 
#     print("None") 
 
 
# head = None 
 
# head = insert_begin(head, 10) 
# head = insert_begin(head, 20) 
# head = insert_begin(head, 30) 
 
# print("Insertion at the begin") 
# traverse(head) 
 
# print() 
 
# print("Insertion at the End") 
# head = insert_end(head, 400) 
# traverse(head)

#  **** INSERTION AT BEGINNING , AT END , AT ANYWHERE IN THE LINKED LIST *****
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_end(head,data):
    new_node = Node(data)

    if head is None:
        return new_node 

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head

def insert_anywhere(head, data, position):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        return new_node

    curr = head 
    for i in range(position - 2):
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return head 
def traverse(head):
    curr = head

    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

head = None 
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)

print("Insertion at the beginning")
traverse(head)

head = insert_end(head, 50)

print("Insertion at the end")
traverse(head)

head = insert_anywhere(head,25, 3)

print("Insertion at position 3")
traverse(head)