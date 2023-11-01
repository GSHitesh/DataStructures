from typing import List, Optional

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_traversal(node):
            nonlocal prev, max_count, current_count, modes

            if not node:
                return

            # Recursively traverse the left subtree
            in_order_traversal(node.left)

            # Check if the current element is the same as the previous element
            if node.val == prev:
                current_count += 1
            else:
                current_count = 1

            # Update the mode if the current count is greater than the maximum count
            if current_count > max_count:
                max_count = current_count
                modes = [node.val]
            elif current_count == max_count:
                modes.append(node.val)

            prev = node.val

            # Recursively traverse the right subtree
            in_order_traversal(node.right)

        if not root:
            return []

        prev = None
        max_count = 0
        current_count = 1
        modes = []

        in_order_traversal(root)

        return modes
