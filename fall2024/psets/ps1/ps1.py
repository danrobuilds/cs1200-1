from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    
    n = len(arr)
    
    k = math.ceil(math.log(univsize, base))
    
    # Convert all K_i to their base-b representation
    base_b_keys = [(BC(K, base, k), V) for K, V in arr]
    
    # Perform sorting for each digit from least significant to most significant
    for j in range(k):
    
        key_digit_pairs = []

        for i in range(n):
            K_prime = base_b_keys[i][0][j]  # get the j-th digit from the base-b key
            key_digit_pairs.append((K_prime, base_b_keys[i]))  # (digit, (K_prime, V))

        sorted_by_digit = singletonBucketSort(base, key_digit_pairs)
        
        base_b_keys = [item[1] for item in sorted_by_digit]
    
    # Reconstruct the sorted array
    sorted_arr = []
    for base_b_key, V in base_b_keys:
        # Convert back from base-b digits to integer key
        K = sum(base_b_key[i] * (base ** (k - 1 - i)) for i in range(k))
        sorted_arr.append((K, V))
    
    return sorted_arr