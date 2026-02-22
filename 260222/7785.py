import sys
input = sys.stdin.readline

n = int(input())
company = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        company.add(name)
    else:
        company.discard(name)

# 사전 역순 출력
for name in sorted(company, reverse=True):
    print(name)