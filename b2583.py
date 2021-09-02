import sys
sys.stdin = open('input.txt')


def dfs():
    di = [-1, 0, 0, 1]
    dj = [0, 1, -1, 0]
    area = 0
    while stack:
        now = stack.pop(0)
        visited[now[0]][now[1]] = 1
        area += 1
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if (0 <= ni < N) and (0 <= nj < M) and (visited[ni][nj] == 0) and (board[ni][nj] == 0) and ([ni, nj]not in stack):
                stack.append([ni, nj])
    return area


M, N, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
for k in range(K):
    a, b, x, y = map(int, input().split())
    for i in range(a, x):
        for j in range(b, y):
            board[i][j] = 1

visited = [[0]*M for _ in range(N)]
stack = []
result = []
cnt = 0
for a in range(N):
    for b in range(M):
        if board[a][b] == 0 and visited[a][b] == 0:
            stack.append([a, b])
            cnt += 1
            result.append(dfs())
ans = sorted(result)
print(cnt)
print(*ans)