Source Code: Append a Node
Here's the method to append a node:

# method to append a node at the end
def append_node(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return

    current = self.head
    while current.next:
        current = current.next
    current.next = new_node
Output

Original Linked List:
80->9->14->None

After appending 20:
80->9->14->20->None
Confused about something? Ask a question!
