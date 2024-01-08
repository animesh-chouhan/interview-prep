# Condition: The next number is greater and index is also greater
def generate_dag(nums):
    dag = [[] for _ in nums]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dag[i].append(j)
    return dag


nums = [10, 9, 2, 5, 3, 7, 101, 18]
for i in zip(list(range(len(nums))), generate_dag(nums)):
    print(i)
