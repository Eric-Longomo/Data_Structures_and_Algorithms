# Uses python3
import sys
import random

def partition3(a, left, right):
    #write your code here
    pivot_value = a[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition2
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def randomized_quick_sort_3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort_3(a, l, m[0] - 1);
    randomized_quick_sort_3(a, m[1] + 1, r);
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort_3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
