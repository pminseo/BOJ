import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])

def mid(root):
    if root != '.':
        mid(tree[root][0])
        print(root, end='')
        mid(tree[root][1])

def ove(root):
    if root != '.':
        ove(tree[root][0])
        ove(tree[root][1])
        print(root, end='')

pre('A')
print()
mid('A')
print()
ove('A')