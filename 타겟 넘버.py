def solution(numbers, target):
    global total

    def dfs(x):
        global total
        for i in tree[x]:
            total += dfs(i)
            result.append(total)
            total -= i

    answer = 0
    tree = [[] for _ in range(51)]
    for i in range(len(numbers) - 1):
        tree[numbers[i]].append(numbers[i + 1])
        tree[numbers[i]].append(-numbers[i + 1])
    result = []
    total = 0
    dfs(numbers[0])