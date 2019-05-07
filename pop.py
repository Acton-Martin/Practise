import timeit

def t6():
    list_1 = list(range(100))
    for i in range(100):
        list_1.pop()  # pop最后一个元素

def t7():
    list_2 = list(range(100))
    for i in range(100):
        list_2.pop(0)  # pop第一个元素

time6 = timeit.Timer("t6()", "from __main__ import t6")
time7 = timeit.Timer("t7()", "from __main__ import t7")
print("pop():%f" %  time6.timeit())
print("pop(0):%f" % time7.timeit())
