Insert a Node at the Given Position
Can you write a program to insert a node at the given position in an existing linked list?

Add the insert_node() method to the LinkedList class, following the outline provided in the editor.
The insert_node() method should insert a node at the given position with the given value.
Then, print the linked list by calling the display() method.
For example, the starting linked list will always be:

8->3->9->7->6->None
If you insert a new node with data value 12 at position 3, the linked list should become:

8->3->12->9->7->6->None
Example
Test Input

3
12
Expected Output

8->3->12->9->7->6->None
Confused about something? Ask a question!
















# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

     # create linked list
    def create_linked_list(self):
        node1 = Node(8)
        self.head = node1

        node2 = Node(3)
        node1.next = node2

        node3 = Node(9)
        node2.next = node3

        node4 = Node(7)
        node3.next = node4

        node5 = Node(6)
        node4.next = node5

    # traverse linked list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)


    def insert_node_at_position(self, data, position):

        new_node = Node(data)
        current = self.head

        for i in range(1, position -1 ):
            current = current.next

        new_node.next = current.next
        current.next = new_node


linked_list = LinkedList()

# create the initial linked list
linked_list.create_linked_list()

# position of the new node
position = int(input())

# the data value of the new node
data = int(input())

linked_list.insert_node_at_position(data, position)

# print the updated linked list
linked_list.display()
