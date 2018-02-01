#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解释器
INTEGER = 'INTEGER'
EOF = 'EOF'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVISION = 'DIVISION'


class Token(object):
    '''字符串标记'''

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return self._token_format('Token({type},{value})')

    def _token_format(self, string):
        '''
        token字符串格式化
        :param string:token
        :return:format token
        '''
        return string.format(
            type=self.type,
            value=repr(self.value)
        )

    __repr__ = __str__


class Interpreter(object):
    '''解释器'''

    def __init__(self, text):
        '''
        初始化
        :param text: 需要解析的文本
        '''
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        '''
        异常提示
        :return:
        '''
        raise Exception('输入有误')

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

    def get_token(self, token_type):
        '''
        获得当前token的类型
        :param token_type:
        :return:
        '''
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''
        整数值的计算
        :return: 返回计算结果
        '''
        self.current_token = self.get_next_token()

        # 左边的数
        left = self.current_token
        self.get_token(INTEGER)

        # 运算符操作
        opt = self.current_token
        if opt.type == PLUS:
            self.get_token(PLUS)
        else:
            self.get_token(MINUS)

        # 右边的数
        right = self.current_token
        self.get_token(INTEGER)

        # 计算器
        return self.calculator(left.value, right.value, opt)

    def calculator(self, num1, num2, opt):
        result = 0
        if opt.type == PLUS:
            result = num1 + num2
        elif opt.type == MINUS:
            result = num1 - num2
        elif opt.type == MULTIPLY:
            result = num1 * num2
        elif opt.type == DIVISION:
            result = num1 / num2

        return result

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
        :return: 返回一位甚至多位的整型
        '''
        result = ''
        while self.current_char is not None \
                and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
