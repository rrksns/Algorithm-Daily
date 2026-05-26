# 백준 1991 - 트리 순회
# 핵심 아이디어:
# 이진 트리의 전위(preorder), 중위(inorder), 후위(postorder) 순회
# 재귀 함수로 각 순회 방식 구현:
#   - 전위: 루트 → 왼쪽 → 오른쪽
#   - 중위: 왼쪽 → 루트 → 오른쪽
#   - 후위: 왼쪽 → 오른쪽 → 루트
# '.'는 자식 없음을 의미

import sys
input = sys.stdin.readline

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

n = int(input())
tree = {}
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

preorder('A'); print()
inorder('A'); print()
postorder('A'); print()
