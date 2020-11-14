# Grokking_Algorithm_Note -> Chapter One: Introduction to Algorithms 

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
            
   - EXERCISES -> P9
        - **1.1**: Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?
            - 7 Steps (128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1)

        - **1.2**: Suppose you double the size of the list. What’s the maximum number of steps now?
            - 8 steps due binary search eliminate half of the size every time it process  

## 1.2 Running time -> No Note -> P10

## 1.3 Big O Notation -> P10
   - Big O establishes a worst-case run time
   - Some common Big O run times -> P15
       - O(log n), also known as log time. Example: **Binary search**.
       - O(n), also known as linear time. Example: **Simple search**.
       - O(n * log n). Example: A fast sorting algorithm, like **quicksort**        (coming up in chapter 4).
       - O(n2). Example: A slow sorting algorithm, like **selection sort** (coming up in chapter 2).
       - O(n!). Example: A really slow algorithm, like the **traveling salesperson** (coming up next!).
       
   - EXERCISES -> P17
       - 1.3 You have a name, and you want to find the person’s phone number in the phone book.
            - O(log n) -> As the phone book is ordered by the name 
            
       - 1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)
            - O(n) -> Need to go through all the phone number to get the wanted one
            
       - 1.5 You want to read the numbers of every person in the phone book.
            - O(n) -> Read through all the people 
       
       - 1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)
            - O(n) -> Dont know yet 
            
            
   - The traveling salesperson -> P17
        - The Big O runtime: O(n!)
        - Question: a salesperson has to go to five cities. Wants to hit all five cities while traveling the minimum distance.
            - There are 120 Operations to solve the problem for 5 cities: 5*4*3*2*1 = 120
            
            
## Recap
   - Binary search is a lot faster than simple search.
   - O(log n) is faster than O(n), but it gets a lot faster once the list of items you’re searching through grows.
   - Algorithm speed isn’t measured in seconds.
   - Algorithm times are measured in terms of growth of an algorithm.
   - Algorithm times are written in Big O notation.