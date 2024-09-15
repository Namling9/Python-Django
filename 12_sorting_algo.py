# bubble sort: Best case of bubble sort is O(n) and worst case is 

# Sort given list = [1,5,9,6,28,1203,4,23]
'''list = [23084,1,5,9,6,28,1203,4,23]
temp = 0

def bubblesort(l):
    n = len(l) 
    for i in range(n): # i loop runs for 0 to n-1 times (0-1-2-3 to n-1  )
    # Track whether any swaps are made in this pass
        swapped = False
        for j in range(n-i-1): # j loop run for 0 to n-i-1 times ( for example if n is 5, it runs 4 - i -1 means 4-0-1. it will run (0-3) for 1st loop of i.)
            
            if( l[j] > l[j+1]): 
                #swap l[j] with l[j+1]
                # temp = l[j] # initializing value of l[j] to temp.
                # l[j] = l[j+1] # initializing value of l[j+1] to l[j].
                # l[j+1] = temp # and initializing value of temp(l[j]) to l[j+1]
                l[j], l[j+1] = l[j+1], l[j]
                print(l)
                swapped = True
                
                
        # If no two elements were swapped by inner loop, then break  
        if not swapped:
            break
    return l

bubblesort(list)
print("Sorted list: ",list) '''

# Merge sort
# Merge sort: Best case of merge sort is O(n log n) and The worst-case time complexity of Merge Sort is O(nlogn), 
# which is the same as its best and average case 

'''Merge sort is a classic and efficient sorting algorithm based on the divide-and-conquer paradigm.
It works by recursively splitting an array into smaller subarrays, sorting each subarray, 
and then merging them back together into a single sorted array.'''


'''

def merge_sort(l):
    
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    
    l_left = l[:mid]
    l_right = l[mid:]
    
    l_left = merge_sort(l_left)
    l_right = merge_sort(l_right)
    
    return merge(l_left, l_right)

def merge(l_left, l_right):
    
    result = []
    i,j = 0,0
    
    while i < len(l_left) and j < len(l_right):
        
        if l_left[i] < l_right[j]:
            
            result.append(l_left[i])
            i+=1
        else: 
            result.append(l_right[j])
            j+=1
    
    result.extend(l_left[i:])
    result.extend(l_right[j:])
    return result

l = [98,12,32,42,12,10,9,2,31,1,31,1,3,4,55,6,4,7,7,8,9]

print(merge_sort(l)) '''


# bubble sort
'''
def bubble_sort(l):
    
    n = len(l)
    for i in range(n):
        swapped = False
        
        for j in range(n-i-1):
            
            if l[j] > l[j+1]:
                
                l[j],l[j+1] = l[j+1], l[j] # swap
                swapped = True
                
        if not swapped:
            break
    
    return l

l = [98,12,32,42,12,10,9,2,31,1,31,1,3,4,55,6,4,7,7,8,9]
print(bubble_sort(l)) #[1, 1, 2, 3, 4, 4, 6, 7, 7, 8, 9, 9, 10, 12, 12, 31, 31, 32, 42, 55, 98] '''

# Merge_sort
'''
def merge_sort(l):
    
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    l_left = l[:mid]
    l_right = l[mid:]
    
    l_left = merge_sort(l_left)
    l_right = merge_sort(l_right)
    
    return merge(l_left,l_right)

def merge(l_left, l_right):
    
    result = []
    i,j = 0,0
    
    while i < len(l_left) and j < len(l_right):
        
        if l_left[i] < l_right[j]:
            
            result.append(l_left[i])
            i+=1
            
        else: 
            result.append(l_right[j])
            j+=1
            
    result.extend(l_left[i:])
    result.extend(l_right[j:])
    
    return result

l = [98,12,32,42,12,10,9,2,31,1,31,1,3,4,55,6,4,7,7,8,9]
print(merge_sort(l)) #[1, 1, 2, 3, 4, 4, 6, 7, 7, 8, 9, 9, 10, 12, 12, 31, 31, 32, 42, 55, 98] 
'''
        

# Quick Sort

# def quick_sort(arr,low,high):
#     if low < high:
#         pivot = partition(arr,low,high) # # Partitioning index
#         quick_sort(arr,low,pivot-1) # Sort the elements before the partition
#         quick_sort(arr,pivot+1, high) # Sort the elements after the partition
#     return arr

# def partition(arr,low,high):

#     p = arr[low]  # Choose the first element as the pivot
#     i = low+1
#     j = high
    
#     while True: 
        
#         while i <= j and arr[i] <= p :
#             i+=1
#         while i <= j and arr[j] >=p:
#             j-=1
        
#         if i <= j: 
            
#             arr[i], arr[j] = arr[j], arr[i] # Swap elements
        
#         else: 
#             break
    
#     arr[low], arr[j] = arr[j], arr[low] # Place pivot in the correct position
#     return j  # Return the pivot index

# l = [98,12,32,42,12,10,9,2,31,1,31,1,3,4,55,6,4,7,7,8,9]
# print(quick_sort(l,0, len(l)-1))

'''        
def quick_sort(arr,low,high):
    
    if low< high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
        
    return arr

def partition(arr,low,high):
    
    p = arr[low]
    i = low+1
    j = high
    
    while True:
        
        while i <= j and arr[i] <= p:
            i+=1
        
        while i<=j and arr[j] >= p:
            j-=1
        
        if i <= j :
            
             arr[i], arr[j] = arr[j], arr[i] 
      
        else: 
            break
    
    arr[low], arr[j]=arr[j],arr[low]
    return j
        
l = [98,12,32,42,12,10,9,2,31,1,2,3,4,5]

print(quick_sort(l, 0, len(l)-1))

'''

        
# Quick Sort

def quick_sort(l,low,high):
    
    if low < high: 
        
        pivot = partition(l,low,high)
        quick_sort(l,low,pivot-1)
        quick_sort(l,pivot+1,high)
    
    return l

def partition(l,low,high):
    
    p = l[low]
    i = low+1
    j = high
    
    while True:
        
        while i <= j and l[i] <= p:
            
            i+=1
        
        while i <= j and l[j] >= p:
            j-=1
        
        if i <= j:
           
            l[i], l[j] = l[j], l[i]
        
        else : break
        
    
    l[low], l[j] = l[j], l[low]
  
    return j
    
    
l = [98,12,32,42,12,10,9,2,31,1,2,3,4,5]
quick_sort(l, 0, len(l)-1)
print(l)   
             
            
