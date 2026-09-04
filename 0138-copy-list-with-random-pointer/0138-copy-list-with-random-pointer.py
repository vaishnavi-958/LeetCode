class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Map original node -> copied node
        old_to_new = {}

        # 1. Create a copy of every node
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # 2. Connect next and random pointers
        current = head
        while current:
            old_to_new[current].next = old_to_new.get(current.next)
            old_to_new[current].random = old_to_new.get(current.random)
            current = current.next

        # Return copied head
        return old_to_new[head]