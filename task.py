
import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Генеруємо набори даних різного розміру
small_data = [random.randint(0, 100) for _ in range(100)]
medium_data = [random.randint(0, 1000) for _ in range(1000)]
large_data = [random.randint(0, 10000) for _ in range(10000)]

# Замірюємо час сортування для кожного алгоритму на різних наборах даних
small_merge_sort_time = timeit.timeit(lambda: merge_sort(small_data), number=10)
medium_merge_sort_time = timeit.timeit(lambda: merge_sort(medium_data), number=10)
large_merge_sort_time = timeit.timeit(lambda: merge_sort(large_data), number=10)

small_insertion_sort_time = timeit.timeit(lambda: insertion_sort(small_data), number=10)
medium_insertion_sort_time = timeit.timeit(lambda: insertion_sort(medium_data), number=10)
large_insertion_sort_time = timeit.timeit(lambda: insertion_sort(large_data), number=10)

small_timsort_time = timeit.timeit(lambda: sorted(small_data), number=10)
medium_timsort_time = timeit.timeit(lambda: sorted(medium_data), number=10)
large_timsort_time = timeit.timeit(lambda: sorted(large_data), number=10)

# Виводимо результати
print("Merge Sort:")
print("Small Data:", small_merge_sort_time)
print("Medium Data:", medium_merge_sort_time)
print("Large Data:", large_merge_sort_time)

print("\nInsertion Sort:")
print("Small Data:", small_insertion_sort_time)
print("Medium Data:", medium_insertion_sort_time)
print("Large Data:", large_insertion_sort_time)

print("\nTimsort:")
print("Small Data:", small_timsort_time)
print("Medium Data:", medium_timsort_time)
print("Large Data:", large_timsort_time)
