Append Element to an Empty Linked List
The code we discussed for appending to a linked list does not work if the linked list is empty.

If you recall the LinkedList class we introduced in the previous lesson, its head attribute is initially set to None.

class LinkedList:
    def __init__(self):
        self.head = None
This means that the head attribute of an empty linked list is None.

Therefore, to append a new node to an empty linked list, we will simply set head to point to new_node.

if not self.head:
    self.head = new_node
    return
Point Head to New Node
Figure: Point Head to New Node
Confused about something? Ask a question!
