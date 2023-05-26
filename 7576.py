import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1
         
bfs()
answer = 0
for i in graph:
    for j in i:
        # 익지 않은 토마토가 있다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 모든 토마토가 익어있는 상태이면 최댓값
    answer = max(answer, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(answer - 1)
