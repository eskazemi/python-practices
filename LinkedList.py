
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, new_data):
        new_data = Node(new_data)

        if self.head is None:
            self.head = new_data
            return
        temp = self.head
        while temp:
            temp = temp.next

        temp.next = new_data

    def insert_between(self, prev_data, new_data):
        if prev_data is None:
            print("ali")
        new_node = Node(new_data)
        new_node.next = prev_data.next
        prev_data.next = new_node

    def travers(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


my_linkedlist = LinkedList()
my_linkedlist.head = Node(1)
second_node = Node(2)
third_node = Node(3)

my_linkedlist.head.next = second_node
second_node.next = third_node
my_linkedlist.insert_between(second_node, 4)
my_linkedlist.travers()

