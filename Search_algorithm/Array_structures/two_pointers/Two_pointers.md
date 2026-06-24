# Two Pointers

## Definition

Two Pointers is a technique that uses two pointers (indices or references) that move through a data structure—usually an array or string—to efficiently solve problems. The pointers can move in the same direction or opposite directions depending on the problem. This technique is particularly useful for problems involving **searching, sorting, or rearranging** elements.

## Real-World Analogy

Imagine you have a glass of juice with two straws:

1. You put one straw on the **left side** and one on the **right side**
2. You drink from both sides simultaneously, moving toward the middle
3. When the juice meets in the middle (or you've consumed it all), you're done

For example, finding if a word is a **palindrome** (reads the same forwards and backwards):
- Put one pointer at the **start** and one at the **end**
- Compare the characters
- Move both pointers toward the middle
- If all characters match, it's a palindrome

## Time Complexity

- **Best Case:** O(1) – When solution is found immediately
- **Average Case:** O(n) – Single or double pass through the array
- **Worst Case:** O(n) – Still linear time, much better than nested loops O(n²)

## How It Works

The two pointers technique typically works in one of two ways:

1. **Opposite Direction Pointers:** One pointer starts at the beginning, the other at the end. They move toward each other, comparing or processing elements.
2. **Same Direction Pointers:** Both pointers start at the beginning and move forward at different speeds or under different conditions.

## Visual Step-by-Step Example

Let's solve: **Find two numbers that sum to a target in a sorted array**

**Array:** `[1][2][3][4][5][6][7][8]`
**Target:** 9
**Goal:** Find two numbers that add up to 9

---

### Step 1: Initialize pointers
- `left = 0` (points to first element: 1)
- `right = 7` (points to last element: 8)
- **Sum:** 1 + 8 = 9 → Match found!

```
[1][2][3][4][5][6][7][8]
 ↑                       ↑
left(1)              right(8)
       Sum = 1 + 8 = 9 ✓
```

---

### Step 2: Return the result
- Found pair: **(1, 8)** at indices (0, 7)

```
[1][2][3][4][5][6][7][8]
 ↑                       ↑
FOUND: 1 + 8 = 9
```

---

## Code Example

### Problem 1: Two Sum in Sorted Array

**Input:**
```
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 9
```

**Code:**

```python
def two_sum(arr, target):
    left = 0                    # Start from beginning
    right = len(arr) - 1        # Start from end
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [arr[left], arr[right]]  # Found the pair
        elif current_sum < target:
            left += 1                       # Need larger sum, move left pointer right
        else:
            right -= 1                      # Need smaller sum, move right pointer left
    
    return []                               # No pair found

# Test
result = two_sum([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(f"Pair found: {result}")
```

**Output:**

```
Pair found: [1, 8]
```

---

### Problem 2: Validate Palindrome

**Input:**
```
s = "racecar"
```

**Code:**

```python
def is_palindrome(s):
    left = 0                    # Start from beginning
    right = len(s) - 1          # Start from end
    
    while left < right:
        if s[left] != s[right]:
            return False                    # Characters don't match
        left += 1                           # Move left pointer forward
        right -= 1                          # Move right pointer backward
    
    return True                             # All characters matched

# Test
result = is_palindrome("racecar")
print(f"Is palindrome: {result}")
```

**Output:**

```
Is palindrome: True
```

---

## Advantages

1. **Efficient:** Reduces time complexity from O(n²) to O(n) for many problems
2. **Space Efficient:** Uses constant O(1) extra space (just two pointers)
3. **Works on Sorted Data:** Great for sorted arrays where order matters
4. **Intuitive:** Simple logic that's easy to understand and implement
5. **Versatile:** Can solve multiple problem types (two sum, palindromes, reversing, etc.)

## Limitations

1. **Requires Sorted Array:** For most problems, the input array needs to be sorted
2. **Only Two Pointers:** Cannot handle problems that require comparing more than two elements at once
3. **Not for Unordered Search:** For unordered arrays with random element search, hash maps might be better
4. **Order Dependent:** The algorithm relies on specific ordering of elements

## Common Use Cases

- ✓ Finding pairs with a specific sum
- ✓ Validating palindromes
- ✓ Reversing arrays or strings
- ✓ Removing duplicates from sorted arrays
- ✓ Merging sorted arrays
- ✓ Container with most water problems
