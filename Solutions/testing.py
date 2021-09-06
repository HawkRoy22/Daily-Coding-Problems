"""
def hasCycle(self, head: ListNode) -> bool:
    # Create empty set for elements in linked list to be placed in to check against while iterating
    seen = set()
    # Establish the head of the ListNode we are iterating through
    cur = head
    # Create while loop that iterates in order to add Elements into the set
    while cur:
        # Checks Element against set to check if it's circular
        if cur in seen:
            return True
        # Adding iterated elements to set
        seen.add(cur)
        # Going to the next Element
        cur = cur.next
    # IF element is not circular return False
    return False
"""


class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(data)

#
#n1 = Node('eggs')
#n2 = Node('ham')
#n3 = Node('cheese')

#n1.next = n2
#n2.next = n3


#cur = n1
#while cur:
#    print(cur.data)
#    cur = cur.next
#

class SinglyLinkedList():
    def __init__(self):
        self.tail = None

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)

        # Check if there are any existing nodes in the list,
        if self.tail == None:
            self.tail = node
        # If there are none we make the new node the first node of the list, we traverse until we reach the end where we append the last node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
    # Creating 2 reference nodes for the compiler to check( FIRST NODE IN THE LIST & LAST NODE)
    def faster_append(self, data):
        node = Node(data)
        if self.head: # we append nodes through self.head
            self.head.next = node
            self.head = node
        else:
            self.tail = node # points toward first node in the list
            self.head = node


#words = SinglyLinkedList()
#words.append("chicken")
#words.append("chickfila")
#words.append("chipotle")

#current = words.tail
#while current:
#    print(current.data)
#    current = current.next