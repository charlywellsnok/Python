Delete Node at Given Position
Can you write a program to delete a node from a given linked list?

Add the delete_node() method to the LinkedList class, following the outline provided in the editor.
The delete_node() method takes a single argument, position, and should delete the node at that position.
Then print the linked list by calling the display() method.
For example, the starting linked list will always be:

90->80->60->50
If we pass 2 as the position, the resulting linked list should become:

90->60->50
Example
Test Input

2
Expected Output

90->60->50->None
Confused about something? Ask a question!










# Replace ___ with your code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 8->3->9->7->6
        # create linked list
    def create_linked_list(self):
        node1 = Node(90)
        self.head = node1

        node2 = Node(80)
        node1.next = node2

        node3 = Node(60)
        node2.next = node3

        node4 = Node(50)
        node3.next = node4


    # print in format: A->B->C->None
    def display(self):
        current = self.head

        while current:
            print(f"{current.data}", end="->")
            current = current.next

        print(None)

    # method to get the length of the linked list
    def get_length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # method to delete a node at the given position
    def delete_node(self, position):
        # Check if the position is valid
        if position <= 0 or position > self.get_length():
            print("Invalid position")
            return

        # if linked list is empty
        if not self.head:
            return

        # condition to delete node at the first position
        if position == 1:
            self.head = self.head.next
            return

        current = self.head

        # Traverse the list to find the node before the one to be deleted
        for i in range(1, position - 1):
            # condition to handle if position
            # is greater than number of nodes
            if not current.next:
                return
            current = current.next

        # current.next is the node to be deleted
        # current.next.next is the node after the node to be deleted
        if current.next:
            current.next = current.next.next

linked_list = LinkedList()
linked_list.create_linked_list()

linked_list = LinkedList()
linked_list.create_linked_list()

# the position of the new node
position = int(input())

# delete the linked list at the give position
linked_list.delete_node(position)

linked_list.display()
