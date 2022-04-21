M, N = map(int,input().split())
def is_prime(x):
    if x == 1:
        return
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return
        return print(x)

for num in range(M,N+1):
    is_prime(num)