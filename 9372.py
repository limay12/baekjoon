import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
    print(n-1)
