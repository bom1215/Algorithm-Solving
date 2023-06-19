from collections import deque

def solution(board):
    answer = -1
    x,y = 0, 0
    q = deque([(x,y,-1,0)])
    n = len(board)
    arr = [[[-1] for _ in range(n)] for _ in range(n)]
    while q:
        x,y,direc,money = q.popleft()
        # arr[x][y] = money
        if x == n-1 and y == n-1 and (answer > money or answer ==-1):
            answer = money

        next_step = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        for i, (new_x, new_y) in enumerate(next_step):
            if new_x >= len(board) or new_y>= len(board) or new_x < 0 or new_y < 0: # 경계
                continue

            if i ==direc or direc == -1:
                cost = 100
            else:
                cost = 600
            if board[new_x][new_y]: # 벽
                continue
            if arr[new_x][new_y][0] !=-1:
                if arr[new_x][new_y][0] < money+cost: #재방문
                    if len(arr[new_x][new_y]) <=10:
                        arr[new_x][new_y].append(money+cost)
                    else:
                        continue
                else:
                    arr[new_x][new_y] = [money+cost]
            else:
                arr[new_x][new_y] = [money+cost]
            q.append((new_x, new_y, i, money+cost))
                
    return answer