Insert Node in a Linked List
The program we wrote to insert a node doesn't work if:

the linked list is empty
the position is negative
the position is greater than the number of nodes.
Let's address these situations as well by creating a universal method to insert nodes. For this, we'll use the separate methods we just discussed as helpers.

# universal insert method
def insert_node(self, data, position=None):
    if position is None:
        self.append_node(data)
        return

    if position <= 0 or position > self.get_length() + 1:
        print("Invalid position")
        return

    if position == 1:
        self.insert_node_at_beginning(data)
    elif position == self.get_length() + 1:
        self.append_node(data)
    else:
        self.insert_node_at_position(data, position)
Output

Original Linked List:
80->9->14->None

After inserting 1 at position 1:
1->80->9->14->None

After inserting 15 without position:
1->80->9->14->15->None

Invalid position
After inserting 100 at position -1:
1->80->9->14->15->None

Invalid position
After inserting 50 at position 100:
1->80->9->14->15->None

After inserting 55 at position 3:
1->80->55->9->14->15->None
Confused about something? Ask a question!
