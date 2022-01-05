#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_chines(message):
    for ch in message.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
