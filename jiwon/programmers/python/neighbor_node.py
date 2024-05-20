
def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if nh < 0 or nh >= len(board) or nw < 0 or nw >= len(board[0]):
            continue
        if board[h][w] == board[nh][nw]:
            answer += 1
    return answer
