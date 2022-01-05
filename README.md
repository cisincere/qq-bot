# AsoulCnki-Bot v1.0

Date：2021-08-15

本文档未必适用于最新版本

## 安装

### 安装依赖
```bash
pip3 install -r requirements.txt
```

### 修改配置文件

配置文件位于 `bot/src/config/` 和 `go-cqhttp/config.yml` 下，其中，

[config.json](./bot/src/config/config.json)  存放爬虫的配置信息（爬取链接，关键词等）

[config.py](./bot/src/config/config.py) 记录数据库连接配置，nginx和爬虫的日志地址

[config.yml](./go-cqhttp/config.yml) 存放账号和密码等配置

<del>nginx日志只需配置到nginx日志对应文件夹，日志格式应当为 access-YYYY-mm-dd.log</del>

<del>日志格式问题，可以在 [这里](./bot/src/CommandExec/log.py) 自行修改 `accessTime()`</del>

<del>爬虫日志需要对应到**文件名**，建议使用 crontab 进行日志分割，保证每天的统计数据是正确的</del>

**由于已经使用GoAccess做日志分析，所以爬虫的日志分析可以弃用了**

## 项目结构

```
./
├── bot                    Bot 文件夹
│   ├── bot.py             Bot 入口文件
│   ├── plugins            nonebot 插件部分 所有的机器人指令
│   │   ├── help           机器人帮助指令
│   │   └── search         search 爬虫相关指令（系统状态相关目前存在耦合，待拆分）
│   └── src
│       ├── CommandExec    命令执行，数据库，日志分析相关模块
│       ├── config         存放配置文件
│       ├── globalConfig   全局配置模块
│       ├── spider         社交媒体爬虫
│       └── utils          工具函数
├── go-cqhttp              go-cqhttp
├── start.sh               一键启动
└── stop.sh                一键停止
```

## 启动项目

在配置完成后，可以准备启动机器人了，下面只介绍linux下的部署

window的部署方式类似，只是将启动go-cqhttp的文件换成exe

### 启动bot

切换到项目根路径，执行
```bash
./start.sh
```

### 重启bot
每次代码变动需要重启项目，由于start.sh会先执行杀掉存在的bot，所以可以直接执行`./start.sh`

### 停止bot
```bash
./stop.sh
```

## Bot指令，见/help