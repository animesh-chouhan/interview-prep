from collections import defaultdict

# Usage
a = defaultdict(int)
print(a[0])
b = defaultdict(bool)
print(b[0])
c = defaultdict(list)
print(c[0])
d = defaultdict(set)
print(d[0])
e = defaultdict(dict)
print(e[0])

# Usage with lambda
f = defaultdict(lambda: [0, 0])
print(f[0])
# Set default to 5 instead of 0
g = defaultdict(lambda: 5)
print(g[0])

# calling missing
h = defaultdict(int)
# h[5] = 1
print(h.__missing__(5))
h[6]
print(h)

# Assigning other than defaultfactory
d1 = defaultdict(list, foo=1, bar=2)
d1["baz"]
d1["exe"] = True
print(d1)

# Assigning defaultfactory
d2 = defaultdict()
d2.default_factory = set
d2["abc"].add(1)
d2.default_factory = dict
d2["xyz"]["a"] = 1
print(d2)
d2.default_factory = None
d2["lmn"]
