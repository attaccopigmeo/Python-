"""
Сортировка простым выбором — это алгоритм сортировки, который работает,//
находя наименьший (или наибольший) элемент в неотсортированной части массива//
и перемещая его в начало (или конец) массива.//
Этот процесс повторяется, пока массив не будет отсортирован.
"""
def selection_sort(array):
    for i in range(len(array)): #Проходим по каждому элементу массива
        min_index = i #Предполагаем текущий элемент минимальным
        #Ищем наименьший эл. в оставшейся части массива
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        #Меняем местами текущий и найденный минимальный
        array[i], array[min_index] = array[min_index], array[i]
    return array


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Not sorted array:", numbers)
print("Already sorted array:", selection_sort(numbers))