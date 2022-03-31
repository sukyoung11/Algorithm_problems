import sys
sys.stdin = open('input.txt')

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    right = []
    left =[]
    center = [pivot]

    for number in numbers[1:]:
        if number<pivot:
            left.append(number)
        elif number>pivot:
            right.append(number)
        else:
            center.append(number)

    return quicksort(left)+ center + quicksort(right)

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    result = quicksort(numbers)
    print(f'#{t+1} {result[N//2]}')