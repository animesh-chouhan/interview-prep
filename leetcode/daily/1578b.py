def get_cost(start_index, end_index, neededTime):
    time_array = neededTime[start_index : end_index + 1]
    return sum(time_array) - max(time_array)


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        colors = colors
        cost = 0
        start_index = 0
        end_index = 0
        for i in range(len(colors) - 1):
            if colors[i] == colors[i + 1]:
                end_index += 1
            else:
                if end_index - start_index > 0:
                    cost += get_cost(start_index, end_index, neededTime)
                start_index = end_index + 1
                end_index = start_index

        if end_index - start_index > 0:
            cost += get_cost(start_index, end_index, neededTime)

        return cost


s = Solution()
print(s.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(s.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
print(s.minCost(colors="abc", neededTime=[1, 2, 3]))
string = "aabbbccccdddddde"
print(s.minCost(colors=string, neededTime=list(range(len(string)))))
