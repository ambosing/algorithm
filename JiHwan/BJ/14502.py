import copy
from collections import deque


def bfs():
    q = deque()
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m or 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((dx, dy))


def make_graph(x):
    matrix = [list(map(int, input().split())) for _ in range(x)]
    return matrix


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = make_graph(n)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0






