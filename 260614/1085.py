# 직사각형에서 탈출
# 현재 위치 (x, y)에서 가로 w, 세로 h인 직사각형 경계까지의 최솟값
# 상하좌우 4방향 중 가장 가까운 경계까지의 거리 = min(x, y, w-x, h-y)
import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))
