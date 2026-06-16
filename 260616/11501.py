# BOJ 11501 - 주식 (Greedy)
# 핵심 아이디어:
# 뒤에서부터 최고가를 추적한다.
# 현재 가격이 최고가보다 낮으면 → 사서 최고가에 판다 (이익 추가)
# 현재 가격이 최고가 이상이면 → 최고가 갱신
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    profit = 0
    max_price = 0
    for p in reversed(prices):
        if p > max_price:
            max_price = p
        else:
            profit += max_price - p
    print(profit)
