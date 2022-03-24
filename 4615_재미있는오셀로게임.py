import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    mat = [[0]*N for _ in range(N)]
    mat[N//2-1][N//2-1] = 2  # 초기설정
    mat[N//2][N//2] = 2
    mat[N//2-1][N//2] = 1
    mat[N//2][N//2-1] = 1
    dx=[0,1,0,-1,1,1,-1,-1]  # 방향설정
    dy=[1,0,-1,0,1,-1,-1,1]

    for i in range(M):
        play = list(map(int,input().split()))
        mat[play[0]-1][play[1]-1] = play[2]  # 돌 놓기
        for d in range(8):  # 가로,세로,대각선 방향으로 탐색하며 상대편 돌 바꾸기
            k=1;x=0;y=0
            while 0 <= play[0]-1+dx[d]*k < N and 0 <= play[1]-1+dy[d]*k < N:
                x=play[0]-1+dx[d]*k
                y=play[1]-1+dy[d]*k
                if mat[x][y]==play[2]:  # 자기 색이랑 같은 돌 찾으면,
                    for c in range(1,k):  # 그 사이에 있는 돌들이 바뀜
                        mat[play[0]-1+dx[d]*c][play[1]-1+dy[d]*c] = play[2]
                    break
                elif mat[x][y] == 0:  # 빈공간이 나오면 break
                    break
                k += 1
        print(mat)

    cnt1 = 0
    cnt2 = 0
    for row in range(N):  # 게임 끝나고 돌 개수 세기
        for col in range(N):
            if mat[row][col]==1:
                cnt1+=1
            elif mat[row][col]==2:
                cnt2+=1
    print(f'#{t+1} {cnt1} {cnt2}')






