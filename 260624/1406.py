# 백준 1406: 에디터
# 두 개의 스택으로 커서 위치를 표현: left(커서 왼쪽), right(커서 오른쪽)
# L: left에서 pop → right에 push (커서 왼쪽 이동)
# D: right에서 pop → left에 push (커서 오른쪽 이동)
# B: left에서 pop (커서 왼쪽 문자 삭제)
# P $: left에 $ push (커서 왼쪽에 문자 삽입)
# 최종 출력: left 역순 + right 순서

import sys
input = sys.stdin.readline

def solve():
    word = input().strip()
    left = list(word)
    right = []

    m = int(input())
    for _ in range(m):
        cmd = input().split()
        op = cmd[0]
        if op == 'L':
            if left:
                right.append(left.pop())
        elif op == 'D':
            if right:
                left.append(right.pop())
        elif op == 'B':
            if left:
                left.pop()
        elif op == 'P':
            left.append(cmd[1])

    sys.stdout.write(''.join(left) + ''.join(reversed(right)) + '\n')

solve()
