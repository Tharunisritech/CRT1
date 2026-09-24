''' 
Deletion in double linked list:
1. Deletion at the beginning.
2. Deletion at the end.
3.Deletion at any position 

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_LL:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)

        if self.head is None:
            return new_node

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

        

    def delete_begin(self):
        if self.head is None:
            return None

        new_head = self.head
        self.head = self.head.next
        del new_head

    def delete_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def count_nodes(self):
        if self.head is None:
            return 0 
        if self.head.next is None:
            return 1
        
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end = " <-> ")
            curr = curr.next
        print("None")


dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)
dll.insert_end(40)
dll.insert_end(50)
dll.delete_begin()
dll.delete_end()
dll.traverse()
print(dll.count_nodes())