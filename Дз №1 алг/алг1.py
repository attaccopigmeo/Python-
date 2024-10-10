a = int(input())
b = int(input())
if a > b:
    d = b
else:
    d = a
while a % d != 0 or b % d != 0:
    d = d - 1
print(d)
 # работает очень долго при больших входных данных   