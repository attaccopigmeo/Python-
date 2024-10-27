def max_digit(N):
    if N < 10:
        return N
    d1 = N % 10
    d2 = max_digit(N // 10)
    if d1 > d2:
        return d1
    else:
        return d2
    
    
N = int(input())
print(max_digit(N))