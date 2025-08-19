Source Code: Delete the First Node
Now, let's combine the code for deleting the first or head node.

# method to delete the first node
def delete_node(self):
    
    # if the linked list is not empty
    if self.head:

        # make second node as new head node
        self.head = self.head.next
Output

Original Linked List:
80->9->14->None

After deleting the first node - node(80):
9->14->None

After deleting the first node - node(9):
14->None
Idea Emoji
Note: A common practice during delete operation is to return the value of the node being deleted. This helps keep track of which node is being deleted.
Confused about something? Ask a question!
