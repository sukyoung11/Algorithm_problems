import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(N):
    queue = deque()
    queue.append((N,0))
    num_list = [0]*1000001
    num_list[N] = 1

    while queue:
        N,c = queue.popleft()
        if 0 <= N + 1 < 1000001 and num_list[N+1] == 0:
            num_list[N+1]= 1
            queue.append((N+1, c+1))
        if 0 <= N-1 < 1000001 and num_list[N-1] == 0:
            num_list[N - 1] = 1
            queue.append((N-1, c + 1))
        if 0 <= N*2 < 1000001 and num_list[N*2] == 0:
            num_list[N * 2] = 1
            queue.append((N * 2, c + 1))
        if 0<= N-10 < 1000001 and num_list[N-10] == 0:
            num_list[N - 2] = 1
            queue.append((N - 10, c + 1))
        if num_list[M] == 1:
            return c+1

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    print(f'#{t+1} {bfs(N)}')

# visited 확인 안하면 runtime error, queue에 자료 넣을 떄는 turple
# from collections import deque
#
# def bfs(N):
#     queue = deque()
#     queue.append([N,0])
#
#     while queue:
#         N,c = queue.popleft()
#         for i in ['+1','-1','*2','-10']:
#             answer = cal(N,i)
#             if answer != M and 0<=answer<=1000000:
#                 queue.append([cal(N,i),c+1])
#
#             elif answer == M:
#                 queue = False
#                 return c+1
#
# def cal(N,x):
#     if x == '+1':
#         return N+1
#     elif x == '-1':
#         return N-1
#     elif x == '*2':
#         return N*2
#     else:
#         return N-10
#
# T = int(input())
# for t in range(T):
#     N, M = map(int,input().split())
#     print(f'#{t+1} {bfs(N)}')