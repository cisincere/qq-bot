import re


class StrUtil:
    import re
    @staticmethod
    def is_mathe_expression(text:str):
        if re.sub(r'[+\-*/().]', '', text).isdigit():
            if text.count('--') <= 1 and text.count('++') <= 1 and text.count('..') <= 1:
                return True
            return False
        return False

