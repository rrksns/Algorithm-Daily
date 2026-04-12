N, M = map(int, input().split())

numList = [i for i in range(0, N+1)]
# [0, 1, 2, 3, 4]

index = 0

def backTracking(result):

    # 개수에 맞게 꽉 찼다면 결과 출력
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        if (i not in result) and (len(result)==0 or i > result[-1]):
            result.append(numList[i])
            # 재귀로 백트래킹 실행
            backTracking(result)
            # 재귀 끝난 뒤 빠져나와서 바로 직전에 담았던 것 제거하기
            result.pop()

backTracking([])