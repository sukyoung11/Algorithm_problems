import sys
sys.stdin = open('input.txt')

def charge(now,change):
    global min_change
    if change >= min_change:  # 최소 교환 횟수를 넘어가면 재귀 중지
        return

    if now >= N-1: # 목표지점 도착
        if change < min_change:  # 기존 최소 교환 횟수보다 작으면 갱신
            min_change = change
        return

    for i in range(1,1+charger[now]):  # 충전 가능한 경우 모두 구하기
        now += i
        charge(now,change+1)
        now-=i

T = int(input())
for t in range(T):
    info = list(map(int,input().split()))
    N = info[0]
    charger = list(info[1:])
    min_change = float('inf')
    charge(0,0)

    print(f'#{t+1} {min_change-1}')


