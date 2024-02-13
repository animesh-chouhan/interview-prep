class Solution:
    def encode(self, strs):
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, str):
        ret = []
        i = 0
        while True:
            sep = str.find("#", i)
            if sep != -1:
                length = int(str[i:sep])
                message = str[sep + 1 : sep + 1 + length]
                ret.append(message)
                i = sep + 1 + length
            else:
                break

        return ret

    def decode(self, str):
        ret = []
        last = 0
        i = 0
        while i < len(str):
            if str[i] == "#":
                length = int(str[last:i])
                message = str[i + 1 : i + 1 + length]
                ret.append(message)
                last = i + 1 + length
                i = last
            else:
                i += 1

        return ret


s = Solution()
strs = ["abcd", "#yreese", "34dsgg#"]
encoded = s.encode(strs)
print(encoded)
decoded = s.decode(encoded)
print(decoded)
assert strs == decoded
