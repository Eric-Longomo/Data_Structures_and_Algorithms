# Uses python3
import sys

def func1(x): return (int)(x - 1)


def func2(x): return (int)(x / 2)


def func3(x): return (int)(x / 3)


actions = [func1, func2, func3]


def optimal_sequence(m):
    min_sequence = [None] * (m + 1)

    min_sequence[0] = 0
    min_sequence[1] = 0

    sequence = []
    sequence.append([0])
    sequence.append([1])

    # 1 2 3 4 5 6 7 8 9 10
    # 1 1 1 2 3 2 3 3 2 3
    for i in range(2, m + 1):
        min_sequence[i] = float('inf')
        tmp2 = float('inf')
        tmp3 = float('inf')
        if (i % 3 == 0):
            tmp3 = min_sequence[func3(i)] + 1
        if (i % 2 == 0):
            tmp2 = min_sequence[func2(i)] + 1
        tmp1 = min_sequence[i - 1] + 1

        min_tmp = min(tmp1, tmp2, tmp3)

        min_sequence[i] = min_tmp
        if min_tmp == tmp1:
            sequence.append(sequence[func1(i)] + [i])
            continue
        if min_tmp == tmp2:
            sequence.append(sequence[func2(i)] + [i])
            continue
        if min_tmp == tmp3:
            sequence.append(sequence[func3(i)] + [i])

    return sequence[-1]

import math

def optimal_sequence2(n):
    # number of operations required for getting 0, 1, 2,.. , n
    num_operations = [0, 0] + [math.inf]*(n-1)

    for i in range(2, n+1):
        temp1, temp2, temp3 = [math.inf]*3

        temp1 = num_operations[i-1] + 1 
        if i%2 == 0: temp2 = num_operations[i//2] + 1
        if i%3 == 0: temp3 = num_operations[i//3] + 1
        min_ops = min(temp1, temp2, temp3)
        num_operations[i] = min_ops

    print(num_operations[n])

    # Backtracking the numbers leading to n
    nums = [n]
    while n!=1:
        if n%3 ==0 and num_operations[n]-1 == num_operations[n//3]:
            nums += [n//3]
            n = n//3
        elif n%2 ==0 and num_operations[n]-1 == num_operations[n//2]:
            nums += [n//2]
            n = n//2
        else:
            nums += [n-1]
            n = n - 1
    return ' '.join([str(i) for i in nums][::-1])

n = int(input())
optimal_sequence2(n)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
