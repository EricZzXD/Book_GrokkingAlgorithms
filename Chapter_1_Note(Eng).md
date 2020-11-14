# 算法图解笔记 -> Chapter One

## 1.1 Intro
   - Binary Search -> P3
        - It is a search algorithm that finds the position of a target value within a sorted array
        - **logarithmic time in the worst case**: O(log n)
        - Principle of operation (Example)
            - array = [1,2,3,4,5,6,7,8,9], target = 8
            - mid_index = (low_index + high_index)/2 = (0+8)/2 = 4 
            - mid_index Value = array[mid_index] = 5 < target
            - New mid_index = (low_index + high_index)/2 = ((4+1)+8)/2 = 7 (due to new low_index = old mid_index + 1)
            - array[mid_index] = 8 == target 
            - return mid_index
            
            
