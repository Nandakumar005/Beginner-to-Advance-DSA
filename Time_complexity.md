# Time Complexity

## O(1) – Constant Time

No matter the input size, the execution time remains the same.

**Example:**

```python
arr = [1, 2, 4, 5, 6, 3, 2]
print(arr[2])
```

## O(n) – Linear Time

The execution time increases along with the size of the input. If the input doubles, the execution time doubles.

**Example:**

```python
arr = [2, 3, 4, 5, 3, 5]
for i in arr:
    print(i)
```

## O(n²) – Quadratic Time

The execution time grows quadratically with the input size. For example, if linear time takes 10 seconds, quadratic time may take 100 seconds or more, depending on the number of nested loops.

**Example:**

```python
arr = [1, 3, 5, 3, 2, 5]
for i in arr:
    for j in arr:
        print(i, j)
```
   
