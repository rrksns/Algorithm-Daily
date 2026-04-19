import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = []
chk = [False] * (n + 1)


def recur(num):
    if num == m:
        print(" ".join(map(str, result)))
        return
    for i in range(1, n + 1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num + 1)
            chk[i] = False
            result.pop()


recur(0)
