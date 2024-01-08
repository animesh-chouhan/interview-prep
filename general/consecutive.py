def group(nums):
    chunks = []
    temp = []
    for i in range(len(nums)):
        temp.append(nums[i])
        if i < len(nums) - 1 and nums[i + 1] - nums[i] <= 1:
            continue
        else:
            chunks.append(temp)
            temp = []
    print(chunks)
    return chunks


group([1, 1, 2, 2, 3, 5, 5, 7])
group([2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 20])
group([1])
group([])
