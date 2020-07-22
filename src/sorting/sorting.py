# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # To-do
    # Loop through the merged array
    # If the arrays are bigger than zero, find out which element is bigger
    # pop(?) that smaller element into the merged_arr
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            #if arrA at the 0th position is bigger than arrB at the 0th position, pop out the element in arrB's 0th position
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB.pop(0)
            else:
                #pop the element in arrA's 0th position
                merged_arr[i] = arrA.pop(0)
        else:
            # if arrA is empty, add rest of arrB to merged array
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        #split left until 1 item
        left = merge_sort(arr[:len(arr) // 2])
        #split right until 1 item
        right = merge_sort(arr[len(arr) // 2:])
        #merge all
        arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
