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
        # print token_type
        # print self.current_token.type
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        token = self.current_token
        self.get_token(INTEGER)
        return token.value

    def expr(self):
        '''
        整数值的计算
        :return: 返回计算结果
        '''

        self.current_token = self.get_next_token()
        result = self.term()
        while self.current_token.type in (PLUS, MINUS, MULTIPLY, DIVISION):
            token = self.current_token
            if token.type == PLUS:
                self.get_token(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.get_token(MINUS)
                result = result - self.term()

        return result

    # def set_operation(self, opt_str):
    #     if opt_str == PLUS:
    #         self.get_token(PLUS)
    #     elif opt_str == MINUS:
    #         self.get_token(MINUS)
    #     elif opt_str == MULTIPLY:
    #         self.get_token(MULTIPLY)
    #     elif opt_str == DIVISION:
    #         self.get_token(DIVISION)

    def calculator(self, num1, num2, opt):
        result = 0
        self.get_token(opt)
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
