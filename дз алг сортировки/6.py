# arr = list(map(int, input().split()))
# m = int(input()) #Длина 1-го отрезка
# n = len(arr) - m #Длина 2-го отрезка
# for i in range(len(arr) // 2): #Переворачиваем массив, считаем одновременно с начала и с конца
#     arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
# for i in range(n // 2): #Восст. порядок во 2-м отрезке (ставшем 1-м)
#     arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
# for i in range(m // 2): #Восст. порядок во 1-м отрезке (ставшем 2-м)
#     arr[n + i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[n + i]
# print(*arr)

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
k = len(arr1)
l = len(arr2)
i, j = 0, 0
cnt = 0
while i < k or j < l:
    if i < k and (j == l or arr1[i] < arr2[j]):
        if i == 0:
            cnt += 1
        elif arr1[i] > arr1[i - 1]:
            cnt += 1
        i += 1
    elif j < l and (i == k or arr2[j] < arr1[i]):
        if j == 0:
            cnt += 1
        elif arr2[j] > arr2[j - 1]:
            cnt += 1
        j += 1
    else:
        if j == 0 and i == 0:
            cnt += 1
        elif arr2[j] > arr2[j - 1] and arr1[i] > arr1[i - 1]:
            cnt += 1
        j += 1
        i += 1
print(cnt)