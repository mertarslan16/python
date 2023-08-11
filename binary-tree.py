class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Input list
lst = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# Create the root node
root = None
for val in lst:
    root = insert(root, val)

print("Inorder traversal of the BST:")
inorder_traversal(root)