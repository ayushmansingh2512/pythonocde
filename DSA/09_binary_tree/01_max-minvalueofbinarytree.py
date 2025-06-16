from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_node_binary_tree(root):
	queue = deque([root])
	max_node = 0
	while queue:
		curr_node = queue.popleft()
		if curr_node.left:
			queue.append(curr_node.left)
		if curr_node.right:
			queue.append(curr_node.right)

		if curr_node.val> max_node:
			max_node = curr_node.val
	return max_node

# Sample Input
#       10
#      /  \
#     5    15
#    / \     \
#   2   7     20

root = TreeNode(10)
root.left = TreeNode(5, TreeNode(2), TreeNode(7))
root.right = TreeNode(15, None, TreeNode(20))

# Output
print(largest_node_binary_tree(root))  # Output: 20

