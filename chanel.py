#!/usr/bin/env python

# encoding=utf-8



import telegram



bot = telegram.Bot(token='1533748242:AAGNjEo_5YIDK8rpT64GuD9wBAV8CBi18zU') 

#생성한 텔레그램 봇 정보

me = bot.getMe()

print(me)

#사용자 id로 메시지 보내기

bot.sendMessage(-1001255979900, u'bot이 채널로 보낸 메시지')