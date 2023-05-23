import sys
input = sys.stdin.readline

a, b  = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
answer = []

for i in a_set:
    if not i in b_set:
        answer.append(i)
answer.sort()

print(len(answer))
if len(answer) != 0:
    print(*answer)
