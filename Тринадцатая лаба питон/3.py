"""
К-ичные числа. Среди чисел в системе счисления с основанием K (2≤K≤10)
определить сколько имеется чисел из N (1<N<20, N+K<26) разрядов таких, что в их записи
содержится более трех подряд идущих нулей.
"""
import itertools

N = int(input())
K = int(input())
# Найдём количество чисел, не содержащих четырёх идущих подряд нулей (назовём такие числа корректными)
dp = [None for _ in range(N + 1)]
dp[0] = 1 # корректных чисел из 0 цифр одна
# корректные числа из 1, 2, 3, 4 цифр - все такие числа (0 не учитываем)
dp[1] = K - 1
dp[2] = (K - 1) * K
dp[3] = (K - 1) * K * K
dp[4] = (K - 1) * K * K * K
# Мы получим корректное число, дописав к корректному любую ненулевую цифру
# Также к корректной последовательности мы можем дописать ненулевую цифру и от одной до трёх 0
for i in range(4, N + 1):
    dp[i] = (K - 1) * (dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4])
# Ответом является количество НЕкорректных чисел
res = (K - 1) * K ** (N - 1) - dp[N]
print("Ответ:", res)
# ответы не сходятся, т.к. в программе считается, что числа не могут начинаться с 0