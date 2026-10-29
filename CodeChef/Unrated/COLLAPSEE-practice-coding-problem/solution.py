# cook your dish here

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    ans = sum(abs(A[i]) for i in range(N - 2))
    ans -= A[N - 2]
    ans += A[N - 1]

    print(ans)
