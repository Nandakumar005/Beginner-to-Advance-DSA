def binary_search(arr,target):
    left=0 # Initialize left pointer
    right=len(arr)-1 # Initialize right pointer
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:# If the target is greater than the middle element, search in the right half
            left=mid+1
        else:# If the target is less than the middle element, search in the left half
            right=mid-1
    return -1#if the target is not found, return -1

#Example
arr=[1,2,3,4,5,6,7,8,9,10]
target=7
result=binary_search(arr,target)
print(f"Target {target} found at index: {result}" if result != -1 else f"Target {target} not found in the array.")