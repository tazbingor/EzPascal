#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试
from interpreter import Interpreter


def main():
    while True:
        try:
            try:
                text = raw_input('ezpas>> ')
            except NameError:
                text = input('ezpas>> ')
        except EOFError:
            break

        if not text:
            continue

        interpr = Interpreter(text)
        result = interpr.expr()
        print result


if __name__ == '__main__':
    main()
