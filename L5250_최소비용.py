import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra(start_x,start_y):
    queue = []
    heapq.heappush(queue,(0,[start_x,start_y]))
    fuel[start_x][start_y] = 0

    while queue:
        spend,node = heapq.heappop(queue)
        if spend <= fuel[node[0]][node[1]]:

            for i in range(4):
                nx = node[0]+dx[i]
                ny = node[1]+dy[i]

                if 0<=nx<N and 0<=ny<N:

                    if graph[nx][ny] > graph[node[0]][node[1]]:
                        sum_spend = spend + (graph[nx][ny] - graph[node[0]][node[1]] +1)
                    else:
                        sum_spend = spend+1


                    if sum_spend < fuel[nx][ny]:
                        fuel[nx][ny] = sum_spend
                        heapq.heappush(queue,(sum_spend,[nx,ny]))

T = int(input())

for t in range(T):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    fuel = [[float('inf')]*N for _ in range(N)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    dijkstra(0,0)
    print(f'#{t+1} {fuel[N-1][N-1]}')