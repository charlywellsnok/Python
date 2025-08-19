Append a Node
Can you write a program to append a node to an existing linked list on your own?

Add the append() method to the LinkedList class, following the outline provided in the editor.
The append() method should insert a node at the end of the linked list.
Then, print the linked list by calling the display() method.
For example,

The starting linked list will always be:

90->80->60->50
If you append a new node with data 12, the linked list should become:

90->80->60->50->12
Example
Test Input

12
Expected Output

90->80->60->50->12->None
Confused about something? Ask a question!











# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 90->80->60->50
    def create_linked_list(self):
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    #  method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        # write your code here
        ___

    # traverse the list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

linked_list = LinkedList()

# create the initial linked list
linked_list.create_linked_list()

# input for data to append
data = int(input())
linked_list.insert_node_at_beginning(data)

# print the updated linked list
linked_list.display()
