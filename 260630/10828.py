# Stack: 스택 구현
# push, pop, size, empty, top 명령어 처리
# sys.stdout.write로 출력 최적화
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    stack = []
    result = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'push':
            stack.append(int(cmd[1]))
        elif cmd[0] == 'pop':
            result.append(stack.pop() if stack else -1)
        elif cmd[0] == 'size':
            result.append(len(stack))
        elif cmd[0] == 'empty':
            result.append(0 if stack else 1)
        elif cmd[0] == 'top':
            result.append(stack[-1] if stack else -1)
    print('\n'.join(map(str, result)))

main()
