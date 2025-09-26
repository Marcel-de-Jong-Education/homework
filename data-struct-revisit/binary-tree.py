class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Root:", root.value)
print("Left child of root:", root.left.value)
print("Right child of root:", root.right.value)
print("Left-Right grandchild:", root.left.right.value)
print("Right-Left grandchild:", root.right.left.value)
