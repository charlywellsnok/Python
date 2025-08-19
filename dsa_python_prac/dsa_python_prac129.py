Append a Node
Let's append a node with the data 20 to the linked list we previously mentioned. Here's how we can do it:

1. Create a new node.

We will use the Node class we discussed in the previous lesson to create a new node.

new_node = Node(20)
Create a Node
Figure: Create a Node
2. Traverse until the last node of the linked list is reached.

Since we need to insert a node at the end, we must traverse until we reach the last node. We will add the new node after the last node.

# code snippet to find the last node

# current variable points to the head node
current = self.head

# traverse until the last node (node pointing to None)
while current:
    current = current.next
Traverse to the Last Node
Figure: Traverse to the Last Node
3. Add a new node after the last node (current node).

current.next = new_node
Add a Node After the Current Node
Figure: Add a Node After the Current Node
Confused about something? Ask a question!
