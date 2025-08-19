Source Code: Delete Node at Given Position
In this program, we have used the delete_node() method to delete the node at the given position.

We have also added conditions to:

delete the first node if the position is 1
handle an empty linked list
handle positions greater than the number of nodes
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
Output

Original List:
80->9->14->None

After deleting node at position 2:
80->14->None

After deleting node at position 1:
14->None

Invalid position
After deleting node at position 10:
14->None
Confused about something? Ask a question!
