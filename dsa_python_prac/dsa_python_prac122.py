Create and Print a Linked List
Can you write a program to create a linked list and print it on your own?

Create a Node class to initialize the data and next attributes of nodes.
Create a LinkedList class to initialize the head attribute.
Add the create_linked_list() method to the LinkedList class. This method will be used to add nodes to the linked list.
Add another method, traverse_linked_list() to the LinkedList class. This method will be used to traverse and print the linked list.
Example
Test Input

10
20
30
40
Expected Output

10->20->30->40->None
Confused about something? Ask a question!



# Replace ___ with your code

# create the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # take input for node data
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())

        # create 4 nodes with input values
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)

        # set head field to the first node
        self.head = node1

        # link the nodes
        node1.next = node2
        node2.next = node3
        node3.next = node4


    # method to traverse and print the nodes
    def traverse_linked_list(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

linked_list = LinkedList()

# create a linked list
linked_list.create_linked_list()

# print the linked list
linked_list.traverse_linked_list()
