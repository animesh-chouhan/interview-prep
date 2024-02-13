# https://docs.python.org/3/library/timeit.html
import timeit


def test():
    """Stupid test function"""
    L = [i for i in range(100)]


if __name__ == "__main__":
    print(timeit.timeit("test()", setup="from __main__ import test"))


# Set intersection vs &
s1 = set([i for i in range(10000)])
s2 = set([i for i in range(5000, 5000 + 10000)])

# python -m timeit -h
# python -m timeit -v -n 10000 -r 10 -s "s1=set([i for i in range(10000)]);s2=set([i for i in range(5000,5000+10000)])" "s1&s2"
# python -m timeit -v -n 10000 -r 10 -s "s1=set([i for i in range(10000)]);s2=set([i for i in range(5000,5000+10000)])" "s1.intersection(s2)"
