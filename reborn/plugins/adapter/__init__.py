#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from random import randint

from nonebot import CommandSession, on_command
from nonebot import on_natural_language
from nonebot import NLPSession, IntentCommand
from reborn.src.util import file, list
from reborn.src.util.text import StrUtil
from src.util.language import is_chines, skip

greet_tuple = ('早安', '早上好', '早', '早啊', '晚安', '晚上好', '午安')


@on_command('ni_image', aliases=('动漫图', '二次元图片', '二刺螈图', '来张图', "色图", "涩图"), only_to_me=False)
async def ni_image(session: CommandSession):
    # 后续要将aliases的参数作为动态——
    """
    初步方案是用拼音模糊匹配
    """
    img = list.random_img(file.get_imgs())
    message = [
        {
            'type': 'image',
            'data': {
                'file': 'file:///' + img
            }
        }
    ]
    await session.send(message)


@on_command("max", aliases=("比大小"))
async def max(session: CommandSession):
    bot = randint(1, 7)
    usr = randint(1, 7)
    result = "你的投掷点数是" + str(usr) + "，我的投掷点数是" + str(bot) + "，"
    if bot > usr:
        result += "我赢了"
    else:
        result += "你赢了"
    await session.send(result)


@on_command('greet', only_to_me=False)
async def greet(session: CommandSession):
    message = session.state.get('text')
    now_time = time.localtime()
    print(message)
    print(now_time)
    result = ''
    if '早' in message:
        if 6 < now_time.tm_hour < 12:
            result = 'Bonjour, tout le monde.'
        else:
            result = 'まだ朝じゃない、バカ(还不是早上啦，笨蛋)'
    else:
        print(message)
        if now_time.tm_hour > 18:
            if '安' not in message:
                result = 'お疲れ様，早く休みなさい'
            else:
                result = 'おやすみなさい'
        else:
            result = 'まだ夜じゃない、バカ(还不是晚上啦，笨蛋)'
    await session.send(result)


@on_command('adapter_text', only_to_me=False)
async def adapter_text(session: CommandSession):
    message = session.state.get('text')
    if StrUtil.is_mathe_expression(message):
        print(message)
        result = str(eval(message))
        await session.send(result)
    else:
        await session.send(message)


@on_natural_language(only_short_message=False, only_to_me=False, allow_empty_message=True)
async def adapter(session: NLPSession):
    msg = session.msg
    if msg in greet_tuple:
        return IntentCommand(90.0, 'greet', args={'text': session.msg})
    elif not is_chines(msg) and not skip(msg):
        return IntentCommand(90.0, 'translate', args={'text': session.msg})
    else:
        return IntentCommand(randint(30, 70) * 1.0, 'adapter_text', args={'text': session.msg})
