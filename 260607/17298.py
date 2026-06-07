# 오큰수 (Next Greater Element)
# 스택에 인덱스를 저장, 현재 값이 스택 top의 값보다 크면 → top의 오큰수 확정
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
