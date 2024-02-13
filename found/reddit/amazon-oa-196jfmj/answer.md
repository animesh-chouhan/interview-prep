Here's my version:

```python
def reverse_operations(s: str):
    i = 0
    j = len(s) - 1
    change = 0
    while i < len(s) and j >= 0:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            change += 1
            i += 1
    return change
```

Performance testing:

```python
from time import perf_counter

start = perf_counter()
for i in range(10000000):
    test = bin(i)[2:]
    reverse_operations(test)

print(f"Time taken: {perf_counter()-start}s")
```

It can be generalized to changing two strings with equal number of 1's and 0's. Here `t` is the target string and `s` is the string to be changed.

```python
def change_operations(s: str, t: str):
    i = 0
    j = 0
    change = 0
    while i < len(s) and j < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            change += 1
            i += 1
    return change
```
