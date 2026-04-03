import sys

input = sys.stdin.readline

N = int(input())
haveList = list(map(int, input().split()))

M = int(input())
findList = list(map(int, input().split()))

# findList에 있는 숫자가 HaveLIst에 몇개가있는지 검사

ansList = []

for f in findList:
    cnt = 0
    for h in haveList:
        if f == h:
            cnt += 1
    ansList.append(cnt)

print(*ansList, sep=" ")
