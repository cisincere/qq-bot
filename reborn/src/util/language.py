#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from util.text import StrUtil


def is_chines(message):
    trust = 0
    for ch in message:
        if u'\u4e00' <= ch <= u'\u9fff':
            trust += 1
    return trust / len(message) > 0.7



def skip(message:str):
    if message.startswith('[CQ:') or StrUtil.is_mathe_expression(message):
        return True
    else:
        return False
