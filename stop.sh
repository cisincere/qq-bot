#!/usr/bin/sh

ps aux | grep "python3 bot.py" | awk '{print $2}' | xargs kill -9
ps aux | grep "go-cqhttp" | awk '{print $2}' | xargs kill -9