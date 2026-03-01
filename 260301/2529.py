import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

results = []
used = [False] * 10

def dfs(depth, current):
    if depth == k + 1:
        results.append(''.join(map(str, current)))
        return
    for num in range(10):
        if not used[num]:
            # 첫 번째 숫자이거나 부등호 조건 만족하는 경우
            if depth == 0 or (signs[depth-1] == '<' and current[-1] < num) or (signs[depth-1] == '>' and current[-1] > num):
                used[num] = True
                current.append(num)
                dfs(depth + 1, current)
                current.pop()
                used[num] = False

dfs(0, [])

print(max(results))
print(min(results))