Create a Linked List
We will now create a linked list using the Node class we created on the last page.

A Linked List
Figure: A Linked List
Let's create a LinkedList class to implement linked lists.

class LinkedList:
    def __init__(self):
        # initialize the head field to None
        self.head = None
Next, we will create a method to add nodes. For now, we will only add our first node to the linked list.

def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1
At this point, our linked list looks like this:

A Single Node
Figure: A Single Node
Next, we will add two more nodes to our linked list.

Confused about something? Ask a question!
