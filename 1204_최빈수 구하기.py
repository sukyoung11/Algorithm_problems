T = int(input())
for t in range(T):
    tc = int(input())
    numbers = list(map(int, input().split()))
    cnt_list = [0] * 1000

    for num in numbers:
        cnt_list[num] += 1

    max_num = max(cnt_list)
    for i in range(len(cnt_list) - 1, -1, -1):
        if cnt_list[i] == max_num:
            print(f'#{t + 1} {i}')
            break