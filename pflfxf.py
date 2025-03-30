def permutations(x, m, perm):
    if len(perm) == len(x):
        for i in perm:
            print(x[i], end=' ')
        print()
        return
    for i in range(len(x)):
        if i in perm:
            continue
        if len(perm) > 0 and x[i] * x[perm[-1]] >= m:
            continue
        permutations(x, m, perm + [i])


x = list(map(int, input("Введите x1,...,xn: ").split()))
m = int(input("Введите М: "))
permutations(x, m, [])