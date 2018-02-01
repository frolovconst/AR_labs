from numpy import random

calls = 0

#
# Quicksort
#

def do_quicksort(A):
    global calls
    calls = 0
    quicksort(A, 0, len(A)-1)
    return calls

def quicksort(A, lo, hi):
    global calls
    calls += 1
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] < pivot:
            i = i + 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    if A[hi] < A[i+1]:
        temp = A[i+1]
        A[i+1] = A[hi]
        A[hi] = temp
    return i + 1

#
# Randomized QuickSort
#


def do_r_quicksort(A):
    global calls
    calls = 0
    r_quicksort(A, 0, len(A) - 1)
    return calls

def r_partition(A,lo,hi):
    # %%% PLACE YOUR CODE HERE %%%
    
    # %%% END YOUR CODE HERE %%%
    return partition(A,lo,hi)

def r_quicksort(A,lo,hi):
    global calls
    calls += 1
    if lo<hi:
        p = r_partition(A,lo,hi)
        r_quicksort(A, lo, p - 1)
        r_quicksort(A, p + 1, hi)
