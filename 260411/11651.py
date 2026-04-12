# import sys
# input = sys.stdin.readline
# n=int(input())
# li=[]
# for i in range(n):
#     a, b = map(int,sys.stdin.readline().split())
#     li.append([a,b])
# li.sort(key=lambda x: (x[1], x[0]))
# for i in li:
#     print(i[0], i[1])


import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

s_array = sorted(array)

for y, x in s_array:
    print(x, y)
