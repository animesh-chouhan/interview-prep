import bisect

a = list(range(0, 20, 2))
print(a)

print(bisect.bisect_left(a, 6))
print(bisect.bisect_right(a, 6))

bisect.insort_left(a, 6)
print(a)

print(bisect.bisect_left(a, 6))
print(bisect.bisect_right(a, 6))


bisect.insort_left(a, 5)
bisect.insort_right(a, 7)
print(a)
