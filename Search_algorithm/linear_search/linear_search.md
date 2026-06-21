# Linear Search

## Definition

Linear search is a simple algorithm that works by checking every element in an array one by one until the target element is found. It iterates sequentially through the array from the beginning to the end.

## Time Complexity

- **Best Case:** O(1) – When the target element is at the first position
- **Average Case:** O(n) – When the target is somewhere in the middle
- **Worst Case:** O(n) – When the target is at the end or not present

## How It Works

The algorithm compares each element with the target value and returns the index when a match is found.

## Example

**Input:**
```
arr = [2, 3, 4, 1, 5, 3, 2, 5]
target = 5
```

**Code:**

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test
result = linear_search([2, 3, 4, 1, 5, 3, 2, 5], 5)
print(f"Element found at index: {result}")
```

**Output:**

```
Element found at index: 4
```

## Advantages

- Simple and easy to implement
- Works with unsorted arrays
- No additional space required

## Limitations

1. **Inefficient for large datasets:** If the input size is very large, the runtime takes considerable time and memory
2. **Returns first occurrence:** It doesn't identify all duplicate elements; it returns only the first match
3. **Slower than other algorithms:** Much slower than binary search or hash-based searches for large arrays
