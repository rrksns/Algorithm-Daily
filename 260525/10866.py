# 덱 (Deque) - 자료구조 구현
# 아이디어:
#   - Python의 collections.deque를 사용하여 O(1) push/pop 구현
#   - push_front: appendleft, push_back: append
#   - pop_front: popleft, pop_back: pop
#   - 빈 덱에서 pop/front/back 시 -1 반환

import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    dq = deque()
    output = []
    
    for _ in range(n):
        cmd = input().split()
        op = cmd[0]
        
        if op == 'push_front':
            dq.appendleft(int(cmd[1]))
        elif op == 'push_back':
            dq.append(int(cmd[1]))
        elif op == 'pop_front':
            output.append(dq.popleft() if dq else -1)
        elif op == 'pop_back':
            output.append(dq.pop() if dq else -1)
        elif op == 'size':
            output.append(len(dq))
        elif op == 'empty':
            output.append(0 if dq else 1)
        elif op == 'front':
            output.append(dq[0] if dq else -1)
        elif op == 'back':
            output.append(dq[-1] if dq else -1)
    
    print('\n'.join(map(str, output)))

main()
