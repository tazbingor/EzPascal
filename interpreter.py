#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解释器
INTEGER = 'INTEGER'
EOF = 'EOF'
PLUS = 'PLUS'


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
    def __init__(self, text):
        '''
        初始化
        :param text: 需要解析的文本
        '''
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        '''
        输入异常
        :return:
        '''
        raise Exception('输入有误')

    def get_next_token(self):
        '''
        分词器
        :return:token格式化对象
        '''
        tmp_text = self.text

        if self.pos > len(tmp_text) - 1:
            return Token(EOF, None)

        current_char = tmp_text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()
