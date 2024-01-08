from collections import Counter


class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        differences = []
        counter = Counter(str_num)
        for digit1 in counter.keys():
            a = str_num.replace(digit1, "9")
            # print(a)
            for digit2 in counter.keys():
                b = str_num.replace(digit2, "0")
                if b[0] == "0":
                    c = str_num.replace(digit2, "1")
                    differences.append(int(a) - int(c))
                else:
                    differences.append(int(a) - int(b))

        print(differences)
        print(max(differences))
        return max(differences)
