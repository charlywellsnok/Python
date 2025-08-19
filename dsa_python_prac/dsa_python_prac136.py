Delete the First Node
Suppose we have the following linked list.

Linked List
Figure: Linked List
Process to Delete the First Node

We can simply remove the first node by making the second node as the new head node.

self.head = self.head.next
Move Head To Second Node
Figure: Move Head To Second Node
Idea Emoji
Note: For an empty linked list, we first need to check if the head exists. Otherwise, the code above results in an error.
Next, we will write a working program to delete the first node.

Confused about something? Ask a question!
