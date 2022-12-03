import telegram
from telegram.ext import Updater
from bs4 import BeautifulSoup
from telegram.ext import MessageHandler, Filters
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler

token = '5749030885:AAF6slWpaVp42caVUTPHKEIQg1hCdY_XIro'
id = '5680930767'
date = '20221214'
mobile_url = "https://m.cgv.co.kr/WebApp/Reservation/Schedule.aspx?tc=0013&rc=01&ymd=&fst=&fet=&fsrc="
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
bot = telegram.Bot(token = token)

def handler(update, context):
    user_text = update.message.text
    if user_text == "정지":
        bot.send_message(chat_id=id, text="실시간 알림 시스템이 종료되었습니다.")
        sched.pause()
    elif user_text == "재개":
        bot.send_message(chat_id=id, text="실시간 알림 시스템이 재개되었습니다.")
        sched.resume()

def job_function():
    theater_url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=" + date
    #op = webdriver.ChromeOptions()
    #op.add_argument('--headless')
    #browser = webdriver.Chrome(options=op)
    browser = webdriver.Chrome()
    browser.get(theater_url)
    browser.switch_to.frame('ifrm_movie_time_table')
    html = browser.page_source
    soup=BeautifulSoup(html,'xml')
    imax = soup.select_one('span.imax')
    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        if title == "아바타-물의 길":
            bot.sendMessage(chat_id=id, text=title + ' IMAX 예매가 열렸습니다. ' + '다음 링크에 접속하여 빠르게 예매하세요: ' + mobile_url)
            echo_handler = MessageHandler(Filters.text, handler)
            dispatcher.add_handler(echo_handler)


sched = BlockingScheduler(timezone='Asia/Seoul')
sched.add_job(job_function, 'interval', seconds=10)
sched.start()
