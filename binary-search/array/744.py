class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l = 0
        r = len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid

        # print(l, mid, r)
        if l < len(letters):
            return letters[l]
        else:
            return letters[0]


s = Solution()
s.nextGreatestLetter(letters=["c", "f", "j"], target="j")
