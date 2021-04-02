# -*- coding: utf-8 -*-
# Chapter 4 -> Quick Sort
import timeit


def main():
    # 4.1 -> 分儿治之
    sum_array = [2, 4, 6, 8, 10]
    print "Loop_sum: " + str(loop_Sum(sum_array))
    print "-----"

    sum_array = [2, 4, 6, 8, 10]
    print "exercise4_1: " + str(exercise4_1(sum_array))

    print "-----"
    count_array = [2, 4, 6, 8, 10]
    print "exercise4_2: " + str(exercise4_2(count_array))

    print "-----"
    BinarySearch_array = [2, 4, 6, 8, 10]
    BinarySearch_target = 8
    First_Index = 0
    Last_Index = len(BinarySearch_array) - 1
    print "exercise4_4: " + str(exercise4_4(BinarySearch_array, BinarySearch_target, First_Index, Last_Index))

    print "-----"
    quicksort_array = [2, 8, 7, 2, 4, 6, 9, 2, 1]
    print "Quick sort: " + str(quicksort(quicksort_array))


# 4.1 -> 分儿治之 (书:P45)
def loop_Sum(sum_array):
    total = 0
    for x in sum_array:
        total += x

    return total

    # 练习 4.1  -> Sum Array
def exercise4_1(sum_array):
    # When the sum_array is empty, return 0
    if len(sum_array) == 0:
        return 0

    # the pop value + recursion_Sum(new sum_array)
    return sum_array.pop() + exercise4_1(sum_array)

    # 练习 4.2  -> Count Array
def exercise4_2(count_array):
    if len(count_array) == 0:
        return 0
    count_array = count_array[1:]
    return 1 + exercise4_2(count_array)

    # 练习 4.3  -> Find Max
def exercise4_3(Max_array):
    if len(Max_array) == 0:
        return 0
    return max(Max_array.pop(), exercise4_3(Max_array))

    # 练习 4.4  -> Use recursion to do binary search
def exercise4_4(BinarySearch_array, BinarySearch_target, First_Index, Last_Index):
    if First_Index < Last_Index:
        Mid_index = (First_Index + Last_Index) / 2
        if BinarySearch_array[Mid_index] == BinarySearch_target:
            return Mid_index
        elif First_Index == Last_Index:
            return None
        elif BinarySearch_array[Mid_index] < BinarySearch_target:
            First_Index = Mid_index + 1
        else:
            Last_Index = Mid_index - 1

    return exercise4_4(BinarySearch_array, BinarySearch_target, First_Index, Last_Index)


# 4.2 -> 快排算法 (书:P52)
def quicksort(quicksort_array):
    if len(quicksort_array) < 2:
        return quicksort_array
    else:
        pivot = quicksort_array[0]
        # Cause the quicksort_array[0] selected as pivot (so exclude the pivot)
        less = [i for i in quicksort_array[1:] if i <= pivot]
        greater = [i for i in quicksort_array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


main()
