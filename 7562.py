from collections import deque
import sys
input = sys.stdin.readline

dx = [1,2,-1,-2,-2,-1,1,2]
dy = [2,1,2,1,-1,-2,-2,-1]

def bfs():
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < l and 0<= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

n = int(input())
for _ in range(n):
    l = int(input())
    sx, sy = map(int, input().rstrip().split())
    ex, ey = map(int, input().rstrip().split())
    graph = [[0]*l for _ in range(l)]
    graph[sx][sy] = 1
    print(bfs())
