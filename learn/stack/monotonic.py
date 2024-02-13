# 739. Daily Temperatures: https://www.youtube.com/watch?v=cTBiBSnjO3c
# https://www.youtube.com/watch?v=Dq_ObZwTY_Q
# https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems


# Get days after which the next greater temperature occurs
def get_days(temp):
    ret = [0] * len(temp)
    stack = []
    for i in range(len(temp)):
        while stack and stack[-1][1] < temp[i]:
            pos, val = stack.pop()
            ret[pos] = i - pos
        stack.append((i, temp[i]))
    return ret


def get_days(temp):
    ret = [0] * len(temp)
    stack = []
    for i in range(len(temp) - 1, -1, -1):
        while stack:
            if stack[-1][1] <= temp[i]:
                stack.pop()
            else:
                pos, val = stack[-1]
                ret[i] = pos - i
                break
        stack.append((i, temp[i]))
    return ret


# Get next temp which is greater than the current element
def get_temp(temp):
    ret = [-1] * len(temp)
    stack = []
    for i in range(len(temp)):
        while stack and stack[-1][1] < temp[i]:
            pos, val = stack.pop()
            ret[pos] = temp[i]
        stack.append((i, temp[i]))
    return ret


def get_temp(temp):
    ret = [-1] * len(temp)
    stack = []
    for i in range(len(temp) - 1, -1, -1):
        while stack:
            if stack[-1] <= temp[i]:
                stack.pop()
            else:
                ret[i] = stack[-1]
                break
        stack.append(temp[i])
    return ret


temp = [71, 72, 73]
print(get_temp(temp))
print(get_days(temp))
assert get_temp(temp) == [72, 73, -1]
assert get_days(temp) == [1, 1, 0]

temp = [73, 72, 71]
print(get_temp(temp))
print(get_days(temp))
assert get_temp(temp) == [-1, -1, -1]
assert get_days(temp) == [0, 0, 0]

temp = [72, 71, 73]
print(get_temp(temp))
print(get_days(temp))
assert get_temp(temp) == [73, 73, -1]
assert get_days(temp) == [2, 1, 0]

temp = [73, 74, 75, 71, 69, 72, 76, 73]
print(get_temp(temp))
print(get_days(temp))
assert get_temp(temp) == [74, 75, 76, 72, 72, 76, -1, -1]
assert get_days(temp) == [1, 1, 4, 2, 1, 1, 0, 0]
