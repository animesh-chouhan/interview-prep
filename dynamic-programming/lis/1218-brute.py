# Brute+not visiting indexes which have been visited
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        count = [1] * len(arr)
        visited = []
        for i in range(len(arr)):
            if i in visited:
                continue
            current_element = arr[i]
            next_index = i
            while True:
                try:
                    target_element = current_element + difference
                    print(i, next_index, current_element, target_element)
                    next_index += arr[next_index + 1 :].index(target_element) + 1
                    visited.append(next_index)
                    count[i] += 1
                    current_element = arr[next_index]
                except ValueError:
                    break
        print(count)
        return max(count)


s = Solution()
print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 1], difference=-2))
print(s.longestSubsequence(arr=[1, -12, -12, 8, 8, 8], difference=0))
