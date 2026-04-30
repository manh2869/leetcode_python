class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def isSameTree(p, q):
    pass


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.right = TreeNode(7)
a.right.left = TreeNode(6)

  
inorder(a)
