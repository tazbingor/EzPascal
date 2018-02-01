#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 语法分析器
from interpreter import Token

INTEGER = 'INTEGER'
EOF = 'EOF'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVISION = 'DIVISION'


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('输入有误:输入了无效的字符')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None \
                and self.current_char.isspace():
            self.advance()

    def integer(self):
        '''
        获取整数
        :return: 返回一位甚至多位的整型
        '''
        result = ''
        while self.current_char is not None \
                and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        '''
        分词器
        :return:token格式化对象
        '''
        while self.current_char is not None:

            # 检测空格
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # 检测整数
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            # OPT
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVISION, '/')

            self.error()

        return Token(EOF, None)
