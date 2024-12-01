# Реализация пузырьковой сортировки
def bubblesort(arr):
    n = len(arr) #Определяем длину массива
    is_sorted = False
    while not is_sorted: #Пока массив не отсортирован
        is_sorted = True #Сначала предполагаем массив отсортированным
        for j in range(n - 1):
            if arr[j] > arr[j + 1]: #Нашли неправильный порядок
                is_sorted = False #Значит массив не отсорт. нужно будет пройтись еще раз
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Восст. правильный порядок


def input_array():
    data = list(map(int, input("Введите элементы списка (через пробел): ").split()))
    return data

arr = input_array()
bubblesort(arr)
print(*arr)
