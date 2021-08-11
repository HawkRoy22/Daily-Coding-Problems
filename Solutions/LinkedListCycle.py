class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




def hasCycle(self, head: ListNode) -> bool:

    seen = set()
    cur = head
    while cur:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next
    return False


hasCycle([[3,2,0,-4]])