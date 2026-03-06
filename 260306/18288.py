import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def solve():
    N, K = map(int, input().split())

    # DP 상태 정의
    # - a_mod  : A가 푼 수 % K  (K=0이면 A는 0개만 가능)
    # - last   : 직전 문제를 푼 사람  (0=A, 1=B, 2=C, 3=초기)
    # - c_flag : C가 1개 이상 풀었는지  (0 or 1)
    # state 인덱스 = a_mod * 8 + last * 2 + c_flag
    # 총 상태 수  = mod_size * 8

    mod_size = K if K > 0 else 1
    S = mod_size * 8

    def idx(a_mod, last, c_flag):
        return a_mod * 8 + last * 2 + c_flag

    # 전이 행렬 구성
    trans = [[0] * S for _ in range(S)]
    for a_mod in range(mod_size):
        for last in range(4):
            for c_flag in range(2):
                src = idx(a_mod, last, c_flag)
                # A가 푸는 경우 (K=0이면 불가)
                if K > 0:
                    new_a = (a_mod + 1) % K
                    dst = idx(new_a, 0, c_flag)
                    trans[dst][src] = (trans[dst][src] + 1) % MOD
                # B가 푸는 경우 (직전이 B면 불가)
                if last != 1:
                    dst = idx(a_mod, 1, c_flag)
                    trans[dst][src] = (trans[dst][src] + 1) % MOD
                # C가 푸는 경우
                dst = idx(a_mod, 2, 1)
                trans[dst][src] = (trans[dst][src] + 1) % MOD

    # 행렬 곱셈
    def mat_mul(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if A[i][k] == 0:
                    continue
                for j in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    # 행렬 지수 승산
    def mat_pow(M, p):
        n = len(M)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while p:
            if p & 1:
                result = mat_mul(result, M)
            M = mat_mul(M, M)
            p >>= 1
        return result

    T = mat_pow(trans, N)
    init = idx(0, 3, 0)
    ans = sum(T[idx(0, last, 1)][init] for last in range(4)) % MOD
    print(ans)

solve()