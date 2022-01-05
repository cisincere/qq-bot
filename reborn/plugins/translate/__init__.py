from nonebot import CommandSession, on_command
from src.translate import o8in


@on_command("translate", aliases=("翻译", "翻译文本", "翻译文本"))
async def translate(session: CommandSession):
    message = session.state.get('text')
    result = o8in.translate(message)
    await  session.send(result)
