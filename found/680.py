def check(s):
    return s == s[::-1]


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if check(s):
            return True
        for i in range(len(s)):
            if check(s[:i] + s[i + 1 :]):
                return True
        return False


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        cnt = 0
        i = 0
        j = len(s) - 1
        while i <= j:
            print(i, s[i], j, s[j])
            if s[i] != s[j]:
                if check(s[:i] + s[i + 1 :]) or check(s[:j] + s[j + 1 :]):
                    return True
                else:
                    return False

            i += 1
            j -= 1

        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         pass


s = Solution()
print(s.validPalindrome("abbbca"))
print(s.validPalindrome("lcupuuduupucul"))
