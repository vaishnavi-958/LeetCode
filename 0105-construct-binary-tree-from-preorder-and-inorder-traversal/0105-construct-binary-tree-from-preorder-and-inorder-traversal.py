class Solution:
    def buildTree(self, preorder, inorder):

        # Store inorder positions for O(1) lookup
        inorder_map = {}

        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # No nodes in this range
            if left > right:
                return None

            # First element in preorder is the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find root in inorder
            root_index = inorder_map[root_value]

            # Build left subtree
            root.left = build(left, root_index - 1)

            # Build right subtree
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)