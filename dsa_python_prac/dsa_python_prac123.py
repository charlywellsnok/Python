Example: Count Number of Nodes
In this example, we will count the number of nodes in a linked list.

To address this problem, we will traverse the linked list and increment a counter for each node we encounter.

# method to count elements in a linked list
def count_elements(self):
    current = self.head
    # initialize count to zero
    count = 0

    while current:
        #increment the count for each node encountered 
        count += 1
        # traverse to the next node
        current = current.next
# return count once all nodes are visited
return count
Output

Count = 3
Confused about something? Ask a question!






