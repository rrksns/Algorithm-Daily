# Queue: 프린터 큐
# 우선순위가 높은 문서 먼저 출력
# deque로 시뮬레이션: 현재 문서가 최대 우선순위가 아니면 뒤로 보내기
import sys
from collections import deque
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        docs = deque(enumerate(map(int, input().split())))
        count = 0
        while docs:
            idx, priority = docs.popleft()
            # 현재보다 높은 우선순위가 남아있으면 뒤로
            if any(priority < p for _, p in docs):
                docs.append((idx, priority))
            else:
                count += 1
                if idx == M:
                    print(count)
                    break

main()
