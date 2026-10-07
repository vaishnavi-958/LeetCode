class Solution:
    def flatten(self, root):
        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                predecessor = curr.left

                while predecessor.right:
                    predecessor = predecessor.right

                # Connect the original right subtree
                # to the rightmost node
                predecessor.right = curr.right

                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None

            # Move to the next node
            curr = curr.right