N = int(input())
board = [list(map(int, input())) for _ in range(N)]

def dfs(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]: # 같은 색이 아니면 분활
                check = -1
                break
                
    if check == -1:
        print("(", end='')
        n = n // 2
        dfs(x, y, n) # 왼쪽 위
        dfs(x, y + n, n) # 오른쪽 위
        dfs(x + n, y, n) # 왼쪽 아래
        dfs(x + n, y + n, n) # 오른쪽 아래
        print(")", end='')
    elif check == 0:
        print(0, end='')
    else:
        print(1, end='')
        
dfs(0, 0, N)
