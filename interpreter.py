#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解释器
INTEGER = 'INTEGER'
EOF = 'EOF'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVISION = 'DIVISION'
LPAREN = '('
RPAREN = ')'


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

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        '''
        异常提示
        :return:
        '''
        raise Exception('输入有误')

    def get_token(self, token_type):
        '''
        获得当前token的类型
        :param token_type:
        :return:
        '''
        # print token_type
        # print self.current_token.type
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.get_token(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.get_token(LPAREN)
            result = self.expr()
            self.get_token(RPAREN)
            return result

    def term(self):
        '''
        乘除运算
        :return:
        '''
        result = self.factor()
        while self.current_token.type in (MULTIPLY, DIVISION):
            token = self.current_token
            if token.type == MULTIPLY:
                self.get_token(MULTIPLY)
                result = result * self.factor()
            elif token.type == DIVISION:
                self.get_token(DIVISION)
                result = result / self.factor()

        return result

    def expr(self):
        '''
        加减运算
        :return: 返回计算结果
        '''
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.get_token(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.get_token(MINUS)
                result = result - self.term()

        return result
