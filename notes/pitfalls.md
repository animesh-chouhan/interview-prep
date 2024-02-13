# Common pitfalls

## Caching

<https://leetcode.com/problems/house-robber/>

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache ={}
        def visit(i):
            if i>=len(nums):
                return 0
            cache[i] = cache.get(i) or nums[i]+ max(visit(i+2), visit(i+3))
            print(cache[i])
            return cache[i]

        return max(visit(0), visit(1))
```

VS

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache ={}
        def visit(i):
            if i>=len(nums):
                return 0
            cache[i] = nums[i]+ max(visit(i+2), visit(i+3)) if cache.get(i) is None else cache[i]
            return cache[i]
        return max(visit(0), visit(1))
```

VS

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache ={}
        def visit(i):
            if i>=len(nums):
                return 0
            if i not in cache:
                cache[i] = nums[i]+ max(visit(i+2), visit(i+3))
            return cache[i]
        return max(visit(0), visit(1))
```

VS

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache ={}
        def visit(i):
            if i>=len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = nums[i]+ max(visit(i+2), visit(i+3))
            return cache[i]
        return max(visit(0), visit(1))
```

VS

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache ={}
        def visit(i):
            if i>=len(nums):
                return 0
            cache[i]=cache.get(i, nums[i]+ max(visit(i+2), visit(i+3)))
            return cache[i]
        return max(visit(0), visit(1))
```
