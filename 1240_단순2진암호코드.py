import sys
sys.stdin = open('input.txt')

num = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    mat = [input() for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if mat[row][col] == '1':
                password = mat[row][col-55:col+1]

    pw=[]
    for i in range(8):
        for n in range(10):
            if num[n] == password[7*i:7*i+7]:
                pw.append(n)

    if ((pw[0]+pw[2]+pw[4]+pw[6])*3 + (pw[1]+pw[3]+pw[5]) + pw[7]) % 10 == 0:
        print(f'#{t+1} {sum(pw)}')
    else:
        print(f'#{t+1} {0}')



