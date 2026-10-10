
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            # Ignore negative paths
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Maximum path passing through this node
            path_sum = node.val + left + right

            self.max_sum = max(self.max_sum, path_sum)

            # Return the best one-sided path to the parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
