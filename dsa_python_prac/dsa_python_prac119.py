Traverse Through the Linked List
Here are the steps involved in traversing a linked list:

1. Assign head to the current variable.

# get the address to the head of the list
current = self.head
Assign Head to Current Variable
Figure: Assign Head to Current Variable
2. Iterate until the current variable is None.

# iterate until current is None
# current is updated to the next node in each iteration

while current:
    current = current.next
Second Iteration

Traverse to the Next Node
Figure: Traverse to the Next Node
Third Iteration

Traverse to the Next Node
Figure: Traverse to the Next Node
If current.next is None, we know for sure that it is the last node.

Next, we will write a complete program to create and traverse a linked list.

Confused about something? Ask a question!
