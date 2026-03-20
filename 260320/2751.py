import sys

input = sys.stdin.readline

N = int(input())
int_list = []

# 한줄씩 입력받아 리스트에 저장
for i in range(N):
    int_list.append(int(input()))

int_list.sort()

print(*int_list, sep="\n")
# print(*int_list) -> 한줄로 출력
# sep="\n" -> enter처리
