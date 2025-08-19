Delete a Node at the Given Position
Suppose we have the following linked list.

Linked List
Figure: Linked List
Let's delete the fourth node from the above list.

Process to Delete a Node

To delete the fourth node, we can simply link the third node to the fifth node.

Link Third Node to Fifth Node
Figure: Link Third Node to Fifth Node
To implement it in our program, we traverse until we reach the third node.

1. Traverse until the current node is the node at position-1.

# delete node at this position
position = 4

current = self.head

    # the current variable is the node at (position - 1)
    for i in range(1, position - 1):
        current = current.next
2. Link the node at position-1 to position+1.

Link the next attribute of the current node to the node at position + 1.

current.next = current.next.next
Link Third Node to Fifth Node
Figure: Link Third Node to Fifth Node
Idea Emoji
Note: The above code cannot be used to delete the node at the first position.
Next, we will write a working program to delete a node at the given position.

Confused about something? Ask a question!
