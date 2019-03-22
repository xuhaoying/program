
def test1():
    L = []
    for i in range(1000):
        # L = L + [i]
        L += [i]

def test2():
    L = []
    for i in range(1000):
        L.append(i)
    
def test3():
    L = [i for i in range(1000)]

def test4():
    L = list(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "seconds")

# concat  0.095499849 seconds
# append  0.07841864200000001 seconds
# comprehension  0.036522940000000004 seconds
# list range  0.017208590999999968 seconds


x = list(range(2000000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero", pop_zero.timeit(number=1000), "seconds")
x = list(range(2000000))
pop_end = Timer('x.pop()', "from __main__ import x")
print("pop_end", pop_end.timeit(number=1000), 'seconds')

# pop_zero 1.844889342 seconds
# pop_end 9.206699999975143e-05 seconds

def x_append():
    x = list(range(2000000))
    for i in range(1000):
        x.append(i)

def x_insert():
    x = list(range(2000000))
    for i in range(1000):
        x.insert(0, i)

time_append = Timer("x_append()", "from __main__ import x_append")
print("x_append", time_append.timeit(number=1000), 'seconds')
time_insert = Timer("x_insert()", "from __main__ import x_insert")
print("x_insert", time_insert.timeit(number=1000), "seconds")

# x_append 61.527599429999995 seconds
# x_insert 1983.778811841 seconds



