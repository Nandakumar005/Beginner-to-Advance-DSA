def two_pointers(arr, target):
    left =0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return arr[left],arr[right]
        if sum<target:
            left+=1
        else:
            right-=1
    return []

arr=[1,2,3,4,5,6,7,8,9]
target=8
result=two_pointers(arr,target)
print(result)