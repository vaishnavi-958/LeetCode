class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # Check if this is a leaf node
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Subtract current node's value
        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )