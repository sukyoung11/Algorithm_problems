import sys
sys.stdin = open('input.txt')

def find_parent(parent,node):
    if parent[node] != node:
        parent[node] = find_parent(parent,parent[node])
    return parent[node]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

T = int(input())
for t in range(T):
    N = int(input())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    E = float(input())

    parent = [0]*(N+1)
    for i in range(N+1):
        parent[i] = i

    edges = []
    for i in range(N):
        for j in range(i+1,N):
            distance = (x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2
            edges.append((distance,i+1,j+1))

    edges.sort()
    result = 0
    for edge in edges:
        distance, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union(parent,a,b)
            result += distance

    print(f'#{t+1} {round(result*E)}')

