
class Solution:
    def getMinimumDifference(self, root):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        minimum = float('inf')

        for i in range(1, len(values)):
            difference = values[i] - values[i - 1]
            minimum = min(minimum, difference)

        return minimum
