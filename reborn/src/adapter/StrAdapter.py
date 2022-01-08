#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from adapter.MessageAdapter import MessageAdapter


class StrAdapter(MessageAdapter):
    pass


class CommandAdapter(StrAdapter):
    """
    命令适配器
    """
    pass


class KeyWordAdapter(StrAdapter):
    """
    关键字适配器
    """
    pass


class NLPAdapter(StrAdapter):
    """
    NLP适配器
    """
    pass
