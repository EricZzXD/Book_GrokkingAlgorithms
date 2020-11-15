# -*- coding: utf-8 -*-
# Chapter 2 -> Selection Sort


def main():
    # 2.1 -> 选择排序 (Selection Sort)
    sort_array = [6, 2, 7, 5, 3, 1, 8, 4, 9]
    C2_SelectionSort(sort_array)


# 2.1 -> 选择排序 (PDF: P14 或 书:P2)
#   -> 对数组进行排序
#   -> 运行效率: O(n^2)
def C2_SelectionSort(sort_array):
    # loop the array
    for i in range(len(sort_array)-1):
        # find the index of smallest value
        smallest = C2_SelectionSortSmallest(sort_array, i)
        # create a temp variable to store value of index 'i'
        temp_swap_1 = sort_array[i]
        # update index 'i' value
        sort_array[i] = sort_array[smallest]
        # the smallest index's value become the value of index of i
        sort_array[smallest] = temp_swap_1

    print sort_array


# This function is used to search the smallest index of the array
    # Sort_array: The array that need to sort
    # begin_index is the index of 'i'
def C2_SelectionSortSmallest(sort_array, begin_index):
    # a temp variable that store index of the smallest value
    temp = begin_index

    # loop the array to find the smaller value
    for Small in range(begin_index+1, len(sort_array)):
        # do comparison
        if sort_array[Small] < sort_array[temp]:
            # update temp when find a smaller value
            temp = Small

    # return the index of smallest value
    return temp


main()
