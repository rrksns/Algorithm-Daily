import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

# 상, 하, 좌, 우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = 1  # 테스트 케이스 번호

while True:
    N = int(input())
    if N == 0:  # 0이 입력되면 프로그램 종료
        break

    # 동굴(맵) 정보 입력받기
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 잃는 루피의 최소 금액을 저장할 2차원 최단 거리 테이블 초기화
    distance = [[INF] * N for _ in range(N)]

    # 우선순위 큐 초기화
    heap = []

    # 시작점 설정: (누적 잃은 루피, x좌표, y좌표)
    # 중요: (0, 0) 칸에 있는 루피도 잃고 시작함!
    start_cost = graph[0][0]
    heapq.heappush(heap, (start_cost, 0, 0))
    distance[0][0] = start_cost

    while heap:
        dist, x, y = heapq.heappop(heap)

        # 목표 지점 (N-1, N-1)에 도달했다면 정답 출력 후 탐색 종료
        # 우선순위 큐(최소 힙)를 사용했기 때문에, 목적지를 처음 꺼낸 순간이 무조건 최솟값입니다.
        if x == N - 1 and y == N - 1:
            print(f"Problem {tc}: {distance[x][y]}")
            break

        # 이미 처리된 적 있는 좌표라면 무시 (최적화)
        if distance[x][y] < dist:
            continue

        # 현재 위치에서 상하좌우 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵의 범위를 벗어나지 않는 경우에만 진행
            if 0 <= nx < N and 0 <= ny < N:
                # 다음 칸으로 이동했을 때의 누적 비용
                cost = dist + graph[nx][ny]

                # 새로 계산한 비용이 기존에 알려진 다음 칸까지의 비용보다 저렴하다면 갱신
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))

    tc += 1  # 다음 테스트 케이스를 위해 번호 증가
