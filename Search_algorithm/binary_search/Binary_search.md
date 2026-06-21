# Binary Search

## Definition

Binary search is an efficient search algorithm that works on the principle of **divide and conquer**. It works by systematically eliminating half of the remaining elements at each step based on a comparison condition. This algorithm only works on **sorted arrays**.

## Real-World Analogy

Imagine reading a book with 100 pages and you want to find page 70. Instead of turning pages one by one (linear search), you:

1. Open to the middle (page 50)
2. Since 50 < 70, you skip the first half and focus on pages 51-100
3. Open the middle of remaining pages (page 75)
4. Since 75 > 70, you skip the second half and focus on pages 51-74
5. Continue this process until you find page 70

This is exactly how binary search works!

## Time Complexity

- **Best Case:** O(1) – When the target element is at the middle position
- **Average Case:** O(log n) – Logarithmic time complexity
- **Worst Case:** O(log n) – Still logarithmic, much better than linear search

## How It Works

The algorithm uses two pointers (`left` and `right`) and calculates the middle point. It then compares the target with the middle element and eliminates half of the search space in each iteration.

## Visual Step-by-Step Example

**Array:** `[1][2][3][4][5][6][7][8][9][10]`
**Target:** 8
**Length:** 10 elements, indices 0-9

---

### Step 1: Initialize pointers and find middle
- `left = 0` (start index)
- `right = 9` (last index)
- `mid = (0 + 9) // 2 = 4` (middle index)
- **Compare:** mid value is 5, target is 8 → 8 > 5, so search right half

```
left → [1][2][3][4][5][6][7][8][9][10] ← right
                 ↑
                mid (index 4, value 5)
```

---

### Step 2: Narrow search to right half
- `left = 5` (mid + 1)
- `right = 9` (unchanged)
- `mid = (5 + 9) // 2 = 7` (new middle)
- **Compare:** mid value is 8, target is 8 → Match found!

```
              [6][7][8][9][10]
               ↑     ↑      ↑
            left    mid      right
         (index 5) (index 7) (index 9)
```

---

### Step 3: Element found!
- `arr[mid] == target` → Return index 7

```
[1][2][3][4][5][6][7][8][9][10]
                      ↑
                FOUND at index 7!
```

## Code Example

**Input:**
```
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8
```

**Code:**

```python
def binary_search(arr, target):
    left = 0                    # Start from the beginning
    right = len(arr) - 1        # End at the last index
    
    while left <= right:
        mid = (left + right) // 2   # Calculate middle index
        
        if arr[mid] == target:
            return mid              # Element found
        elif target > arr[mid]:
            left = mid + 1          # Search in right half
        else:
            right = mid - 1         # Search in left half
    
    return -1                       # Element not found

# Test
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
print(f"Element found at index: {result}")
```

**Output:**

```
Element found at index: 7
```

## Why Index Adjustment?

- `right = len(arr) - 1` because array indexing starts from 0. If the array has 10 elements, the last valid index is 9 (not 10)
- Example: Array of 10 elements has indices 0-9, so `len(arr) - 1` = 10 - 1 = 9

## Advantages

- **Very efficient:** O(log n) time complexity is much faster than O(n) for large datasets
- **Predictable performance:** Guaranteed logarithmic time complexity
- **Minimal comparisons:** Eliminates half the remaining elements in each iteration
- **Works on large datasets:** Ideal for searching in large sorted collections

## Limitations

1. **Requires sorted array:** The array must be sorted beforehand, which adds preprocessing time
2. **Not suitable for unsorted data:** Must sort first, which could be O(n log n)
3. **Not ideal for linked lists:** Random access is needed for efficiency
4. **Duplicate handling:** Returns one match; doesn't identify all duplicates like linear search

## Comparison: Linear vs Binary Search

| Aspect | Linear Search | Binary Search |
|--------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Requires Sorted Array | No | Yes |
| Space Complexity | O(1) | O(1) |
| Best for | Small/Unsorted data | Large sorted data |
 
