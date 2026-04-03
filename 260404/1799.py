# 시간 복잡도 O(N)

arr = input()
stack = []
result = 0

for i, x in enumerate(arr):
    # ( 를 만나면 막대기를 시작
    if x == "(":
        stack.append("(")
    # ) 를 만났는데, 이전 막대기가 ( (레이저 O)
    elif arr[i - 1] == "(" and x == ")":
        stack.pop()  # stack에서 막대기를 빼고,
        result += len(stack)  # 지금까지 살아있는 막대기의 수를 더한다
    # ) 를 만나면 막대기 끝 (레이저 X)
    else:
        stack.pop()  # stack에서 막대기를 빼고,
        result += 1  # 남은 막대기 수 하나를 더한다

print(result)