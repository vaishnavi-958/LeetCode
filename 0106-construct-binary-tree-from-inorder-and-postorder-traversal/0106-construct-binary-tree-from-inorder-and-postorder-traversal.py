class Solution:
    def buildTree(self, inorder, postorder):
        # Map each value to its index in inorder
        inorder_index = {
            value: i for i, value in enumerate(inorder)
        }

        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            # Last postorder element is the root
            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)

            # Because we're reading postorder backwards:
            # build RIGHT first, then LEFT
            mid = inorder_index[root_value]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)