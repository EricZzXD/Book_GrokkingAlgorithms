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
    print "exercise4_4: " + str(exercise4_3(BinarySearch_array, BinarySearch_target))


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
def exercise4_4(BinarySearch_array, BinarySearch_target):

    return


main()
