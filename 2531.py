N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
eat = []
answer = 0

for i in range(N):
    for j in range(k):
        if i + j > N - 1:
            eat.append(arr[(i + j) % N])   
        else:
            eat.append(arr[i + j])
    if c in eat:
        answer = max(answer, len(set(eat)))
    else:
        answer = max(answer, len(set(eat)) + 1)
    if answer == k + 1:
        break
    eat = []
                 
print(answer)
