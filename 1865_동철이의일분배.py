import sys
sys.stdin = open('input.txt')

def dfs(person,per):
    global max_percent
    if person == N:
        if per > max_percent:
            max_percent = per
        return
    if per == 0:
        return
    if per <= max_percent:
        return

    for col in range(N):
        if visited[col] == 0:
            a=per*percent[person][col]/100
            visited[col] = 1
            dfs(person+1,a)
            visited[col] = 0


T = int(input())
for t in range(T):
    N = int(input())
    percent = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    max_percent = 0
    dfs(0,1)
    print(f'#{t+1} {round(max_percent*100,6):.6f}')



    # max_per = 0
    # result = 1
    # for i in range(N):
    #     max_per = 0
    #     for row in range(len(percent)):
    #         for col in range(len(percent)):
    #             if percent[row][col]> max_per:
    #                 max_row = row
    #                 max_col = col
    #                 max_per = percent[row][col]
    #
    #     result *= (max_per*0.01)
    #
    #     for k in range(N):
    #         percent[max_row][k] = 0
    #         percent[k][max_col] = 0
    #
    #
    # print(f'#{t+1} {round(result*100,6)}')


