class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def DFS(root):
    if root == None:
        return
    stack = [root]
    while stack :
        node = stack.pop()
        print(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


a = tree(1)
a.left = tree(2)
a.left.left = tree(3)
a.left.right = tree(4)
a.right = tree(2)
a.right.left = tree(4)
a.right.right = tree(3)
DFS(a)
