# Iteratie Binary search
def iterative_binary_search(sorted_arr, target):
    # Define the leftmost and rightmost element of the array
    left = 0
    right = len(sorted_arr) - 1

    # Iterate throgh the values based on the position of the midpoint
    while left <= right:
        # Set the midpoint
        mid = (right + left) // 2

        if sorted_arr[mid] == target:
            return mid
            
        # Set the new left index after first iteration   
        elif sorted_arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return - 1


# Divide and couquer with merge sort
def merge_sort(arr): 
    """
    The array is divided into two parts: 'left' and 'right' part
    Each of the two parts is recursively divided to the smallest unit
    The units are then joined in aceding order
    """

    if len(arr) > 1:
        # Midpoint of the data
        mid = len(arr) // 2
    
        # Divide left and right part
        left = arr[:mid]
        right = arr[mid:]
    
        # recusively divide the two parts
        merge_sort(left)
        merge_sort(right)
        # i = left index; j= right index, k = sorted array
        i = j = k = 0
    
        # Merge the arrays when they got elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
    
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # check for remaining element in the left array if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k+=1
        # Add remaining eement from the rigt if any    
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k+=1

    return arr

             
def main():
    # Unsorted list
    arr = [54, 78, 64, 32, 90, 100, 123, 169]
    targets = [54, 123, 189]

    # Merge sort
    sorted_arr = merge_sort(arr)
    print(f"Sorted Array: {sorted_arr}")

    
    for target in targets:
        result = iterative_binary_search(arr, target)

        if result != -1:
            print(f"Target {target} found at index {result}")
        else:
            print(f"Target {target} not found in the array")

if __name__ == "__main__":
    main()
    