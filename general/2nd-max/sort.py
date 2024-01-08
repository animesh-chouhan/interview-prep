def print2largest(line):
    nums = line.split(",")

    nums.sort(reverse=True)
    max_num = nums[0]
    max1_num = None

    for num in nums:
        if num < max_num:
            max1_num = num
            break

    if max1_num:
        print(max_num, max1_num)
    else:
        print("No 2nd max num")


while True:
    try:
        line = input()
        print2largest(line)
    except EOFError:
        break
