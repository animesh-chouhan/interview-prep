class Solution:
    def minOperations(self, s: str) -> int:
        seq1 = [str(i % 2) for i in range(len(s) + 1)]
        count1 = 0
        count2 = 0
        for i, d in enumerate(s):
            if seq1[i] != d:
                count1 += 1
            if seq1[i + 1] != d:
                count2 += 1

        return min(count1, count2)
