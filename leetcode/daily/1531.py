from itertools import combinations


def encoded(s):
    if not s:
        return s
    ret = ""
    l = 0
    r = 0
    while r < len(s):
        if s[l] == s[r]:
            r += 1
        else:
            count = r - l
            if count > 1:
                ret += f"{s[l]}{count}"
            else:
                ret += s[l]
            l = r
            r += 1
    count = r - l
    if count > 1:
        ret += f"{s[l]}{count}"
    else:
        ret += s[l]

    return ret


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        s_len = len(s)
        indexes = combinations(range(s_len), k)
        lengths = []
        for index in indexes:
            mod_string = "".join([s[i] for i in range(s_len) if i not in index])
            encoded_string = encoded(mod_string)
            print(encoded_string)
            lengths.append(len(encoded_string))

        return min(lengths)


s = Solution()
print(s.getLengthOfOptimalCompression(s="aaabcccd", k=2))
print(s.getLengthOfOptimalCompression(s="aabbaa", k=2))
print(s.getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0))
print(s.getLengthOfOptimalCompression(s="a", k=1))

# print(encoded("aaabcccd"))
# print(encoded("aaaabbbcdeaa"))
