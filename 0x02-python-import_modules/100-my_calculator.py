#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    i = 0
    if (len(argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(len(argv[:1]))
    elif (argv[2] == '+'):
        arg1 = argv[i + 1]
        a = int(arg1)
        arg2 = argv[i + 3]
        b = int(arg2)
        print(a, "+", b, "=", add(a, b))
    elif (argv[2] == '-'):
        arg1 = argv[i + 1]
        a = int(arg1)
        arg2 = argv[i + 3]
        b = int(arg2)
        print(a, "-", b, "=", sub(a, b))
    elif (argv[2] == "*"):
        arg1 = argv[i + 1]
        a = int(arg1)
        arg2 = argv[i + 3]
        b = int(arg2)
        print(a, "*", b, "=", mul(a, b))
    elif (argv[2] == '/'):
        arg1 = argv[i + 1]
        a = int(arg1)
        arg2 = argv[i + 3]
        b = int(arg2)
        print(a, "/", b, "=", div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(len(argv[:1]))


if __name__ == "__main__":
    main()
