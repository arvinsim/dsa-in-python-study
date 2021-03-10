"""
=====
Factorial
=====
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(10))

"""
=====
Binary Search
=====
*Mar 10, 2021*
I modified the code to handle the IndexError exception when data[mid] doesn't exist(mid is out of bounds)
"""


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        try:
            mid = (low + high) // 2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                # Search the left part of the array
                return binary_search(data, target, low, mid - 1)
            else:
                # Search the right part of the array
                return binary_search(data, target, mid + 1, high)
        except IndexError:
            return False


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(data, 3, 0, len(data)))
print(binary_search(data, 8, 0, len(data)))
print(binary_search(data, 20, 0, len(data)))
