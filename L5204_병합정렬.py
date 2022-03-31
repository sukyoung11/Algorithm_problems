import sys
from collections import deque
sys.stdin = open('input.txt')

def merge_sort(num_list):
    if len(num_list) == 1:
        return num_list
    left = []
    right = []
    middle = len(num_list)//2
    for i in range(middle):
        left.append(num_list[i])
    for i in range(middle,len(num_list)):
        right.append(num_list[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    global cnt
    global result
    left = deque(left)
    right = deque(right)
    result = []
    if len(left) > 0 and len(right) > 0:
        if left[-1] > right[-1]:
            cnt += 1
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())

        elif len(left)>0:
            result.append(left.popleft())
        elif len(right)>0:
            result.append(right.popleft())

    return result


T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))
    num_list = deque(num_list)
    cnt = 0
    print(num_list)
    merge_sort(num_list)
    print(f'#{t+1} {result[len(result)//2]} {cnt}')