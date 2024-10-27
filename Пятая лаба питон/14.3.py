N = int(input())
minimal = 1e10
cnt = 0
ans = 0
for _ in range(N):
    x = int(input())
    if x == minimal:
        cnt += 1
    else:
        if cnt > ans:
            ans = cnt
        if x < minimal:
            minimal = x
            ans = 0
            cnt = 1
        else:
            cnt = 0
if cnt > ans:
    ans = cnt
print(ans)