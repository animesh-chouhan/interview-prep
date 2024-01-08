class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        used1 = 0
        used2 = 0
        i = 0
        while True:
            i += 1
            if memory1 >= i and memory1 >= memory2:
                used1 += i
                memory1 -= i
            elif memory2 >= i:
                used2 += i
                memory2 -= i
            else:
                break

        return [i, memory1, memory2]
