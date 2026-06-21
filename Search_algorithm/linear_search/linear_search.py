def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

# Example usage
arr=[2,3,4,5,3]
target=4
result=linear_search(arr,target)
print(result)