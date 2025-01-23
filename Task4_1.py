import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def timsort(arr):
    return sorted(arr)


def generate_data(size, order='random'):
    if order == 'sorted':
        return list(range(size))
    elif order == 'reverse':
        return list(range(size, 0, -1))
    elif order == 'partial':
        arr = list(range(size))
        for i in range(size // 10):
            j = random.randint(0, size - 1)
            arr[j] = random.randint(0, size)
        return arr
    else:
        return [random.randint(0, size) for _ in range(size)]


def time_algorithm(algorithm, arr):
    setup_code = f"from __main__ import {algorithm.__name__}"
    stmt = f"{algorithm.__name__}({arr})"
    times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=1)
    return min(times)


def main():
    sizes = [1000, 5000, 10000] 
    orders = ['random', 'sorted', 'reverse', 'partial']
    algorithms = [insertion_sort, merge_sort, timsort]

    print(f"{'Algorithm':<15}{'Time (seconds)':>15}")
    for size in sizes:
        print(f"\nData Size: {size}")
        for order in orders:
            print(f"\nOrder: {order}")
            data = generate_data(size, order=order)
            print("-" * 30)
            for algorithm in algorithms:
                arr = data.copy()
                time_taken = time_algorithm(algorithm, arr)
                print(f"{algorithm.__name__:<15}{time_taken:>15.6f}")
        print("-" * 30)

if __name__ == '__main__':
    main()