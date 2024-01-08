def print2largest(line):
    nums = line.split(",")
    max_num = nums[0]
    max1_num = None

    for num in nums:
        if num > max_num:
            max1_num = max_num
            max_num = num
        elif num < max_num:
            if max1_num == None or num > max1_num:
                max1_num = num

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
