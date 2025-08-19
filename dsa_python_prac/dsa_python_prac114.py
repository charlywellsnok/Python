Create a Linked List
Since a linked list is a collection of connected nodes, let's first learn to create nodes.

Create a Node
As mentioned before, a node stores data and the address of the next node.

A Node
Figure: A Node
Let's implement a node in our Python code.

class Node:

    def __init__(self, data):   
        self.data = data
        self.next = None
Here, the Node class has two fields:

data - to store the element
next - to store the address to the next node
Idea Emoji
Note: We have initialized the value of next to None because, currently, there are no nodes after it.
Now, we can create nodes and add data to them.

node1 = Node(11)
node2 = Node(2)
node3 = Node(88)
Next, we will create a linked list by connecting the nodes above.

Confused about something? Ask a question!
