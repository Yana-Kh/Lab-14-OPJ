#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2


if __name__ == '__main__':
    test_fun = fun1(4)
    print("ex1")
    print(test_fun(7))

    print("\nex2")
    tpl = lambda d, e: (d, e)
    s = tpl(1, 2)
    print(s)
    f = tpl(3, s)
    print(f)
    c = tpl(s, f)
    print(c)
