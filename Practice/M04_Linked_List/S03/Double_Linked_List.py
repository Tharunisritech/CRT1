'''
    Double Linked list:
    data store Nodes 
    nodes 3 parts
    1. dat
    2. prev
    3. next

    Algorithm:
    1. Create Nodes
    2. Insert data
    3. Connection btw nodes
    4. Traverse

'''
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 
#         self.prev = None 
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.prev = node1

# node2.next = node3
# node3.prev = node2

# node3.next = node4
# node4.prev = node3



# def traverse_forward():
#     curr = node1
#     while curr:
#         print(curr.data, end = " <-> ")
#         curr = curr.next
#     print("None")


# def traverse_backword():
#     curr = node4
#     while curr:
#         print(curr.data, end = " <-> ")
#         curr = curr.prev
#     print("None")

# traverse_forward()
# traverse_backword()

'''
Insertion at the beginning, Insertion at the end, Insertion at any position...

'''
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None 
#         self.prev = None 

# def insert_begin(head,data):
#     new_node = Node(data)
#     new_node.next = head

#     if head:
#         head.prev = new_node
#     return new_node

# def insert_end(head,data):
#     new_node = Node(data)

#     if head is None:
#         return new_node

#     curr = head
#     while curr.next:
#         curr = curr.next
#     curr.next = new_node
#     new_node.prev = curr
#     return head 

# def insert_anywhere(head, data,position):
#     new_node = Node(data)

#     if position == 1:
#         new_node.next = head
#         if head:
#             new_node.prev = head
#         return new_node

#     curr = head
#     for i in range(position - 2):
#         curr = curr.next

#     new_node.next = curr.next
#     new_node.prev = curr

#     if curr.next:
#         curr.next.prev = new_node
#     curr.next = new_node

#     return head

# def traverse(head):
#     curr = head
#     while curr:
#         print(curr.data, end = " <-> ")
#         curr = curr.next
#     print("None")

# head = None 
# head = insert_begin(head, 10)
# head = insert_begin(head, 20)
# head = insert_begin(head, 30)
# head = insert_begin(head, 40)
# print("Insertion at the beginning")
# traverse(head)

# head = insert_end(head, 100)
# print("Insertion at the end")
# traverse(head)

# head = insert_anywhere(head,25,3)
# print("Insertion at any position")
# traverse(head)

'''
Deletion of node in a doubly linked list
1. deletion at the beginning 
2. deletion at the end 
3. deletion anywhere or at a position'''

#  Deletion at the beginning 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head

    if head:
        head.prev = new_node 

    return new_node
def delete_begin(head):
    if head is None:
        return None 
    
    head = head.next

    if head:
        head.prev = None

    return head 

def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")

head = None
head = insert_begin(head, 100)
head = insert_begin(head, 200)
head = insert_begin(head, 300)
head = insert_begin(head, 400)
print("before deletion:")
traverse(head)

head = delete_begin(head)
print("After deletion:")
traverse(head)

