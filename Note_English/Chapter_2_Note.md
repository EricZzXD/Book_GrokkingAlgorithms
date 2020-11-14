# Grokking_Algorithm_Note -> Chapter Two: Selection Sort  

## 2.1 How Memory Works -> P23
   - Your computer looks like a giant set of drawers, and each drawer has an address.
   - When require to store Data into the memory, request a some space from the computer, and the computer give back an memory address
   - Memory Address Example: fe0ffeeb  
   
## 2.2 Array and Linked Lists -> P24
   - Array -> P26
       - Features 
           - Read: O(1)
           - Add: O(n)
           - The reserved space within memory are connected 
           - Have to define how big the spaces that needed before usage 
           - Reserved Space > Actual Usage -> Waste of space 
           - Reserved Space > Actual Usage -> Reallocate the data 
           
       - Advantage 
           - Easy to implement 
           - Read Data with high efficiency
           
       - Disadvantage 
           - Add or delete data with low efficiency 
       
   - Linked Lists -> P25
       - Features
           - Read: O(n)
           - Add: O(1)
           - each item store the address of the next item in the list that make a bunch of random memory addresses are linked together  
           - Add new Item -> Add the new Item's memory address into the Item before  
           - Delete Item -> Replace the deleted item's memory Address 

       - Advantage 
           - Add and Delete with high efficiency
       
       - Disadvantage 
           - Read Item with low efficiency (due to linked lists store the items randomly, requires to read the items one by one to get the next item's memory address)
           
   - EXERCISE -> P28 and P31
       - 2.1: Suppose you’re building an app to keep track of your finances. Every day, you write down everything you spent money on. At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list? 
           - Linked list -> The Insertion operation relatively often compare to read, linked list is more suitable as the add efficiency is high
           
       - 2.2: Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders off the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it. <br>
            Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)        
           - Linked list -> Add and delete operation are more often and always read from the first one. 
           
       - 2.3: Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list?
           - Array -> Linked list cannot read items randomly (without knowing the memory address). for read data, array with higher efficiency
           
       - 2.4: People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array? 
           - Require to sort the array (Binary Search requires to operate an sorted array)
           - If the reserved space is not enough, requires to reallocate the data 
           - Insertion is slow in array 
           
       - 2.5: In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with a. The second slot points to a linked list containing all the usernames starting with b, and so on. Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the linked list for slot 1, and add Adit it B at the end. Now, suppose you want to search for Zakhir H. <br>
            You go to slot 26, which points to a linked list of all the Z names. Then you search through that list to find Zakhir H. Compare this hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You don’t have to give Big O run times, just whether the new data structure would be faster or slower.
           - Search operation will be slower than array, but faster than linked list 
           - Insertion will be faster than array, same as linked list (basically the insertion occur in linked list)
           
           
           
## 2.3 Selection Sort  -> P32
