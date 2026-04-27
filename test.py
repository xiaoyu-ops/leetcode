import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        k = (m + n) // (n + 1)  # ceil(m / (n + 1))
        print(max(0, k * n - m))

solve()