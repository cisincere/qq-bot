import requests
import json


def translate(text):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        post_data = {
            "fromLang": "auto-detect",
            "text": text,
            "to": "zh-Hans",
            "token": "1U5kLeYJGVOgSjFXHagYbIesMMWihrWm",
            "key": "1641394673146"
        }

        post_url = "https://cn.bing.com/ttranslatev3?&IG=8027468AC2B6456A9F4DA3249555E018&IID=SERP.5518.15"

        res = requests.post(post_url, headers=headers, data=post_data)
        string = res.content.decode()
        return json.loads(string)[0]["translations"][0]["text"]
    except Exception as e:
        return '是服务器的错，不是我的错，呜呜呜呜~~'


