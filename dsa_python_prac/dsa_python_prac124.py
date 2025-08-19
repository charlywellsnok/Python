Sum of All Elements in a Linked List
Write a program to find the sum of all nodes in a linked list.

Create a Node class to represent a node.
Create a LinkedList class to represent the linked list data structure.
Within the LinkedList class, add the calculate_sum() method.
The calculate_sum() method should compute the sum of all the nodes and return the result.
Print the total sum outside of the classes.
Note: All necessary code, except for the calculate_sum() method, is provided for you in the editor.

Example
Test Input

9
1
1
Expected Output

11
Confused about something? Ask a question!













# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())

        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)

        self.head = node1
        node1.next = node2
        node2.next = node3

    # method to calculate sum of nodes
    def calculate_sum(self):

        # initialize total sum to 0
        total = 0

        current = self.head

        while current is not None:
            total += current.data
            current = current.next

        return total

# create a linked list
linked_list = LinkedList()
linked_list.create_linked_list()

# calculate sum of elements in linked list
total = linked_list.calculate_sum()
print(total)
