class Solution:
    def connect(self, root):
        if not root:
            return None

        leftmost = root

        while leftmost:

            # Build the next level
            curr = leftmost
            prev = None
            next_leftmost = None

            while curr:

                # Process left child
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        next_leftmost = curr.left

                    prev = curr.left

                # Process right child
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        next_leftmost = curr.right

                    prev = curr.right

                # Move to the next node in the current level
                curr = curr.next

            # Last node of the level points to NULL
            if prev:
                prev.next = None

            # Move to the next level
            leftmost = next_leftmost

        return root