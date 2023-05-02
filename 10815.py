import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

dict = {}
for i in range(n):
    dict[cards[i]] = 0  # 아무 숫자로 mapping

for j in range(m):
    if checks[j] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')
