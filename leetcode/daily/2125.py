class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        counts = []
        for i in range(len(bank)):
            latest_count = bank[i].count("1")
            if latest_count > 0:
                counts.append(latest_count)

        # print(counts)
        total = 0
        for i in range(len(counts) - 1):
            total += counts[i] * counts[i + 1]

        return total


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total = 0
        prev_count = 0
        for i in range(len(bank)):
            latest_count = bank[i].count("1")
            if latest_count > 0:
                if prev_count > 0:
                    total += prev_count * latest_count
                prev_count = latest_count

        return total


s = Solution()
print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(s.numberOfBeams(bank=["000", "111", "000"]))
