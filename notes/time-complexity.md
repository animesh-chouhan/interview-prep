# Time complexity

## Processors

Most modern processors have a base clock of around 3GHz which is 3e9 clock cycles per second. Here is a simple code that loops 1e8 times performing a basic operation.

Code:

```python
import time

start = time.perf_counter()

a = 0
for i in range(pow(10, 8)):
    a += 1

print(f"Time taken: {time.perf_counter()-start}s")
```

Output:

```sh
Time taken: 4.131068754999433s
```

## Guessing the complexity of a problem

By looking at the constraints of a problem, we can often "guess" the solution.

Let n be the main variable in the problem:

- If n ≤ 12, the time complexity can be O(n!).
- If n ≤ 25, the time complexity can be O(2^n).
- If n ≤ 100, the time complexity can be O(n^4).
- If n ≤ 500, the time complexity can be O(n^3).
- If n ≤ 10^4, the time complexity can be O(n^2).
- If n ≤ 10^6, the time complexity can be O(nlog n).
- If n ≤ 10^8, the time complexity can be O(n).
- If n > 10^8, the time complexity can be O(log n) or O(1).

Another good way to remember this is that whatever algorithm you chose, if you plug in `n`, you should get around `~10^8`.

Source: https://codeforces.com/blog/entry/21344