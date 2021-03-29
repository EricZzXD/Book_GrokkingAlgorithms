# -*- coding: utf-8 -*-
# Chapter 1 -> Algorithm Introduction
import timeit


def main():
    # 1.1 -> 二分法 (Binary Search)
    binary_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    binary_target = 8
    C1_BinarySearch(binary_array, binary_target)


# 1.1 -> 二分法 (PDF: P14 或 书:P2)
#   -> 二分法的前提需要排列数据
#   -> 运行效率: O(log n)
def C1_BinarySearch(binary_array, binary_target):
    low_index = 0
    high_index = len(binary_array)-1

    # Compare if low == high and cannot find the match -> Cant find the target
    while low_index < high_index:
        mid_index = (low_index + high_index)/2
        guess = binary_array[mid_index]
        if guess == binary_target:
            print "Index: " + str(mid_index)
            return mid_index
        elif binary_target < guess:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return False


main()
