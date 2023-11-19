import sys

class Node():
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

n = int(sys.stdin.readline())

tree = {}

for _ in range(n):
    m, l, r = sys.stdin.readline().split()
    tree[m] = Node(m, l, r)

def preorder(now):

    print(tree[now].node, end="")

    if tree[now].left != '.':
        preorder(tree[now].left)

    if tree[now].right != '.':
        preorder(tree[now].right)

def inorder(now):

    if tree[now].left != '.':
        inorder(tree[now].left)

    print(tree[now].node, end="")
    
    if tree[now].right != '.':
        inorder(tree[now].right)


def postorder(now):
    
    if tree[now].left != '.':
        postorder(tree[now].left)

    if tree[now].right != '.':
        postorder(tree[now].right)

    print(tree[now].node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')