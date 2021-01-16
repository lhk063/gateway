#!/usr/bin/env python

# encoding=utf-8



import requests

import time

from bs4 import BeautifulSoup

import telegram

a=12361

bot = telegram.Bot(token='1533748242:AAGNjEo_5YIDK8rpT64GuD9wBAV8CBi18zU')



if __name__ == '__main__':

    # 제일 최신 게시글의 번호 저장
    latest_num = 0


    while True:
        req = requests.get('https://www.ddengle.com/market_personal')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all("tr", {"data-voted": "0"}) # 편법으로됨
        # posts = soup.find("tbody").find("tr").attr['data_document-srl'] # 안됨
        # posts = soup.find_all('tr', limit=1)




        print(posts)
        post_num = posts.find("td", {"class" : "no"}).text


        # 제일 최신 게시글 번호와 30초 마다 크롤링한 첫번째 게시글의 번호 비교
        # 비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        if latest_num != post_num :
            latest_num = post_num
            link = posts.find("td", { "class" : "title"}).find("a").attrs['href']
            title = posts.find("td", {"class" : "title"}).find("a").text

            text = '<땡글 게시글 업데이트>'+'\n'+title+'\n'+link  
            bot.sendMessage(-1001255979900, text)
            # 프롬프트 로그
            print(post_num)
            print(title)
            print(link)
        time.sleep(30) # 30초 간격으로 크롤링
        print('bot 동작 중 현재 게시글 번호' + latest_num)