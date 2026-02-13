class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data , end = " ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end="")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="")

def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        current= queue.pop(0)
        print(current.data,end = "")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nLevel order Traversal:")
level_order(root)