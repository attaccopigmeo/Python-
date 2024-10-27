def Sum(N):
    if N == 1:
        return 1.0
    return Sum(N-1) + 1 / ((-2) ** (N - 1))


N = int(input())
print(Sum(N))