Create a Linked List
Let's create the second node.

def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1

    # create the second node
    node2 = Node(9)

    # link the first and second nodes
    node1.next = node2
Here, we have created a node named node2 with value 9. We then linked it with node1 by assigning node2 to the next field of node1.

At this point, our linked list looks like this:

A Linked List With Two Nodes
Figure: A Linked List With Two Nodes
Let's add the third node as well.

def create_linked_list(self):

    # create the first node
    node1 = Node(80)

    # set the head field to the first node
    self.head = node1

    # create the second node
    node2 = Node(9)

    # link the first and second nodes
    node1.next = node2

    # create the third node
    node3 = Node(14)

    # link the second and third nodes
    node2.next = node3
This is how our linked list looks after adding three nodes.

A Linked List With Three Nodes
Figure: A Linked List With Three Nodes
Here,

The head is the first node in the linked list.
Each node is connected to each other.
The last node points to None.
Confused about something? Ask a question!
