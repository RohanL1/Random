# Randoimized serach algo for finding element in gievn list/Array

import random

def random_search(arr, x):
    visited = set()
    while len(visited) < len(arr):
        i = random.randint(0, len(arr) - 1)
        if i not in visited:
            visited.add(i)
            if arr[i] == x:
                return i
    return -1

A = [3, 5, 7, 2, 8, 1, 9, 4, 6]
key = 5
print(A)
print("search key = {}".format(key))
print(random_search(A, key))