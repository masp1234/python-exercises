import sys


def hello(x):
    if x[1] == "hello":
        print("Hello world" + x[1])
    else:
        print("no")

hello(sys.argv)


