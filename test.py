#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试
from interpreter import Interpreter
from lexer import Lexer


def main():
    while True:
        try:
            try:
                text = raw_input('ezpas> ')
            except NameError:
                text = input('ezpas> ')
        except EOFError:
            break

        if not text:
            continue
        lexer = Lexer(text)
        interpr = Interpreter(lexer)
        result = interpr.expr()
        print result


if __name__ == '__main__':
    main()
