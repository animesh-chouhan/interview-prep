from collections import defaultdict


# using string.find
def is_subseq(s, t):
    for c in s:
        index = t.find(c)
        if index == -1:
            return False
        t = t[index + 1 :]
    return True


# 2 pointer for loop
def is_subseq(s, t):
    len_s = len(s)
    j = 0
    for c in t:
        if j > len_s - 1:
            return True
        if s[j] == c:
            j += 1

    return j == len_s


# 2 pointer while loop
def is_subseq(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


# d = defaultdict(list)


# def is_subseq(s, t):
#     for i, c in enumerate(t):
#         d[c].append(i)

#     print(d)


print(is_subseq("india", "indonesia"))
print(is_subseq("oman", "romania"))
print(is_subseq("mali", "malawi"))
print(is_subseq("mali", "banana"))
print(is_subseq("ais", "indonesia"))
print(is_subseq("ca", "abc"))
