#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import markovify


def text_fix():
    f = open('./in.txt', encoding='utf-8')
    o = open('./auf.txt', 'w', encoding='utf-8')
    for i in range(747):
        line = f.readline()
        if line != '\n' and line != '***\n':
            o.write(line)


def aue():
    with open('./auf.txt', encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.Text(text, state_size=2)
    return text_model.make_short_sentence(380)


if __name__ == '__main__':
    aue()
