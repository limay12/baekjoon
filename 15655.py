N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def sol(start):
    if len(answer) == M:
        print(*answer, sep=' ')
    for i in range(start, N):
        if arr[i] not in answer:
            answer.append(arr[i])
            sol(i + 1)
            answer.pop()
sol(0)
