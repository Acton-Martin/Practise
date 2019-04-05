import math
"""计算将洒江辣酱辣酱啦"""


def quadratic(a, b, c):
    """计算将洒江辣酱辣酱啦"""
    if a == 0:
        x = -c / b
        print("OMG! The answer is %f" % (x))
    elif a == 0 and b == 0 and c != 0:
        print("Oooooops.It's wrong!")
    elif a == 0 and b == 0 and c == 0:
        print("It is all ok")
    else:
        dalt = b * b - 4 * a * c
        if dalt > 0:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            print("Two answers are %f %f" % (x1, x2))
        else:
            print("something is wrong!")
        # return x1, x2

a=float(input("get a:"));
b=float(input("get b:"));
c=float(input("get c:"));


print(quadratic(a, b, c))
