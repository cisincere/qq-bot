#!/usr/bin/sh

./stop.sh

cd bot
nohup python3 bot.py &
cd ../go-cqhttp
nohup ./go-cqhttp &