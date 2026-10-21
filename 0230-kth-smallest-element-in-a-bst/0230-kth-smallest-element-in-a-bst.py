
class Solution:
    def kthSmallest(self, root, k):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        return values[k - 1]
