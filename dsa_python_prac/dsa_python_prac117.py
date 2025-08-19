Visualize: Create a Linked List
Visualize how Linked List is created:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # a linked list of three nodes: 80->9->14
    def create_linked_list(self):
        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

linked_list = LinkedList()

# create linked list
linked_list.create_linked_list()
