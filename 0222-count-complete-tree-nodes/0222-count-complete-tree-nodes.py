
class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        left = root
        right = root
        left_height = 0
        right_height = 0

        # Calculate the height by going left
        while left:
            left_height += 1
            left = left.left

        # Calculate the height by going right
        while right:
            right_height += 1
            right = right.right

        # If heights are equal, the tree is perfect
        if left_height == right_height:
            return (2 ** left_height) - 1

        # Otherwise, count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
