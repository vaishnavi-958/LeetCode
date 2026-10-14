
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # If root is empty or matches either target
        if root is None or root == p or root == q:
            return root

        # Search in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides find a target, current root is the LCA
        if left and right:
            return root

        # Otherwise, return whichever side found a target
        return left if left else right
