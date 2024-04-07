from operator import itemgetter

from aiogram import *
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
import json
import random
import time
import datetime
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
import requests
import threading
import server
import token_get
from topers import *
from games import *

from flask import Flask, render_template, request
from threading import Thread

app = Flask('app')

tok = token_get.tok

bot = Bot(tok, parse_mode="HTML", disable_web_page_preview=True)
dp = Dispatcher(bot)

People = {}
promo = {}
pbl_lst = []
chat_in = []
bisnes = {}
pricer = {}
inf = {}
city = {}
Messages = {}
Ivent = {}
Inventer = {}
Laba = {}

lst_boss_ataced = {}
bit_cost = 0
hur_cost = 0

chanel = "https://t.me/GbBotBoarBot"
chanel_us = "@GbBotBoarBot"
chat = "https://t.me/boarBotTrykaban"
chat_us = "@boarBotTrykaban"
chanel_promo = "https://t.me/GbPromokods"
chanel_promo_us = "@GbPromokods"
kaban = "@Trykaban"
chat_id = -1001806713364
chanel_id = -1001842985432
promo_chat = -1001888963287
my_id = 870264076

id_bd_save = -4038331532
start = 1

time_start = datetime.now()
time_save_bd = datetime.now()

flash_limit = 95000000

boses = {"1": {"hp": 2500, "type": 1}, "2": {"hp": 2500, "type": 1}, "3": {"hp": 2500, "type": 1}, "4": {"hp": 2500, "type": 1}, "5": {"hp": 2500, "type": 1}, "6": {"hp": 2500, "type": 1}}
for_bisnes = {"1": {"num": 1, "nalog_pay": 1000, "nalog": 5000, "cost": 80000, "pay": 4500, "name":"частая школа", "t1": "учащихся мест", "mon_p":1000, "upC":10000},
              "2": {"num": 2, "nalog": 10000, "nalog_pay": 1900, "cost": 120000, "pay": 20000, "name":"частная больница", "t1": "больничных коек", "mon_p":10000, "upC":30000},
              "3": {"num": 3, "nalog_pay": 2300, "nalog": 15000, "cost": 300000, "pay": 80000, "name":"туристический отдел", "t1": "турестических программ", "mon_p":20000, "upC":100000},
              "4": {"num": 4, "nalog_pay": 3000, "nalog": 25000, "cost": 340000, "pay": 100000, "name":"прокат машин", "t1": "уровень элитности машин", "mon_p":40000, "upC":10000},
              "5": {"num": 5, "nalog_pay": 3400, "nalog": 30000, "cost": 400000, "pay": 120000, "name":"прокат яхт", "t1": "количество яхт", "mon_p":100000, "upC":10000},
              "6": {"num": 6, "nalog_pay": 5000, "nalog": 60000, "cost": 550000, "pay": 140000, "name":"компания по инвестированию", "t1": "количество соотрудников", "mon_p":100000, "upC":10000},
              "7": {"num": 7, "nalog_pay": 6500, "nalog": 75000, "cost": 630000, "pay": 175000, "name":"пекарня", "t1": "количество печек", "mon_p":200000, "upC":10000},
              "8": {"num": 8, "nalog_pay": 9000, "nalog": 1000000, "cost": 700000, "pay": 190000, "name":"Киностудия", "t1": "уровень студии", "mon_p":30000, "upC":10000},
              "9": {"num": 9, "nalog_pay": 13000, "nalog": 1500000, "cost": 850000, "pay": 240000, "name":"аэропорт", "t1": "количество рейсов", "mon_p":40000, "upC":10000},
              "10": {"num": 10, "nalog_pay": 15000, "nalog": 1560000, "cost": 900000, "pay": 260000, "name":"обувной магазин", "t1": "пространство магазина", "mon_p":50000, "upC":10000},
              "11": {"num": 11, "nalog_pay": 15000, "nalog": 1600000, "cost": 1000000, "pay": 300000, "name":"компания по созданию сайтов", "t1": "количество сотрудников", "mon_p":50000, "upC":300000},
              "12": {"num": 12, "nalog_pay": 16000, "nalog": 1800000, "cost": 500000000, "pay": 12000000, "name":"it школа", "t1": "учащихся мест", "mon_p":50000, "upC":700000},
              "13": {"num": 13, "nalog_pay": 17000, "nalog": 1650000, "cost": 1000000000, "pay": 15000000, "name":"свой ИИ", "t1": "привлечённых инвесторов", "mon_p":1000000, "upC":750000},
              "14": {"num": 14, "nalog_pay": 18000, "nalog": 1100000, "cost": 10000000000, "pay": 25000000, "name":"производство крутых тачек из 90-ых", "t1": "ваших инвесторов", "mon_p":1000000, "upC":800000},
              "15": {"num": 15, "nalog_pay": 19000, "nalog": 2000000, "cost": 15000000000, "pay": 28000000, "name":"завод", "t1": "количество станков", "mon_p":1000000, "upC":1000000}}

keis_information = {"1": {"inventor": [1, 1, 2, 1, 2, 1, 2], "cost": 500000000},
                    "2": {"inventor": [3, 3, 3, 4, 1, 2, 3], "cost": 750000000},
                    "3": {"inventor": [4, 4, 4, 4, 5, 5, 6, 7, 7], "cost": 1000000000},
                    "4": {"inventor": [6, 6, 7, 7, 7, 6, 6, 7], "cost": 2500000000}}

books = {"1": {"type": 1, "name": "Отвёртка", "boost": [3, 4, 5, 6]},
         "2": {"type": 1, "name": "молоток", "boost": [10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20]},
         "3": {"type": 1, "name": "нож", "boost": [13, 13, 13, 14, 14, 11, 11, 1, 1, 1, 15, 25]},
         "4": {"type": 1, "name": "кувалда", "boost": [18, 18, 18, 25]},
         "5": {"type": 1, "name": "дрель", "boost": [20, 21]},
         "6": {"type": 1, "name": "огнемёт", "boost": [23]},
         "7": {"type": 1, "name": "молот тора", "boost": [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,100]}}

vips = {"1":{"name":"Silver Vip"}, "2":{"name":"Silver Vip"}, "3":{"name":"Platinum Vip"}}

kmn_stavka_pers = {}
link="https://omniscient-jolly-trade.glitch.me/"
###---база данных---###
def load():
    global People, promo, pbl_lst, bisnes, chat_in, pricer, inf, city, Messages, Inventer, Laba
    try:
        f1 = open("persons.json", "r")
        People = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("messages.json", "r")
        Messages = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("promo.json", "r")
        promo = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("publick", "r")
        pbl_lst = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("bisnes.json", "r")
        bisnes = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("in_chat.json", "r")
        chat_in = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("razdacha.json", "r")
        pricer = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("information.json", "r")
        inf = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("inventer.json", "r")
        Inventer = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    try:
        f1 = open("Labar.json", "r")
        Laba = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

    load_ivent()

def save():
    global People
    f1 = open("persons.json", "w")
    json.dump(People, f1, ensure_ascii=False)
    f1.close()

def save2():
    global People
    f1 = open("promo.json", "w")
    json.dump(promo, f1, ensure_ascii=False)
    f1.close()


def save3():
    global bisnes
    f1 = open("bisnes.json", "w")
    json.dump(bisnes, f1, ensure_ascii=False)
    f1.close()

def save4():
    global inf
    f1 = open("information.json", "w")
    json.dump(inf, f1, ensure_ascii=False)
    f1.close()

def save5():
    global city
    f1 = open("Places.json", "w")
    json.dump(city, f1, ensure_ascii=False)
    f1.close()

def save_laba():
    global Laba
    f1 = open("Labar.json", "w")
    json.dump(Laba, f1, ensure_ascii=False)
    f1.close()

def inventer_save():
    global Inventer
    f1 = open("inventer.json", "w")
    json.dump(Inventer, f1, ensure_ascii=False)
    f1.close()

def save_message():
    global Messages
    f1 = open("messages.json", "w")
    json.dump(Messages, f1, ensure_ascii=False)
    f1.close()
    threading.Timer(10.0, save_message).start()


def dup_to_people(kkk, key, value):
    global People
    low = People[kkk]
    if key not in low.keys():
        low[key] = value
    People[kkk] = low
    save()


def chater_of(kkk, id_chat):
    kkk = str(kkk)
    id_chat = str(id_chat)
    if kkk not in chat_in and id_chat == "-1001806713364":
        chat_in.append(kkk)
        f1 = open("in_chat.json", "w")
        json.dump(chat_in, f1)
        f1.close()
        return 1
    else:
        return 0


async def chek_people(kkk, param):
    if kkk not in People.keys() or param == "1":
        if param == "1":
            idd = People[kkk]['game_id']
        elif param == "0":
            idd = People['idd']

        if param == "1":
            try:
                await bot.send_message(870264076, f"Obnul! -- Before In Baze \n\n{People[kkk]}")
            except:
                pass

        People[kkk] = {
            "game_id": idd,
            "ban": 0,
            "name": f"игрок:{idd}",
            "balance": 5000000,
            "boost1": 0,
            "admin": 0,
            "promo": 0,
            "boss_hp": 0,
            "time_farm1": "",
            "time_farm2": "tm",
            "bitcoin": 0,
            "place": 1,
            "inventer": [],
            "ks_1": 0,
            "ks_2": 0,
            "ks_3": 0,
            "ks_4": 0,
            "keis_col": 0,
            "state_prem":{"kol": 0, "true": 0, "information": 0, "limit": 0, "name": "\u0424\u043b\u044d\u0448"},
            "users": [],
            "invetner": "1",
            "bisnes_levl": 0,
            "harry": 0,
            "skil": 0,
            "bank": 0,
            "date": str(datetime.now())
        }

        if param == "0":
            try:
                await bot.send_message(870264076, f"Зареался новый поьзователь. In Baze: \n\n{People[kkk]}")
            except:
                pass
            People['idd'] += 1

        save()


def create1(kkk, num, msg):
    global bisnes
    bisnes[kkk] = {"balance": 0,
                   "date": str(msg.date),
                   "start": str(msg.date),
                   "nalog": 0,
                   "number": str(num)
                   }

    save3()


def sender(msg):
    global pbl_lst
    if msg.chat.id not in pbl_lst:
        pbl_lst.append(msg.chat.id)
        f1 = open("publick", "w")
        json.dump(pbl_lst, f1)
        f1.close()


###-конец базы данных-###






#              IVENTS                           IVENTS
def load_ivent():
    global Ivent
    try:
        f1 = open("ivent_money.json", "r")
        Ivent = json.load(f1)
        f1.close()
    except:
        print("Не удалось загрузить файл")

def save_ivent():
    global Ivent
    f1 = open("ivent_money.json", "w")
    json.dump(Ivent, f1, ensure_ascii=False)
    f1.close()

def chek_ivent(msg):
    if str(msg.from_user.id) not in Ivent.keys():
        Ivent[str(msg.from_user.id)] = {"money":0, "items":[]}
        save_ivent()

IVENT_SET = True





###-валюта-###
def val_cost():
    global bit_cost, hur_cost
    DOLLAR_RUB = "https://g.co/kgs/pTQitx"
    btc_RUB = "https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C5CHFA_enRU989RU989&oq=%2Cbnrjby+r+he%2Ck&aqs=chrome.1.69i57j0i10i131i433i512j0i10i512l6.166408062j1j7&sourceid=chrome&ie=UTF-8"
    # Заголовки для передачи вместе с URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    full_page = requests.get(DOLLAR_RUB, headers=headers)
    full_page2 = requests.get(btc_RUB, headers=headers)
    # Разбираем через BeautifulSoup
    soup = BeautifulSoup(full_page.content, 'html.parser')
    soup2 = BeautifulSoup(full_page2.content, 'html.parser')


    # Получаем нужное для нас значение и возвращаем его
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    convert2 = soup2.findAll("span", {"class": "pclqee"})
    data = convert[0].text
    btc = ""
    for i in data:
        if i == "," or i == ".":
            pass
        else:
            btc += i

    rd = random.randint(400, 550)
    bit_cost = (int(btc) * 4) + (rd*2)

    print(f"фиткоин стоит: {bit_cost}")


    data = convert2[0].text
    btc = ""
    for i in data:
        if i == "," or i == "." or i == " ":
            pass
        else:
            btc += i

    hur_cost = (int(btc) * 4)

    print(f"harry стоит: {hur_cost}")
    threading.Timer(60, val_cost).start()


#####----функции----#####
def money_form(mon):
    mon = str(mon)
    idd = -1
    ctr = 1
    rez = ""
    for i in range(len(mon)):
        if ctr == 4:
            ctr = 1
            rez += "."
        rez += mon[idd]
        ctr += 1
        idd -= 1

    rez = rez[::-1]
    return rez


def bisnes_go(msg, num):
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    date_last_farm = datetime.strptime(str(bisnes[kkk]["date"]), "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
    tm = date2 - date_last_farm
    tm2 = int(tm.total_seconds())

    if tm2 < 3600:

        txt = f"({bisnes[kkk]['number']}) {mention}, ваш бизнес {for_bisnes[bisnes[kkk]['number']]['name']} \n\n" \
              f"  уровень: {People[kkk]['bisnes_levl']}/5 \n" \
              f"  на счету: {money_form(bisnes[kkk]['balance'])} \n" \
              f"  налог: {money_form(bisnes[kkk]['nalog'])}/{money_form(for_bisnes[bisnes[kkk]['number']]['nalog'])} \n" \
              f"  \n" \
              f"стоимость улучшения: {for_bisnes[num]['upC']}\n" \
              f"снять деньги с бизнеа: бизнес снять\n" \
              f"оплатить налог: бизнес налог\n"
        return txt
    else:
        col = tm2 // 3600
        nalog = for_bisnes[num]['nalog']
        nalog_pay = for_bisnes[num]['nalog_pay']
        pay = for_bisnes[num]['pay']
        nalog_do = bisnes[kkk]['nalog']
        pay_do = bisnes[kkk]['balance']

        lvl = People[kkk]['bisnes_levl']
        up = for_bisnes[num]['mon_p']
        pay_pl = int(lvl) * int(up)
        for i in range(col+10000):
            if nalog_do >= nalog or i == col:
                bisnes[kkk]['nalog'] = nalog_do
                bisnes[kkk]['balance'] = pay_do
                bisnes[kkk]['date'] = str(msg.date)
                break
            else:
                nalog_do += nalog_pay
                pay_do += pay_pl
                pay_do += pay

        txt = f"({bisnes[kkk]['number']}) {mention}, ваш бизнес {for_bisnes[bisnes[kkk]['number']]['name']} \n\n" \
              f"  уровень: {People[kkk]['bisnes_levl']}/5 \n" \
              f"  на счету: {money_form(bisnes[kkk]['balance'])}\n" \
              f"  налог: {money_form(bisnes[kkk]['nalog'])}/{money_form(for_bisnes[bisnes[kkk]['number']]['nalog'])} \n" \
              f"  \n" \
              f"стоимость улучшения: {for_bisnes[num]['upC']}\n" \
              f"снять деньги с бизнеа: бизнес снять\n" \
              f"оплатить налог: бизнес налог\n"

        save3()
        return txt



########-команды-########
@dp.message_handler(content_types=['new_chat_members'])
async def new_user_joined(message: types.Message):
    try:
        for i in message.new_chat_members:
            if message.chat.id == -1001806713364:
                kkk = str(message.from_user.id)
                id_chat = str(message.chat.id)
                kkk2 = str(i['id'])
                mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
                if kkk2 in People[kkk]['users']:
                    await bot.send_message(message.chat.id, "Вы уже добавляли тогоо человека, или он присоеденился по вашей реф сылке")
                else:
                    await bot.send_message(message.chat.id, f"{mention}, вы добавили нового игрока! вот ваша награда +90.000")
                    People[kkk]['balance'] += 90000
                    People[kkk]['users'].append(kkk2)
                    await chek_people(kkk2, "0")
                    chek_people_not_fun = chater_of(kkk2, id_chat)
                    if chek_people_not_fun == 1:
                        mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                        await bot.send_message(message.chat.id, f"{mention2}, вы присоеденились! ваша награда +50.000")
                        People[kkk2]['balance'] += 50000
                    if People[kkk]['state_prem']['kol'] == 20:
                        People[kkk]['state_prem']['true'] = 1
                        People[kkk]['state_prem']['limit'] = 0
                        People[kkk]['state_prem']['information'] = str(datetime.now().day)
                        try:
                            await bot.send_message(int(kkk), "Ваш новый статус Флэш!")
                        except:
                            pass

                    save()

    except:
        pass


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

@dp.message_handler(commands=["start"], state="*")
async def user_registration(msg: types.Message):
    unique_code = extract_unique_code(msg.text)
    if unique_code:
        kkk2 = str(msg.from_user.id)
        kkk = str(unique_code)
        if kkk2 in People[kkk]['users']:
            await bot.send_message(msg.chat.id, "Вы уже присоеденялись по этой ссылке или этот человек добавил вас в чат")
        else:
            mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
            await bot.send_message(msg.chat.id, f"ого! вы вступили по рефф ссылке этого человека {mention}")
            People[kkk]['users'].append(kkk2)
            People[kkk]['balance'] += 1000000
            People[kkk]['state_prem']['kol'] += 1
            if People[kkk]['state_prem']['kol'] == 20:
                People[kkk]['state_prem']['true'] = 1
                People[kkk]['state_prem']['limit'] = 0
                People[kkk]['state_prem']['information'] = str(datetime.now().day)
                try:
                    await bot.send_message(int(kkk), "Ваш новый статус Флэш!")
                except:
                    pass

            save()
    else:
        pass
    txt_hello = f"привет, это 𝓖𝓑 𝓑𝓞𝓘\n" \
                f"Ты автоматически зарегестрировался,чтобы узнать подробнее о своём профиле обратись к команде 'проф'. если есть вопросы - 'помощь' \n \n" \
                f"у нас также есть: \n" \
                f"канал - {chanel_us}\n" \
                f"чат - {chat_us}) \n" \
                f"промокоды - {chanel_promo_us}"

    await bot.send_message(msg.chat.id, txt_hello)

@dp.message_handler(commands=['icecream'])
async def send_welcome(msg: types.Message):
    txt_icecream = f"🍨icecream - Специальная валюта. По ней можно купить вещи(магазин), она позволит вам за актив в главном чате% получать вознагрождение! \n" \
                   f"\n" \
                   f"Её нельзя купить, но можно продать. Благодаря мороженному появятся темы, вип. Вип даст больше возможностей!\n"
    await bot.send_message(msg.chat.id, txt_icecream)

@dp.message_handler(commands=['buttons'])
async def send_welcome(msg: types.Message):

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Открыть", web_app=WebAppInfo(url=link + "/inventer?id=" + str(msg.from_user.id))))
    if msg.chat.type != "private":
        bt = InlineKeyboardMarkup()
        bt.add(InlineKeyboardButton("Открыть tg app", url="t.me/True_gb_bot/TryGbapp"))
        await bot.send_message(msg.chat.id, "❤️Волшебная кнопка входа в мир гб! нажми на кнопку, чтобы открыть интерфейс бота \n\n💬Или поделись ссылкой для входа из любого места телеграм! \nt.me/True_gb_bot/TryGbapp", reply_markup=bt)
    else:
        await bot.send_message(msg.chat.id, "Вот твои кнопки!", reply_markup=markup)

@dp.message_handler(commands=['lnk'])
async def send_welcome(msg: types.Message):
    L1 = msg.text.split()
    kkk = str(msg.from_user.id)
    try:
        if pricer['is_do'] == "True":
            if kkk in pricer['users']:
                await bot.send_message(msg.chat.id, "Вы уже учавствуете!")
            else:
                if L1[1] not in pricer['another'].keys():
                    await bot.send_message(msg.chat.id, "Увы,владелец ссылки ещё сам не участвует в розыгрыше(")
                else:
                    await bot.send_message(msg.chat.id, "Вы приняли уастие в раздаче через приглашение пользователя, ваш приз уже у вас! +500.000")
                    try:
                        await bot.send_message(L1[1], "кто-то принял участиве в раздаче через ваше приглашение! Вы получили +250.000")
                    except:
                        pass

                    People[kkk]['balance'] += 500000
                    People[L1[1]]['balance'] += 250000
                    save()


                    pricer['users'].append(kkk)
                    pricer['another'][kkk] = 0
                    pricer['another'][L1[1]] += 1
                    pricer['kol'] += 1


                    mk = InlineKeyboardMarkup()
                    btn1 = InlineKeyboardButton(f"Участвовать 🚀{pricer['kol']}", callback_data=f"razdacha:{pricer['num']}")
                    mk.add(btn1)
                    f1 = open("razdacha.json", "w")
                    json.dump(pricer, f1)
                    f1.close()
        else:
            await bot.send_message(msg.chat.id, "Увы, сейчас нету раздачи(")
    except:
        pass

@dp.message_handler(commands=['report'])
async def send_welcome(msg: types.Message):
    kkk = str(msg.from_user.id)
    L1 = msg.text.split()
    if msg.reply_to_message:
        kkk2 = str(msg.reply_to_message.from_user.id)
        mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
        mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
        txt = ""
        if len(L1) == 1:
            txt = "нет уточнений("
        else:
            idd = 0
            for i in L1:
                if idd == 0:
                    pass
                else:
                    txt += i
                    txt += " "
                idd += 1
        txt_report = f"report operation 𝓖𝓑 𝓑𝓞𝓘 \n" \
                     f"{mention}, вы отправили реопрт на {mention2}\n" \
                     f"уточнения  репорте: {txt}\n" \
                     f"\n" \
                     f"отправитель: \n" \
                     f"id: {kkk}\n" \
                     f"game id: {People[kkk]['game_id']}\n" \
                     f"\n" \
                     f"обвиняемый:\n" \
                     f"id: {kkk2}\n" \
                     f"game id: {People[kkk2]['game_id']}\n" \
                     f"\n" \
                     f"**не отправляйте репорты сильно часто! можете отхватить бан!** \n" \
                     f"#report"

        await bot.send_message(msg.chat.id, txt_report)
        await bot.send_message(my_id, txt_report)
        await bot.forward_message(my_id, msg.chat.id, msg.reply_to_message.message_id)
    else:
        await bot.send_message(msg.chat.id, "вы отправли не ответом на сообщение!")



@dp.message_handler(commands=["LabaHelp"], state="*")
async def user_registration(msg: types.Message):
    global People
    kkk = str(msg.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    txt = f"{mention}, Книга помощи для вашей лабараториии: \n" \
          f"\n" \
          f"1. Смена названя продукта -- Продукт (Название)\n" \
          f"\n" \
          f"❗️владелец не несёт ответственность за название вашего игрового продукта"

    await bot.send_message(msg.chat.id, txt)
znaks = {"1":{"nm":"P123 ER", "cost":95000},"2":{"nm":"P888 PP", "cost":10000000000},"3":{"nm":"A984 DF", "cost":95000},"4":{"nm":"CM635 MK", "cost":95000}, "5":{"nm":"C065 MK", "cost":95000}, "6":{"nm":"M000 MM", "cost":5000000000}, "7":{"nm":"HG956 MK", "cost":100000}, "8":{"nm":"C456 DF", "cost":100000}, "9":{"nm":"GH586 KM", "cost":105000}}
@dp.message_handler(commands=["numer"], state="*")
async def user_registration(msg: types.Message):
    global People
    kkk = str(msg.from_user.id)
    if 'znaks' not in People[kkk].keys():
        People[kkk]['znaks'] = []
        save()

    rm = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("Начать 100к", callback_data="NewNum")
    rm.add(b1)
    await bot.send_message(msg.chat.id, "Игра 'Слови знак', Для начала игры нажмите кнопку начать \n\nВнимание, Псоле нажатия на кнопку начать вы потратите 100.000", reply_markup=rm)


########-система-########
@dp.message_handler()
async def sistema(msg: types.Message):
    global boss_1, boss_1_type, my_id, bit_cost, time_save_bd, Messages, People
    kkk = str(msg.from_user.id)
    id_chat = str(msg.chat.id)
    await chek_people(kkk, "0")
    sender(msg)
    #####
    chat_cheker = chater_of(kkk, id_chat)
    if chat_cheker == 1:
        await bot.send_message(msg.chat.id, "Вы уже существуете в чате! вот ваша повышеная нарада +5.000.000.000")
        People[kkk]['balance'] += 5000000000
        save()

    L1 = msg.text.split()
    if L1[0] == "+пароль":
        if len(L1) == 2:
            pasword = L1[1]
            if len(pasword) < 4 or len(pasword) > 12:
                await bot.send_message(msg.chat.id, "Пароль должен содержать от 4, до 12 симолов")
            else:
                if 'passord' not in People[kkk].keys():
                    People[kkk]['passord'] = pasword
                else:
                    People[kkk]['passord'] = pasword

                await bot.send_message(msg.chat.id, f"Вы сменили свой пароль. \n\nДля входа в аккаунт:\nлогин: {msg.from_user.id}\nпароль: {pasword}")

                save()
    mention = "<a href='tg://openmessage?user_id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    if People[kkk]['ban'] == 2:
        pass
    elif People[kkk]['ban'] == 1:
        await bot.send_message(
            msg.chat.id,
            f"📛{mention}, вы забанены напишите владельцу для дальнейших уточнений {kaban}"
        )
        People[kkk]['ban'] = 2
        save()
    try:
        await bot.forward_message(-954072151, msg.chat.id, msg.message_id)
    except:
        pass
    else:
        try:
            if "premium" in People[kkk].keys():
                if People[kkk]["premium"]['pr'] != "0":
                    date_last_farm = datetime.strptime(str(People[kkk]['premium']['date']).split(".")[0], "%Y-%m-%d %H:%M:%S")
                    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                    time_difference = date_last_farm - date2
                    sec_difference = time_difference.total_seconds()
                    if sec_difference < 0:
                        await bot.send_message(msg.chat.id, f"{mention}, у вас закончился вип статус). Надеюсь вы скоро вернётесь в наши вип ряды!")
                        People[kkk]['premium']['pr'] = "0"
                        People[kkk]['premium']['date'] = ""
                        save()

            if msg.chat.id == chat_id:
                if kkk not in Messages:
                    Messages[kkk] = 0

                Messages[kkk] += 1
                if Messages[kkk] >= 50:
                    if "icecream" not in People[kkk].keys():
                        People[kkk]['icecream'] = 0

                    Messages[kkk] = 0

                    People[kkk]['icecream'] += 10
                    save()


            control = 0
            ###    настройки     ####
            if L1[0] == "+ник":
                control = 1
                if len(L1) >= 2:
                    People[kkk]['name'] = L1[1]
                    save()
                    await bot.send_message(msg.chat.id, f"{mention}, вы сменили ник на -> {L1[1]}")
                else:
                    await bot.send_message(msg.chat.id, "а имя")

            if msg.text in ["Премиум","премиум"]:
                if "premium" not in People[kkk].keys():
                    await bot.send_message(msg.chat.id, "У вас нету вип. Купить можно в разделе 'магазин(м)'")
                else:
                    if People[kkk]['premium']['pr'] == "0":
                        await bot.send_message(msg.chat.id, "У вас нету вип(просрочился / не приобритён). Купить можно в разделе 'магазин(м)'")
                    elif People[kkk]['premium']['pr'] == "1":
                        txt_vip = f"{mention}, Ваш вип пропуск: \n" \
                                  f"👑SILVER VIP👑, до {People[kkk]['premium']['date'].split('.')[0]}"
                        await bot.send_photo(msg.chat.id, open("assets/vip1.jpeg", "rb"), caption=txt_vip)
                    elif People[kkk]['premium']['pr'] == "2":
                        txt_vip = f"{mention}, Ваш вип пропуск: \n" \
                                  f"🔱GOLD VIP🔱, до {People[kkk]['premium']['date'].split('.')[0]}"
                        await bot.send_photo(msg.chat.id, open("assets/vip1.jpeg", "rb"), caption=txt_vip)
                    elif People[kkk]['premium']['pr'] == "3":
                        txt_vip = f"{mention}, Ваш вип пропуск: \n" \
                                  f"⚜️PLATINUM VIP⚜️, до {People[kkk]['premium']['date'].split('.')[0]}"
                        await bot.send_photo(msg.chat.id, open("assets/vip1.jpeg", "rb"), caption=txt_vip)

            if msg.text in ["Магазин","магазин","Магаз","магаз","М","м"]:
                rb_k = InlineKeyboardMarkup()
                rb_k.add(InlineKeyboardButton("Темы🎭", callback_data="vipTheme_1"))
                rb_k.add(InlineKeyboardButton("Vip👑", callback_data="vipShop_3"))

                await bot.send_message(msg.chat.id, "Магазин", reply_markup=rb_k)


            if msg.text in ["чат", "Чат"]:

                txt = f"{mention}, Всё, что мне известно: \n" \
                      f"🚀сообщения: {Messages[kkk]}/50 \n" \
                      f"\n" \
                      f"❓Напишите 50 сообщений, чтобы получить мороженной\n" \
                      f"мороженное - /icecream\n"
                await bot.send_message(msg.chat.id, txt)

            if L1[0] in ["Кейсы", "кейсы", "Кейс", "кейс"]:
                control = 1
                if len(L1) == 1:
                    ks_txt = ""
                    control_v = 0
                    i = People[kkk]
                    if i['ks_1'] > 0:
                        ks_txt += f"1. 💼бесплатный - {i['ks_1']}шт.\n"
                        control_v += 1
                    if i['ks_2'] > 0:
                        ks_txt += f"2. 🔥хороший - {i['ks_2']}шт.\n"
                        control_v += 1
                    if i['ks_3'] > 0:
                        ks_txt += f"3. 💰богатый - {i['ks_3']}шт.\n"
                        control_v += 1
                    if i['ks_4'] > 0:
                        ks_txt += f"4. 😎секретный - {i['ks_4']}шт.\n"
                        control_v += 1

                    if control_v > 0:
                        ks_txt = "\n\nКейсы в вашем инвенторе: \n" + ks_txt

                    st_txt = ""
                    if People[kkk]['state_prem']['true'] == 1:
                        status = People[kkk]['state_prem']['name']
                        st_txt = f"<b>[{status}]</b>"

                    txt_ks = f"📦{st_txt}{mention}, доступные кейсы: \n\n" \
                             f"1. 💼бесплатный кейс - {money_form(keis_information['1']['cost'])}👾\n" \
                             f"2. 🔥хороший кейс - {money_form(keis_information['2']['cost'])}👾\n" \
                             f"3. 💰богатый кейс - {money_form(keis_information['3']['cost'])}👾\n" \
                             f"4. 😎секретный кейс - {money_form(keis_information['4']['cost'])}👾" \
                             f" {ks_txt} \n\n" \
                             f"купить кейс: кейс купить (номер) (количество) \n" \
                             f"открыть кейс: кейс открыть (номер) (количество)"

                    await bot.send_message(msg.chat.id, txt_ks)
                elif len(L1) >= 4:
                    control = 1
                    if L1[1] in ["купить", "Купить"]:
                        num = L1[2]
                        kol = L1[3]
                        cost = keis_information[num]['cost']
                        try:
                            name_2 = await bot.send_message(msg.chat.id, "Кейсы подсчитываються!")
                            if cost * int(kol) > People[kkk]['balance'] or int(kol) < 0:
                                await bot.send_message(msg.chat.id, f"{mention}, У вас не хватило денег")
                            else:
                                People[kkk]['balance'] -= cost * int(kol)
                                People[kkk][f"ks_{num}"] += int(kol)
                                save()
                                await bot.edit_message_text(f"{mention}, вы купили {kol} кейс(ов). номер кейcов {num}", msg.chat.id, name_2.message_id)
                        except:
                            await bot.send_message(msg.chat.id,
                                                   f"{mention}, увы что-то пошло не так. \nкейс купить (номер) (количество)")

                    if L1[1] in ["открыть", "Открыть"]:
                        num = L1[2]
                        kol = L1[3]
                        try:
                            if People[kkk][f'ks_{num}'] < int(kol) or int(kol) < 1:
                                await bot.send_message(msg.chat.id, f"{mention}, У вас не хватило кейсов или открывать меньше одного кейса нельзя")
                            else:
                                if int(kol) > 100:
                                    await bot.send_message(msg.chat.id, "больше чем 100, открывать нельзя")
                                else:
                                    name = await bot.send_message(msg.chat.id, "Кейсы открываются!")
                                    txt_pricer = f"{mention}, ваш выигрыш!\n\n"
                                    low = keis_information[num]
                                    pr_do = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}
                                    for i in range(int(kol)):
                                        i += 1
                                        set = str(random.choice(low['inventor']))
                                        pr_do[set] += random.choice([10,11,12,13,20,10,10,10,12])


                                    for i, y in pr_do.items():
                                        if y > 0:
                                            txt_pricer += f"{books[i]['name']} -- {y}\n"
                                            if i not in People[kkk].keys():
                                                People[kkk][i] = int(y)
                                            else:
                                                People[kkk][i] += int(y)
                                    People[kkk][f"ks_{num}"] -= int(kol)
                                    save()
                                    await bot.edit_message_text(txt_pricer,msg.chat.id, name.message_id)

                        except:
                            await bot.send_message(msg.chat.id,
                                                   f"{mention}, увы что-то пошло не так. \nкейс открыть (номер) (количество)")

            if msg.text in ["Предметы","предметы","П","п"]:
                control = 1
                txt_lets = f"{mention}, Все доступные предметы: \n\n"
                for i, y in books.items():
                    txt_lets += f"{i}. {y['name']}, \n" \
                                f" урон: {min(y['boost'])}/{max(y['boost'])} \n\n"
                await bot.send_message(msg.chat.id, txt_lets)

            if msg.text in ["Мои предметы","мои предметы"]:
                control = 1
                txt_prdmet = ""
                for i, y in People[kkk].items():
                    for feet in range(10):
                        ifeet = str(feet)
                        if ifeet == i:
                            if People[kkk][i] >= 1:
                                txt_prdmet += f"{ifeet}. {books[i]['name']} - {People[kkk][ifeet]} \n" \
                                              f" урон: {min(books[i]['boost'])}/{max(books[i]['boost'])} \n\n"

                if txt_prdmet == "":
                    await bot.send_message(msg.chat.id, "У вас нет предметов")
                else:
                    txt_prdmet = f"{mention}, Вот ваши предметы! \n\n" + txt_prdmet
                    await bot.send_message(msg.chat.id, txt_prdmet)

            if msg.text in ["Помощь", "помощь"]:
                control = 1
                txt_help = f"{mention}, мои команды:\n" \
                           f"🆘 /report [фраза] - обратиться к администрации.\n\n" \
                           f"  1.💰 заработок \n" \
                           f"  2.🎰 игры \n" \
                           f"  3.🚀 основные\n" \
                           f"  4.⚗ лабаратория\n\n" \
                           f"❓Нажми на кнопки, чтобы узнать подробнее."

                bt_m = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("💰заработок", callback_data="job")
                b2 = InlineKeyboardButton("🎰игры", callback_data="happy")
                b3 = InlineKeyboardButton("🚀основные", callback_data="main")
                b4 = InlineKeyboardButton("⚗Лабаратория", callback_data="laba")
                bt_m.add(b1, b2)
                bt_m.add(b3)
                bt_m.add(b4)
                await bot.send_sticker(msg.chat.id, sticker="CAACAgIAAxkBAAJEF2UUeRqkdX21_IDUT2a6MczXJCYhAAKNOgACoi3oSnpCZw-6xdX5MAQ")
                await bot.send_message(msg.chat.id, txt_help, reply_markup=bt_m)

            if msg.text in ["мои знаки", "Мои знаки"]:
                if 'znaks' not in People[kkk].keys() or len(People[kkk]['znaks']) == 0:
                    await bot.send_message(msg.chat.id, "у вас нету знаков, начать игру --> /numer")
                else:
                    txt_nums = ""
                    kol = 1
                    for i in People[kkk]['znaks']:
                        txt_nums += f"\n🔒{kol}. {znaks[i]['nm']} \n" \
                                    f"   🏦Г.цена - {znaks[i]['cost']}"
                        kol += 1

                    txt_nums += "\n\nначать игру --> /numer"
                    await bot.send_message(msg.chat.id, txt_nums)


            if msg.text in ["Бизнесы", "бизнесы"]:
                control = 1
                txt = "список бизнесов, доступных на дынный момент: \n\n"
                for i, y in for_bisnes.items():
                    txt += f"💼{i}. {y['name']}:\n" \
                           f"  🔥прибыль: {y['pay']}/1h.\n" \
                           f"  💰стоимость: {y['cost']}👾\n"

                txt += "\n\nдля покупки: бизнес купить[num]"
                await bot.send_message(msg.chat.id, txt)

            if L1[0] in ["Бизнес", "бизнес"]:
                control = 1
                if len(L1) >= 3:
                    if L1[1] in ["Купить", "купить"]:
                        if int(L1[2]) <= 15 and int(L1[2]) >= 1:
                            if kkk in bisnes.keys():
                                if bisnes[kkk]["number"] == str(L1[2]):
                                    await bot.send_message(msg.chat.id, f"{mention}, вы уже купили данный бизнес")
                                else:
                                    if People[kkk]['balance'] >= for_bisnes[L1[2]]["cost"]:
                                        create1(kkk, L1[2], msg)
                                        People[kkk]['balance'] -= for_bisnes[L1[2]]["cost"]
                                        People[kkk]['bisnes_levl'] = 0
                                        save()
                                        await bot.send_message(msg.chat.id,
                                                               f"{mention}, вы купили бизнес за {money_form(for_bisnes[L1[2]]['cost'])}")
                                    else:
                                        await bot.send_message(msg.chat.id,
                                                               f"{mention}, у вас не хватило средств на покупки бизнеса")
                            else:
                                if People[kkk]['balance'] >= for_bisnes[L1[2]]["cost"]:
                                    create1(kkk, L1[2], msg)
                                    People[kkk]['balance'] -= for_bisnes[L1[2]]["cost"]
                                    save()
                                    await bot.send_message(msg.chat.id,
                                                           f"{mention}, вы купили бизнес за {money_form(for_bisnes[L1[2]]['cost'])}")
                                else:
                                    await bot.send_message(msg.chat.id,
                                                           f"{mention}, у вас не хватило средств на покупки бизнеса")
                elif len(L1) >= 2:
                    if L1[1] in ["Налог", "налог"]:
                        if kkk not in bisnes.keys():
                            await bot.send_message(msg.chat.id, f"{mention}, у вас нету бизнеса(")
                        else:
                            num = bisnes[kkk]['number']
                            txt = bisnes_go(msg, num)
                            bs = bisnes[kkk]['nalog']
                            if bs == 0:
                                await bot.send_message(msg.chat.id, f"{mention}, вам ещё не требуется оплатить налог!")
                            else:
                                if bs <= People[kkk]['balance']:
                                    bisnes[kkk]['nalog'] = 0
                                    People[kkk]['balance'] -= bs
                                    print(bisnes[kkk]['nalog'])
                                    save()
                                    save3()
                                    await bot.send_message(msg.chat.id, "вы оплатили налог!")
                                else:
                                    await bot.send_message(msg.chat.id, f"{mention}, у вас недостаточно средств!")
                    if L1[1] in ["Снять", "снять"]:
                        if kkk not in bisnes.keys():
                            await bot.send_message(msg.chat.id, f"{mention}, у вас нету бизнеса(")
                        else:
                            num = bisnes[kkk]['number']
                            txt = bisnes_go(msg, num)
                            bs = bisnes[kkk]['balance']
                            if bs == 0:
                                await bot.send_message(msg.chat.id, "У вас нету денег на счету ")
                            elif bs > 0:
                                People[kkk]['balance'] += bs
                                bisnes[kkk]['balance'] = 0
                                save()
                                save3()
                                await bot.send_message(msg.chat.id, f"{mention}, вы успешно сняли с бизнеса {money_form(bs)}")

                else:
                    if kkk not in bisnes.keys():
                        await bot.send_message(msg.chat.id, f"{mention}, у вас нету бизнеса(")
                    else:
                        num = bisnes[kkk]['number']
                        txt = bisnes_go(msg, num)
                        kb = InlineKeyboardMarkup()
                        b_up = InlineKeyboardButton("🚀Улучшить", callback_data=f"upgradeB_{num}:{msg.from_user.id}")
                        kb.add(b_up)
                        await bot.send_photo(msg.chat.id, open("assets/pngtree-hand-gesture-business-office-technology-internet-map-business-technology-gesture-image_791811.jpg", "rb"), txt, reply_markup=kb)

            if msg.text in ["Мороженое","мороженое"]:
                await bot.send_message(msg.chat.id, f"{mention}, Стоимость мороженого оцениваеться в 1.000.000.000ё\n\nпродать мороженое - продать мороженое [кол]")

            if msg.text in ["фиткоин", "Фиткоин"]:
                control = 1
                st_txt = ""
                if People[kkk]['state_prem']['true'] == 1:
                    status = People[kkk]['state_prem']['name']
                    st_txt = f"<b>[{status}]</b>"
                txt_bitcoin = f"{st_txt}{mention}, вот цена фиткоина на данный момент \n" \
                              f"\n" \
                              f"  ⌈💳цена: {money_form(bit_cost)}💰⌋" \
                              f"   \n\n" \
                              "купить фиткоин - купить фиткоин {kol}\n" \
                              "продать фиткоин - продать фиткоин {kol}"
                await bot.send_photo(msg.chat.id, open("assets/bit_foto.jpg", "rb"), caption=txt_bitcoin)

            if msg.text in ["харикоин", "Харикоин"]:
                control = 1
                st_txt = ""
                if People[kkk]['state_prem']['true'] == 1:
                    status = People[kkk]['state_prem']['name']
                    st_txt = f"<b>[{status}]</b>"
                txt_bitcoin = f"{st_txt}{mention}, вот цена харикоина на данный момент \n" \
                              f"\n" \
                              f"  ⌈💳цена: {money_form(hur_cost)}💰⌋" \
                              f"   \n\n" \
                              "купить харикоин - купить харикоин {kol}\n" \
                              "продать харикоин - продать харикоин {kol}"
                await bot.send_photo(msg.chat.id, open("assets/a-stack-of-five-rows-of-coins.jpg", "rb"), caption=txt_bitcoin)

            if L1[0] in ["купить", "Купить"]:
                control = 1
                if len(L1) >= 3:
                    if L1[1] in ["Харикоин","харикоин"]:
                        try:
                            kol = int(L1[2])
                            if kol * hur_cost > People[kkk]['balance'] or kol < 0:
                                await bot.send_message(msg.chat.id, f"У вас недостаточно средств для покупки {kol}харикоинов")
                            else:
                                st_txt = ""
                                if People[kkk]['state_prem']['true'] == 1:
                                    status = People[kkk]['state_prem']['name']
                                    st_txt = f"<b>[{status}]</b>"
                                People[kkk]['balance'] -= int(kol * hur_cost)
                                People[kkk]['harry'] += kol
                                save()

                                await bot.send_message(msg.chat.id, f"{st_txt}{mention}, вы купили {kol} харикоинов")
                        except:
                            pass

                    if L1[1] in ["фиткоин", "Фиткоин"]:
                        try:
                            kol = int(L1[2])
                            if kol * bit_cost > People[kkk]['balance'] or kol < 0:
                                await bot.send_message(msg.chat.id, f"У вас недостаточно средств для покупки {kol}фиткоинов")
                            else:
                                st_txt = ""
                                status = ""
                                if People[kkk]['state_prem']['true'] == 1:
                                    status = People[kkk]['state_prem']['name']
                                    st_txt = f"<b>[{status}]</b>"

                                if status == "Флэш":
                                    limit = 1000000000000000
                                else:
                                    limit = 1000000000000

                                if People[kkk]['admin'] >= 4:
                                    limit = 10000000000000000

                                if limit < People[kkk]['bitcoin'] + kol:
                                    await bot.send_message(msg.chat.id, f"{mention}, лимит фиткоинов закончился, {money_form(People[kkk]['bitcoin'])}/{money_form(limit)}")
                                else:
                                    People[kkk]['balance'] -= kol * bit_cost
                                    People[kkk]['bitcoin'] += kol
                                    save()
                                    st_txt = ""
                                    if People[kkk]['state_prem']['true'] == 1:
                                        status = People[kkk]['state_prem']['name']
                                        st_txt = f"<b>[{status}]</b>"
                                    await bot.send_message(msg.chat.id, f"{st_txt}{mention}, вы купили {kol} фиткоинов")
                        except:
                            await bot.send_message(msg.chat.id, "что? подсказка: \nкупить фиткоин {количество}")

            if L1[0] in ["продать", "Продать"]:
                if len(L1) >= 3:
                    if L1[1] in ["Харикоин","харикоин"]:
                        try:
                            kol = int(L1[2])
                            if kol > People[kkk]['harry'] or kol < 0:
                                await bot.send_message(msg.chat.id, f"У вас недостаточно средст для продажи {kol} харикоинов")
                            else:
                                People[kkk]['balance'] += kol * hur_cost
                                People[kkk]['harry'] -= kol
                                save()
                                await bot.send_message(msg.chat.id, f"{mention}, вы продали {kol} харикоинов")
                        except:
                            await bot.send_message(msg.chat.id, "что? подсказка: \nпродать харикоин {количество}")

                    if L1[1] in ["фиткоин", "Фиткоин"]:
                        try:
                            kol = int(L1[2])
                            if kol > People[kkk]['bitcoin'] or kol < 0:
                                await bot.send_message(msg.chat.id, f"У вас недостаточно средст для продажи {kol} фиткоинов")
                            else:
                                People[kkk]['balance'] += kol * bit_cost
                                People[kkk]['bitcoin'] -= kol
                                save()
                                await bot.send_message(msg.chat.id, f"{mention}, вы продали {kol} фиткоинов")
                        except:
                            await bot.send_message(msg.chat.id, "что? подсказка: \nпродать фиткоин {количество}")
                    if L1[1] in ["Мороженое","мороженое"]:
                        try:
                            kol = int(L1[2])
                            if "icecream" not in People[kkk].keys():
                                await bot.send_message(msg.chat.id, "У вас нет мороженого")
                            else:
                                if kol > People[kkk]['icecream'] or kol < 0:
                                    await bot.send_message(msg.chat.id, f"У вас недостаточно мороженого")
                                else:
                                    People[kkk]['balance'] += kol * 1000000000
                                    People[kkk]['icecream'] -= kol
                                    save()
                                    await bot.send_message(msg.chat.id, f"{mention}, вы продали {kol} Мороженого")
                        except:
                            await bot.send_message(msg.chat.id, "что? подсказка: \nпродать мороженое {количество}")

            if msg.text in ["топ", "Топ"]:
                control = 1
                txt = top_do1(kkk, People, msg.chat.id, "balance")
                st_txt = ""
                if People[kkk]['state_prem']['true'] == 1:
                    status = People[kkk]['state_prem']['name']
                    st_txt = f"<b>[{status}]</b>"
                txt_ke = f"{st_txt} {mention},"
                name_3 = await bot.send_message(msg.chat.id, "Получаю данные с сервера")
                kebord = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("урон", callback_data=f"top1_{msg.message_id}:{msg.from_user.id}:{msg.chat.id}")
                b2 = InlineKeyboardButton("fitcoin", callback_data=f"top2_{msg.message_id}:{msg.from_user.id}:{msg.chat.id}")
                b3 = InlineKeyboardButton("промо", callback_data=f"top3_{msg.message_id}:{msg.from_user.id}:{msg.chat.id}")
                b4 = InlineKeyboardButton("haricoin", callback_data=f"top4_{msg.message_id}:{msg.from_user.id}:{msg.chat.id}")
                b5 = InlineKeyboardButton("icecream", callback_data=f"top5_{msg.message_id}:{msg.from_user.id}:{msg.chat.id}")

                b_END= InlineKeyboardButton("💰Воровать", callback_data=f"RobbyGo")
                kebord.add(b1, b2, b3, b4, b5)
                kebord.add(b_END)
                await bot.edit_message_text(txt_ke+txt, msg.chat.id, name_3.message_id, reply_markup=kebord)

            if msg.text in ['б', 'Б', 'баланс', 'Баланс']:
                kb_balance = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("Канал", url=f"{chanel}")
                b2 = InlineKeyboardButton("Бонус", callback_data="bonus")
                kb_balance.add(b1,b2)
                control = 1
                name_4 = await bot.send_message(msg.chat.id, "получаю информацию с сервера...")
                st_txt = ""
                if People[kkk]['state_prem']['true'] == 1:
                    status = People[kkk]['state_prem']['name']
                    st_txt = f"<b>[{status}]</b>"
                if msg.reply_to_message:
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    text_bank = ""
                    if People[kkk2]['balance'] > 0:
                        text_bank += f"  💸Счёт ⧽ {money_form(People[kkk2]['balance'])}\n"
                    if People[kkk2]['bitcoin'] > 0:
                        text_bank += f"  💳fitcoin ⧽ {money_form(People[kkk2]['bitcoin'])}\n"
                    if People[kkk2]['harry'] > 0:
                        text_bank += f"  💳Harycoin ⧽ {money_form(People[kkk2]['harry'])}\n"

                    if "icecream" in People[kkk2].keys():
                        if People[kkk2]['icecream'] > 0:
                            text_bank += f"  🍧Icecream ⧽ {money_form(People[kkk2]['icecream'])}\n"
                    if text_bank == "":
                        text_bank = "Пусто.\n"
                    mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                    txt = f"{st_txt}{mention}, баланс игрока {mention2}:\n\n" \
                          f"🏦Банк:\n" \
                          f"{text_bank}" \
                          f"\n" \
                          f"❓Icecream - Специальная валюта /icecream"
                    pute = "assets/money.jpg"
                else:
                    text_bank = ""
                    if People[kkk]['balance'] > 0:
                        text_bank += f"  💸Счёт ⧽ {money_form(People[kkk]['balance'])}\n"
                    if People[kkk]['bitcoin'] > 0:
                        text_bank += f"  💳fitcoin ⧽ {money_form(People[kkk]['bitcoin'])}\n"
                    if People[kkk]['harry'] > 0:
                        text_bank += f"  💳Harycoin ⧽ {money_form(People[kkk]['harry'])}\n"

                    if "icecream" in People[kkk].keys():
                        if People[kkk]['icecream'] > 0:
                            text_bank += f"  🍧Icecream ⧽ {money_form(People[kkk]['icecream'])}\n"
                    if text_bank == "":
                        text_bank = "Пусто.\n"

                    txt = f"{st_txt}{mention} ваш баланс:\n\n" \
                          f"🏦Банк:\n" \
                          f"{text_bank}" \
                          f"\n" \
                          f"❓Icecream - Специальная валюта /icecream"

                    pute = "assets/money.jpg"


                await bot.send_photo(msg.chat.id,
                                     open(pute, "rb"),
                                     caption=txt, reply_markup=kb_balance)
                await bot.delete_message(msg.chat.id, name_4.message_id)


            if msg.text == "промокод" or msg.text == "Промокод" and len(L1) == 1:
                control = 1
                await bot.send_message(msg.chat.id,
                                       "Вот формула по создания промокода: создать промо {имя} {количество} {приз}")

            if msg.text in ["реф","Реф"]:
                control = 1
                txt = f"{mention}, пригласи 20 человек, и получи флэш статус! \n" \
                      f"твоя реф- https://t.me/True_gb_bot?start={kkk} \n"

                await bot.send_message(msg.chat.id, txt)

            if msg.text in ["Ивент","ивент"]:
                t_1 = ""
                if IVENT_SET:
                    t_1 = f"На данный момент идёт ивент!"

                await bot.send_message(msg.chat.id, t_1 + f"\n\nВаш баланс: {Ivent[kkk]['money']} Монеток")

            if L1[0] in ["создать", "Создать"]:
                control = 1
                if len(L1) >= 5:
                    if L1[1] in ["промо", "Промо"]:
                        name = L1[2]
                        kol = L1[3]
                        price = L1[4]

                        if name in promo.keys():
                            await bot.send_message(msg.chat.id, "увы, но такое имя уже есть")
                        else:
                            if int(kol) * int(price) > People[kkk]["balance"]:
                                await bot.send_message(msg.chat.id, "у вас недостаточно средств для создания промокода")
                            else:
                                if int(kol) * int(price) <= 0:
                                    await bot.send_message(msg.chat.id, "Так запрещено!")
                                else:
                                    await bot.send_sticker(msg.chat.id, sticker="CAACAgIAAxkBAAJEG2UUgnqREpyAdqFLKelxlyktH1UcAAKCNAACQTfpSnf4wrGkjKACMAQ")
                                    txt_promo = f"{mention}, вы создали промокод '{name}': \n\n" \
                                                f"👤активаций: {kol}\n" \
                                                f"💰приз: {price}\n" \
                                                f"\n" \
                                                f"🪄общая сумма: {int(kol) * int(price)}\n"
                                    await bot.send_message(msg.chat.id, txt_promo)
                                    promo[name] = {"kol": int(kol), "price": int(price), "users": []}
                                    save2()
                                    People[kkk]['balance'] -= int(kol) * int(price)
                                    People[kkk]['promo'] += int(kol) * int(price)
                                    save()

            if L1[0] in ["промо", "Промо", "Промокод", "промокод"]:
                control = 1
                if len(L1) >= 2:
                    name = L1[1]
                    if name in promo.keys():
                        if promo[name]['kol'] <= 0:
                            await bot.send_message(msg.chat.id, "Промокод закончился")
                        else:
                            if kkk in promo[name]['users']:
                                await bot.send_message(msg.chat.id, "вы уже активировали данный промокод")
                            else:
                                user_channel_status = await bot.get_chat_member(chat_id=-1001842985432,
                                                                                user_id=msg.from_user.id)
                                if user_channel_status["status"] != 'left':
                                    st_txt = ""
                                    if People[kkk]['state_prem']['true'] == 1:
                                        status = People[kkk]['state_prem']['name']
                                        st_txt = f"<b>[{status}]</b>"
                                    promo[name]['kol'] -= 1
                                    promo[name]['users'].append(kkk)
                                    People[kkk]['balance'] += promo[name]['price']
                                    save()
                                    save2()
                                    await bot.send_message(msg.chat.id, f"{st_txt} {mention}Вы активировали промокод +{promo[name]['price']}")
                                else:
                                    bt = InlineKeyboardMarkup()
                                    b1 = InlineKeyboardButton("канал", url="https://t.me/GbBotBoarBot")
                                    bt.add(b1)

                                    await bot.send_message(msg.chat.id,
                                                           "Вам нужно подписаться на основной канал, чтобы использовать промокоды!",
                                                           reply_markup=bt)
                    else:
                        await bot.send_message(msg.chat.id, "такого промокода нету")


            if msg.text in ["Проф", "проф", "Профиль", "профиль"]:
                control = 1
                if People[kkk]['admin'] == 5:
                    adm = "Владелец"
                if People[kkk]['admin'] == 4:
                    adm = "старший админ"
                if People[kkk]['admin'] == 3:
                    adm = "младший админ"
                if People[kkk]['admin'] == 2:
                    adm = "старший модератор"
                if People[kkk]['admin'] == 1:
                    adm = "младший модератор"
                if People[kkk]['admin'] == 0:
                    adm = "нету"

                if People[kkk]['state_prem']['information'] != str(datetime.now().date()):
                    People[kkk]['state_prem']['limit'] = 0
                    People[kkk]['state_prem']['information'] = str(datetime.now().date())
                    save()

                st_txt = ""
                status = ""
                if People[kkk]['state_prem']['true'] == 1:
                    status = People[kkk]['state_prem']['name']
                    st_txt = f"<b>[{status}]</b>"

                if status == "":
                    status = "нету"

                inf_txt = ""
                limit = 0
                if status == "Флэш":
                    inf_txt = f"   date: {People[kkk]['state_prem']['information']} \n" \
                              f"   Выдал денег: {money_form(People[kkk]['state_prem']['limit'])}/{money_form(flash_limit)}\n"
                    limit = 1000000000000000
                else:
                    limit = 1000000000000

                if People[kkk]['admin'] >= 4:
                    limit = 10000000000000000

                place = ""
                if People[kkk]['place'] == 1:
                    place = f"Спавн"
                elif People[kkk]['place'] == 2:
                    place = f"Город хрюва"
                elif People[kkk]['place'] == 3:
                    place = f"Шахта"
                elif People[kkk]['place'] == 4:
                    place = f"город блэкарей"
                elif People[kkk]['place'] == 5:
                    place = f"манки тавн"
                elif People[kkk]['place'] == 6:
                    place = f"город гномиков"
                money = money_form(People[kkk]['balance'])
                bitco = money_form(People[kkk]['bitcoin'])

                if "energy" not in People[kkk].keys():
                    ENRG = 0
                else:
                    ENRG = People[kkk]['energy']['kol']

                txt = f"{st_txt}{mention}, вот ваш профиль\n\n" \
                      f"🚀 адм ⧽ {adm} \n" \
                      f"⚜ статус ⧽ {status}\n" \
                      f"🆔 Telegram ID ⧽ {msg.from_user.id} \n" \
                      f"🆔 Игровой ID ⧽ {People[kkk]['game_id']} \n" \
                      f"✨ Опыт ⧽ {money_form2(People[kkk]['skil'])} \n" \
                      f"❤️‍🔥️ Энергии ⧽ {ENRG} \n\n" \
                      f"👻 Никнейм в боте ⧽ {People[kkk]['name']} \n" \
                      f"🍀 промокоды ⧽ {money_form(People[kkk]['promo'])}👾\n" \
                      f"🌉 Место нахождения ⧽ {place}\n" \
                      f"🏦 Баланс ⧽ {money}👾\n" \
                      f"💳 фиткоинов ⧽ {bitco}/{money_form(limit)}\n" \
                      f"💳 харикоинов ⧽ {money_form(People[kkk]['harry'])}\n" \
                      f"\n" \
                      f"регестрация ⧽ {People[kkk]['date'].split('.')[0]}"

                await bot.send_photo(msg.chat.id, open("assets/NY1.jpeg", "rb"), caption=txt)



            if msg.text in ["места", "Места"]:
                control = 1
                c_name1 = ""
                c_name2 = ""
                c_name3 = ""
                c_name4 = ""
                c_name5 = ""
                c_name6 = ""
                if People[kkk]['place'] == 1:
                    c_name1 = f"🟢"
                elif People[kkk]['place'] == 2:
                    c_name2 = f"🟢"
                elif People[kkk]['place'] == 3:
                    c_name3 = f"🟢"
                elif People[kkk]['place'] == 4:
                    c_name4 = f"🟢"
                elif People[kkk]['place'] == 5:
                    c_name5 = f"🟢"
                elif People[kkk]['place'] == 6:
                    c_name6 = f"🟢"

                bt = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton(f"{c_name1}спавн(100000👾)", callback_data=f"ride_100000:1:{kkk}")
                b2 = InlineKeyboardButton(f"{c_name2}город хрюва(1000000👾)", callback_data=f"ride_1000000:2:{kkk}")
                b3 = InlineKeyboardButton(f"{c_name3}шахта(1500000👾)", callback_data=f"ride_1500000:3:{kkk}")
                b4 = InlineKeyboardButton(f"{c_name4}город блэкарей(1400000👾)", callback_data=f"ride_1400000:4:{kkk}")
                b5 = InlineKeyboardButton(f"{c_name5}маки тавн(1500000👾)", callback_data=f"ride_2000000:5:{kkk}")
                b6 = InlineKeyboardButton(f"{c_name6}город гномиков(1500000👾)", callback_data=f"ride_2000000:6:{kkk}")
                bt.add(b1)
                bt.add(b2)
                bt.add(b3)
                bt.add(b4)
                bt.add(b5)
                bt.add(b6)
                await bot.send_photo(msg.chat.id, open("assets/3d-render-sunrise-view-from-space-on-planet-earth_130291-1.jpeg", "rb"), reply_markup=bt)

            if msg.text in ["Шахта","шахта"]:
                if "energy" not in People[kkk].keys():
                    People[kkk]['energy'] = {"kol":15, "date": str(msg.date)}

                date_last_farm = datetime.strptime(str(People[kkk]["energy"]['date']), "%Y-%m-%d %H:%M:%S")
                date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                tm = date2 - date_last_farm
                tm2 = int(tm.total_seconds())

                kol_arl = tm2 // 600
                for i in range(kol_arl):
                    People[kkk]['energy']['kol'] += 1
                    People[kkk]['energy']['date'] = str(msg.date)
                    if i >= 20:
                        break

                if People[kkk]['energy']['kol'] > 15:
                    People[kkk]['energy']['kol'] = 15

                if People[kkk]['energy']['kol'] <= 0:
                    txt_shahta = "У вас закончилась энергия"
                elif People[kkk]['energy']['kol'] > 0:
                    txt_shahta = "1 железо"
                    if 'silver' not in People[kkk].keys():
                        People[kkk]['silver'] = 0
                    People[kkk]['silver'] += 1
                    People[kkk]['energy']['kol'] -= 1
                    People[kkk]['skil'] += 1

                await bot.send_photo(msg.chat.id, open("assets/under-the-ground-beautiful-view-of-stalactites-and-stalagmites-in-an-underground-cavern-new-athos-cave-sacred-ancient-underworld-formations.jpg", "rb"), caption=f"⛏{mention}, Вы побывали в шахте \n\n⬛️{txt_shahta} \n\n⚡️ Энергия: {People[kkk]['energy']['kol']} | 💡 Опыт: {money_form2(People[kkk]['skil'])}")
                save()

            if msg.text in ["Ресурсы","ресурсы"]:
                txt = f"{mention}, Ресурсы доступные в боте: \n\n" \
                      f"железо - 100.000 | {People[kkk]['silver']}\n" \
                      f"\n" \
                      f"продать ресурс - продать (железо) количество"

                await bot.send_message(msg.chat.id, txt)

            if L1[0] in ["Продать", "продать"]:
                if len(L1) >= 3:
                    if L1[1] in ["Железо","железо"]:
                        try:
                            kol = int(L1[2])
                            try:
                                kol_iron = People[kkk]['silver']
                            except:
                                kol_iron = 0

                            if kol_iron <= 0 or kol < 1:
                                await bot.send_message(msg.chat.id, "У вас нет железа")
                            elif kol_iron > 0:
                                if kol_iron > kol:
                                    People[kkk]['silver'] -= kol
                                    People[kkk]['balance'] += (100000 * kol)
                                    save()
                                    await bot.send_message(msg.chat.id, f"{mention}, Вы успешно обменяли {kol} железа на {100000 * kol}")
                                else:
                                    await bot.send_message(msg.chat.id, "Не достаточно железа")
                        except:
                            await bot.send_message(msg.chat.id, "Ведите число!")

            if msg.text == "копать" or msg.text == "Копать":
                control = 1
                if People[kkk]['place'] != 3:
                    await bot.send_message(msg.chat.id, "копать можно только в шахте! а тут можно и на штраф( \n\nместа -> кнопка(шахта)")
                elif People[kkk]['place'] == 3:
                    if People[kkk]['time_farm1'] == "" or People[kkk]['time_farm1'] == "tm":
                        People[kkk]['time_farm1'] = datetime.now().day
                        rand2 = random.randint(1000000000, 2000000000)
                        rand = money_form(rand2)
                        await bot.send_message(msg.chat.id, f"⸕вы выкопали кучу алмазов и продали их за {rand}👾")
                        People[kkk]['balance'] += rand2
                        save()
                    else:
                        if People[kkk]['time_farm1'] != datetime.now().day:
                            rand2 = random.randint(1000000000, 2000000000)
                            if "premium" in People[kkk].keys():
                                if People[kkk]['premium']['pr'] == "1":
                                    procent = int((rand2 / 100)) + rand2
                                    print(procent)
                                    t1 = "+5% по Silver Vip"
                                elif People[kkk]['premium']['pr'] == "2":
                                    procent = int((rand2 * 0.1)) + rand2
                                    t1 = "+10% по Gold Vip"
                                elif People[kkk]['premium']['pr'] == "3":
                                    procent = int((rand2 * 0.15)) + rand2
                                    t1 = "+15% по Platinum Vip"
                                else:
                                    procent = rand2
                                    t1 = ""
                            else:
                                procent = rand2
                                t1 = ""

                            rand = money_form(procent)

                            await bot.send_message(msg.chat.id, f"⸕вы выкопали кучу алмазов и продали их за {rand}👾 \n💥опыт увеличен на 1 \n{t1}")
                            People[kkk]['time_farm1'] = datetime.now().day
                            People[kkk]['balance'] += procent
                            People[kkk]['skil'] += 1
                            save()

                            if IVENT_SET:
                                chek_ivent(msg)
                                await bot.send_message(msg.chat.id, f"{mention}, Вот ваши ивентовые монетки! +15 \nВаш баланс монеток: {Ivent[kkk]['money'] + 15}")
                                Ivent[kkk]['money'] += 15
                                save_ivent()
                        else:
                            await bot.send_message(msg.chat.id, f"вы сегодня уже копали")

            if msg.text in ["работать", "Работать"]:
                control = 1
                if People[kkk]['time_farm2'] == "" or People[kkk]['time_farm2'] == "tm":
                    monee = random.randint(450000000, 550000000)
                    mon2 = money_form(monee)
                    await bot.send_message(msg.chat.id, f"{mention}, вы заработали {mon2}👾")
                    print(mon2)
                    People[kkk]["balance"] += monee
                    People[kkk]['time_farm2'] = str(msg.date)
                    save()
                else:
                    date_last_farm = datetime.strptime(str(People[kkk]["time_farm2"]), "%Y-%m-%d %H:%M:%S")
                    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                    tm = date2 - date_last_farm
                    tm2 = int(tm.total_seconds() // 60)
                    if tm2 * 60 >= 7200:
                        monee = random.randint(450000000, 550000000)
                        if "premium" in People[kkk].keys():
                            if People[kkk]['premium']['pr'] == "1":
                                procent = int((monee / 100)) + monee
                                print(procent)
                                t1 = "+5% по Silver Vip"
                            elif People[kkk]['premium']['pr'] == "2":
                                procent = int((monee * 0.1)) + monee
                                t1 = "+10% по Gold Vip"
                            elif People[kkk]['premium']['pr'] == "3":
                                procent = int((monee * 0.15)) + monee
                                t1 = "+15% по Platinum Vip"
                            else:
                                procent = monee
                                t1 = ""
                        else:
                            procent = monee
                            t1 = ""

                        mon2 = money_form(procent)
                        await bot.send_message(msg.chat.id, f"{mention}, вы заработали {mon2}👾 \n{t1}")

                        People[kkk]["balance"] += procent
                        People[kkk]['time_farm2'] = str(msg.date)
                        save()

                        if IVENT_SET:
                            chek_ivent(msg)
                            await bot.send_message(msg.chat.id, f"{mention}, Вот ваши ивентовые монетки! +15 \nВаш баланс монеток: {Ivent[kkk]['money'] + 15}")
                            Ivent[kkk]['money'] += 15
                            save_ivent()
                    else:
                        await bot.send_message(msg.chat.id, f"{mention}, работать можно только раз в 2 часа!")

            if msg.text in ["найти клад", "Найти клад"]:
                control = 1
                if People[kkk]['time_farm2'] == "" or People[kkk]['invetner'] == "1":
                    mon = random.randint(500000000, 650000000)
                    mon2 = money_form(mon)
                    await bot.send_message(msg.chat.id, f"{mention}, вы заработали {mon2}👾")
                    People[kkk]["balance"] += mon
                    People[kkk]['invetner'] = str(msg.date)
                    save()
                else:
                    date_last_farm = datetime.strptime(str(People[kkk]["invetner"]), "%Y-%m-%d %H:%M:%S")
                    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                    tm = date2 - date_last_farm
                    tm2 = int(tm.total_seconds())
                    if tm2 >= 10800:
                        rand2 = random.randint(500000000, 650000000)
                        if "premium" in People[kkk].keys():
                            if People[kkk]['premium']['pr'] == "1":
                                procent = int((rand2 * 0.05)) + rand2
                                print(procent)
                                t1 = "+5% по Silver Vip"
                            elif People[kkk]['premium']['pr'] == "2":
                                procent = int((rand2 * 0.1)) + rand2
                                t1 = "+10% по Gold Vip"
                            elif People[kkk]['premium']['pr'] == "3":
                                procent = int((rand2 * 0.15)) + rand2
                                t1 = "+15% по Platinum Vip"
                            else:
                                procent = rand2
                                t1 = ""
                        else:
                            procent = rand2
                            t1 = ""

                        rand = money_form(procent)

                        await bot.send_message(msg.chat.id, f"{mention}, вы нашли клад на сумму {rand}👾")
                        People[kkk]["balance"] += procent
                        People[kkk]['invetner'] = str(msg.date)
                        save()

                        if IVENT_SET:
                            chek_ivent(msg)
                            await bot.send_message(msg.chat.id, f"{mention}, Вот ваши ивентовые монетки! +15 \nВаш баланс монеток: {Ivent[kkk]['money'] + 15}")
                            Ivent[kkk]['money'] += 15
                            save_ivent()
                    else:
                        await bot.send_message(msg.chat.id,
                                               f"{mention}, искать клад можно раз в 3часа! \nпрошло: {tm2}/10800сек")

            if msg.text in ["босс", "Босс"]:
                control = 1
                tp2 = str(People[kkk]['place'])
                low = boses[tp2]
                if low['type'] == 1:
                    file = open("assets/boss1.png", "rb")
                    price = 1000000000
                    txt1 = "свинтус придёт"
                if low['type'] == 2:
                    file = open("assets/boss2.png", "rb")
                    price = 1500000000
                    txt1 = "агри дед мороз"

                txt_boss = f"{txt1}: \n" \
                           f"hp: {low['hp']}\n" \
                           f"награда: {price}👾\n" \
                           f"\n" \
                           f"чобы атаковать боса: босс атака\n"
                await bot.send_photo(msg.chat.id, file, caption=txt_boss)

            if msg.text in ["Воровать","воровать"]:
                txt = f"Топ 10 человек, Вы можете воровать только 1 раз в 2 часа! \n\nКанал - {chanel_us}"
                OBJ = top_robby(kkk, People)
                kb = InlineKeyboardMarkup()
                for i, y in OBJ.items():
                    b1 = InlineKeyboardButton(f"{People[i]['name']} -- {money_form(y)}", callback_data=f"rob_{datetime.now().day}:{i}")
                    kb.add(b1)

                await bot.send_message(msg.chat.id, txt, reply_markup=kb)

            if msg.text in ["босс атака", "Босс атака"]:
                if kkk not in lst_boss_ataced.keys():
                    lst_boss_ataced[kkk] = str(msg.date)
                    tm2 = 10
                else:
                    date_last_farm = datetime.strptime(str(lst_boss_ataced[kkk]), "%Y-%m-%d %H:%M:%S")
                    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                    tm = date2 - date_last_farm
                    tm2 = int(tm.total_seconds())

                if tm2 >= 3:
                    control = 1
                    tp1 = str(People[kkk]['place'])
                    val = boses[tp1]
                    uron = random.randint(3, 40)
                    users_permission = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,}
                    if "1" in People[kkk].keys():
                        users_permission['1'] = People[kkk]["1"]
                    if "2" in People[kkk].keys():
                        users_permission["2"] = People[kkk]["2"]
                    if "3" in People[kkk].keys():
                        users_permission["3"] = People[kkk]["3"]
                    if "4" in People[kkk].keys():
                        users_permission["4"] = People[kkk]["4"]
                    if "5" in People[kkk].keys():
                        users_permission["5"] = People[kkk]["5"]
                    if "6" in People[kkk].keys():
                        users_permission["6"] = People[kkk]["6"]
                    if "7" in People[kkk].keys():
                        users_permission["7"] = People[kkk]["7"]
                    if "8" in People[kkk].keys():
                        users_permission["8"] = People[kkk]["8"]


                    user_channel_status = await bot.get_chat_member(chat_id=f'{chat_id}', user_id=msg.from_user.id)
                    if user_channel_status["status"] != 'left':
                        mn = 1.5
                    else:
                        mn = 1
                    if mn == 1.5:
                        u = uron // 2
                        uron += u
                    txt_boss_err = ""
                    txt_boost = ""
                    for key, value in users_permission.items():
                        if value > 0:
                            uron_height = random.choice(books[key]['boost'])
                            uron += uron_height
                            q = random.choice([1,1,1,1,2])
                            txt_boost = f"\nДополнитльный урон! {books[key]['name']} -- {uron_height}"
                            if q == 2:
                                txt_boss_err = f"\n💥У вас сломалась вещь '{books[key]['name']}' -- 1"
                                People[kkk][key] -= 1
                                save()


                    val['hp'] -= uron
                    People[kkk]['boss_hp'] += uron
                    if val['hp'] <= 0:
                        if val['type'] == 1:
                            price = 1000000000
                        if val['type'] == 2:
                            price = 1500000000

                        await bot.send_message(msg.chat.id, f"{mention}, Вы одалели боса. Ваша награда: 1. {money_form(price)}👾")
                        People[kkk]['balance'] += price
                        bos = random.choice([1, 1, 1, 1, 1, 2, 2])
                        if bos == 1:
                            val['hp'] = 2500
                            val['type'] = 1
                        if bos >= 2:
                            val['hp'] = 5500
                            val['type'] = 2

                        boses[tp1] = val
                    else:
                        rand = random.randint(1, 10)
                        price = 'нету'
                        if rand >= 6:
                            rand2 = random.randint(500, 2300)
                            price = f"+{rand2} к балансу"
                            People[kkk]['balance'] += rand2
                            save()
                        if val['type'] == 1:
                            file = open("assets/boss1.png", "rb")
                        if val['type'] == 2:
                            file = open("assets/boss2.png", "rb")
                        await bot.send_photo(msg.chat.id, file,
                                             caption=f"{mention}, вы нанесли {uron} урона босу. \nваша награда за удар: {price}{txt_boost}{txt_boss_err} \n\n🎁ваш множитель: {mn}x\n🚀войдите в чат 'Boar chat', чтобы увеличть множитель")

                    boses[tp1] = val
                    lst_boss_ataced[kkk] = str(msg.date)
                    save()
                else:
                    await bot.send_message(msg.chat.id, "У вас не востановились силы! до востановления чуть меньше 3-ёх секунд")

            if L1[0] in ["дать", "Дать"]:
                control = 1
                if len(L1) >= 2 and msg.reply_to_message:
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    kol = int(L1[1])
                    if kol <= 100:
                        await bot.send_message(msg.chat.id, f"{mention}, нельзя перевести меньше чем 100!")
                    else:
                        if People[kkk]['balance'] >= kol:
                            People[kkk2]['balance'] += kol
                            People[kkk]['balance'] -= kol
                            save()
                            mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                            txt = f"{mention2}, вам перевели {kol}👾 от {mention}"
                            await bot.send_photo(msg.chat.id, open("assets/perve_foto.jpg", "rb"), caption=txt)
                        else:
                            await bot.send_message(msg.chat.id, f"{mention}, у вас нету {kol}👾")
            
            if msg.text in ["Лабаратория","лабаратория", "Лаба", "лаба"]:
                if kkk not in Laba.keys():
                    Laba[kkk] = {"lvl":0, "name":"Лек", "matrl":0, "el":100, "prizon":0, "kol":0}
                    save_laba()

                kb = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("⚡️Электричество", callback_data=f"BayEL_{kkk}")
                b2 = InlineKeyboardButton("⚗Материалы", callback_data=f"BayMATR_{kkk}")
                b3 = InlineKeyboardButton("💥Подозревания", callback_data=f"BayPRIZN_{kkk}")
                kb.add(b1)
                kb.add(b2)
                kb.add(b3)

                txt = f"{mention}, Лабаратория ур. {Laba[kkk]['lvl']}\n" \
                      f"\n" \
                      f"⚡️электричество ⧽ {Laba[kkk]['el']}/100\n" \
                      f"⚗Материалы ⧽ {Laba[kkk]['matrl']}/100\n" \
                      f"💥подозревания ⧽ {Laba[kkk]['prizon']}\n" \
                      f"✨стоимость продаж ⧽ 1кк ~ 20кк\n" \
                      f"\n" \
                      f"⛓Изготовляем ⧽ {Laba[kkk]['name']}\n" \
                      f"💎Количество продукта ⧽ {Laba[kkk]['kol']}\n" \
                      f"\n" \
                      f"❗️владелец не несёт ответственность за название вашего игрового продукта ⧽ /LabaHelp \n" \
                      f"Команда производства -- производить"

                await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-27 20.12.04.jpeg", "rb"),  caption=txt, reply_markup=kb)

            if msg.text in ["Производить","производить"]:
                if "time" not in Laba[kkk].keys():
                    Laba[kkk]['time'] = str(msg.date)
                    Laba[kkk]['kol'] += 10
                    save_laba()
                    await bot.send_message(msg.chat.id, f"{mention}, Вы произвели 10 {Laba[kkk]['name']}")
                else:
                    date_last_farm = datetime.strptime(str(Laba[kkk]['time']), "%Y-%m-%d %H:%M:%S")
                    date2 = datetime.strptime(str(msg.date), "%Y-%m-%d %H:%M:%S")
                    tm = date2 - date_last_farm
                    tm2 = int(tm.total_seconds())
                    kol = tm2 // 1800
                    if kol == 0:
                        await bot.send_message(msg.chat.id, f"{mention}, Вы ещё ничего не произвели! Подождите немного")
                    else:
                        if kol > 23:
                            kol = 23

                        await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Рад тебя видеть! Лабаратория произвела {kol} продукта!")
                        Laba[kkk]['kol'] += kol
                        Laba[kkk]['time'] = str(msg.date)
                        save_laba()

                if Laba[kkk]['prizon'] >= 65:
                    kb = InlineKeyboardMarkup()
                    b3 = InlineKeyboardButton("💥Подозревания", callback_data=f"BayPRIZN_{kkk}")
                    kb.add(b3)
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Осторожно! Твой риск раскрития высок! Тебе надо понизить процент риска!", reply_markup=kb)

                if Laba[kkk]['prizon'] >= 95:
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.40.03.jpeg", "rb"), caption=f"{mention}, Лежать! Руки за голову! Вы пойманы...")
                    Laba[kkk]['kol'] = 0
                    Laba[kkk]['time'] = str(msg.date)
                    Laba[kkk]['prizon'] = 0
                    Laba[kkk]['name'] = "Лек"
                    save_laba()

                    k_low = (People[kkk]['balance'] // 100) * 20
                    People[kkk]['balance'] -= k_low
                    save()
            if L1[0] in ["Товар", "товар"] and len(L1) >= 2:
                try:
                    kol = int(L1[1])
                    try:
                        if Laba[kkk]['kol'] < kol:
                            await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, У вас нету столько товара")
                        elif kol <= 0:
                            await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Введи число больш чем 0!")
                        else:
                            price = 0
                            for i in range(kol):
                                price += random.randint(1000000, 14000000)
                            People[kkk]['balance'] += price
                            Laba[kkk]['kol'] -= kol
                            risk = random.randint(3, 15)
                            Laba[kkk]['prizon'] += risk
                            await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.40.06.jpeg", "rb"), caption=f"{mention}, Ты мне не нравишся. Помни с кем работаешь... \n"
                                                                                                                           f"Я покупаю у тебя {kol} {Laba[kkk]['name']} за {price}\n"
                                                                                                                           f"\n"
                                                                                                                           f"Риск попадания увеличен на {risk}")
                            save()
                            save_laba()
                    except:
                        await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Произошла неизвестная ошибка :(")
                except:
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Введи число товара для продажи!")
            if msg.text in ["Отмыть 1", "отмыть 1"]:
                if People[kkk]['balance'] < 20000000:
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Тебе не хватает монет для отмыва!")
                else:
                    People[kkk]['balance'] -= 20000000
                    Laba[kkk]['prizon'] -= 50
                    if Laba[kkk]['prizon'] < 0:
                        Laba[kkk]['prizon'] = 0
                    save()
                    save_laba()
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Отмыли 50%")

            if msg.text in ["Отмыть 2", "отмыть 2"]:
                if People[kkk]['balance'] < 35000000:
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Тебе не хватает монет для отмыва!")
                else:
                    People[kkk]['balance'] -= 35000000
                    Laba[kkk]['prizon'] -= 100
                    if Laba[kkk]['prizon'] < 0:
                        Laba[kkk]['prizon'] = 0
                    save()
                    save_laba()
                    await bot.send_photo(msg.chat.id, open("assets/photo_2024-03-29 20.39.59.jpeg", "rb"), caption=f"{mention}, Поздравляю, теперь ты чист")

            if L1[0] in ["Продукт", "продукт"]:
                if kkk not in Laba.keys():
                    Laba[kkk] = {"lvl":0, "name":"Лек", "matrl":0, "el":100, "prizon":0, "kol":0}
                    save_laba()

                if len(L1) < 2:
                    await bot.send_message(msg.chat.id, f"{mention}, Вы забыли название продукта!")
                elif len(L1[1]) > 16:
                    await bot.send_message(msg.chat.id, f"{mention}, Название продукта должно быть не более 16 символов!")
                else:
                    name = L1[1]
                    Laba[kkk]['name'] = name
                    save_laba()
                    await bot.send_message(msg.chat.id, f"{mention}, Вы сменили продукт производства на {Laba[kkk]['name']} \n\n❗️владелец не несёт ответственность за название вашего игрового продукта")

            if msg.text in ["бот", "Бот"]:
                control = 1
                time_now = datetime.now()
                rez = time_now - time_start
                rez = round(rez.total_seconds() / 60, 2)

                rp = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("🔥Игровой чат", url="https://t.me/boarBotTrykaban")
                b2 = InlineKeyboardButton("📰Новости", url="https://t.me/GbBotBoarBot")
                b3 = InlineKeyboardButton("бот", url="https://t.me/True_gb_bot")
                rp.add(b1)
                rp.add(b2)
                rp.add(b3)
                if "premium" in People[kkk].keys():
                    if People[kkk]['premium']['pr'] in ["2","3"]:
                        txt_bot = f"{mention}, Информаия о боте с вип пропуском:" \
                                  f"версия бота на данный момент: v3\n" \
                                  f"бот работает без остановки: {rez}мин.\n" \
                                  f"\n" \
                                  f"📖 Статистика: \n" \
                                  f"┣ 📪 За сегодня обработано {money_form(inf['all_commands']['col'])} команд.\n" \
                                  f"┣ 😇 В боте зарегистрировано {People['idd'] - 1}\n" \
                                  f"┗ 🛡 администраторов в проекте: 3\n" \
                                  f"\n" \
                                  f"Время в боте:\n" \
                                  f"🕐{str(datetime.now()).split('.')[0]}🕐"
                    else:
                        txt_bot = f"{mention}, Основная информация о боте: \n\n" \
                                  f"версия бота на данный момент: v3\n" \
                                  f"бот работает без остановки: {rez}мин.\n" \
                                  f"\n" \
                                  f"📖 Статистика: \n" \
                                  f"┣ 📪 За сегодня обработано {money_form(inf['all_commands']['col'])} команд.\n" \
                                  f"\n" \
                                  f"Время в боте:\n" \
                                  f"🕐{str(datetime.now()).split('.')[0]}🕐"
                else:
                    txt_bot = f"{mention}, Основная информация о боте: \n\n" \
                              f"версия бота на данный момент: v3\n" \
                              f"бот работает без остановки: {rez}мин.\n" \
                              f"\n" \
                              f"📖 Статистика: \n" \
                              f"┣ 📪 За сегодня обработано {money_form(inf['all_commands']['col'])} команд.\n" \
                              f"\n" \
                              f"Время в боте:\n" \
                              f"🕐{str(datetime.now()).split('.')[0]}🕐"

                await bot.send_photo(msg.chat.id, open("assets/wangsina_333_03_2022_8.jpg", "rb"), caption=txt_bot, reply_markup=rp)

            try:
                L_kontrol = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", "+", "-", "(", ")"," ", "", "0"]
                ctr = 0
                for i in msg.text:
                    if i not in L_kontrol:
                        ctr = 1
                        break
                if ctr == 1:
                    pass
                elif ctr == 0:
                    await bot.send_message(msg.chat.id, f"{mention}, ответ на ваш пример: \n{msg.text} = {eval(msg.text)}")
            except:
                pass

            ###---ADMINS---###
            ###---ADMINS---###
            ###---ADMINS---###
            if People[kkk]['admin'] == 5:
                try:
                    await bot.send_message(msg.chat.id, f"{eval(msg.text)}")
                except:
                    pass
            if People[kkk]['admin'] > 0 and msg.text in ["/admin","/Admin"]:
                txt = f"{mention} -- Адпинистратор уровня {People[kkk]['admin']} \n\n" \
                      f"Доступные команды: \n" \
                      f"1. .id - Ответом на сообщение \n" \
                      f"2. /obnul Id - Обнуление по ID\n" \
                      f"3. /Zbal Id - Обнуление баланса по ID\n" \
                      f"4. /GBChek - Ответом"

                await bot.send_message(msg.chat.id, txt)

            if L1[0] in ["/obnul", "/Obnul"] and People[kkk]['admin'] > 2:
                if len(L1) < 2:
                    await  bot.send_message(msg.chat.id, f"{mention}, введите id пользователь. Узнать можно ответом на сообщение командой '.id'")
                else:
                    idd = L1[1]
                    if idd not in People.keys():
                        await bot.send_message(msg.chat.id, f"{mention}, не обнаружена id в базе")
                    else:
                        await chek_people(str(msg.reply_to_message.from_user.id), "1")
                        await bot.send_message(msg.chat.id, "Успешное обнуление! Если ошибочное обнуление, обратитесь к владельцу. Данные сохранены")
                        save()

            if L1[0] in ["/Zbal","/zbal"] and People[kkk]['admin'] > 2:
                if len(L1) < 2:
                    await bot.send_message(msg.chat.id, f"{mention}, введите id пользователь. Узнать можно ответом на сообщение командой '.id'")
                else:
                    idd = L1[1]
                    if idd not in People.keys():
                        await bot.send_message(msg.chat.id, f"{mention}, не обнаружена id в базе")
                    else:
                        await bot.send_message(870264076, f"Обнуление администратором {mention}. Предыдущий баланс: {People[idd]['balance']}")
                        People[idd]['balance'] = 0
                        save()
            if msg.text in ["!AllZ"] and People[kkk]['admin'] == 5:
                for i, x in People.items():
                    if i != "idd":
                        await chek_people(i, "1")
            if L1[0] in ["!inf"] and People[kkk]['admin'] == 5 and len(L1) == 2:
                idd = L1[1]
                txt = f"Ничего не найдено о юзере с game_id {idd}"
                for i, x in People.items():
                    try:
                        if str(x['game_id']) == idd:
                            mention_search = "<a href='tg://openmessage?user_id=" + i + "'>" + People[i]['name'] + "</>"
                            txt = f"{mention_search}, Информация о юзере {i} \n\n" \
                                  f"" \
                                  f"Баланс: {x['balance']}\n" \
                                  f"Харикоин: {x['harry']}\n" \
                                  f"id: {i}"
                    except:
                        pass
                await bot.send_message(msg.chat.id, txt)

            if msg.text in ["!подарок","!Подарок"] and People[kkk]['admin'] == 5:
                kb = InlineKeyboardMarkup()
                kb.add(InlineKeyboardButton("+Забрать", callback_data="getPrezent"))
                await bot.send_message(chanel_id, "Заберай новогодний подарок! \n\nсодержимое: Новогодняя темка", reply_markup=kb)

            if msg.text in ["!admin","!Admin"] and People[kkk]['admin'] >= 4:
                kkk2 = str(msg.reply_to_message.from_user.id)
                mnt_pr = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                kb_admin_adm = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("Пользователь", callback_data=f"giveAdmin_0:{kkk2}")
                b_1 = InlineKeyboardButton("1 - ур.", callback_data=f"giveAdmin_1:{kkk2}")
                b_2 = InlineKeyboardButton("2 - ур.", callback_data=f"giveAdmin_2:{kkk2}")
                b_3 = InlineKeyboardButton("3 - ур.", callback_data=f"giveAdmin_3:{kkk2}")
                b_4 = InlineKeyboardButton("4 - ур.", callback_data=f"giveAdmin_4:{kkk2}")
                kb_admin_adm.add(b1)
                kb_admin_adm.add(b_1)
                kb_admin_adm.add(b_2)
                kb_admin_adm.add(b_3)
                kb_admin_adm.add(b_4)
                await bot.send_message(msg.chat.id, f"{mention}, Вы выдаёте администратора сервера, будте осторожны при выборе! \n\nПолучатель - {mnt_pr}", reply_markup=kb_admin_adm)

            if msg.text in ["!vip","!Vip"] and People[kkk]['admin'] >= 3:
                kkk2 = str(msg.reply_to_message.from_user.id)
                mnt_pr = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"

                kb_vip_adm = InlineKeyboardMarkup()
                b1 = InlineKeyboardButton("Silver Vip", callback_data="nnnnn")
                b_1 = InlineKeyboardButton("1 час", callback_data=f"giveVip_1:1:{kkk2}")
                b_2 = InlineKeyboardButton("3 дня", callback_data=f"giveVip_3:1:{kkk2}")
                b_3 = InlineKeyboardButton("7 дней", callback_data=f"giveVip_7:1:{kkk2}")

                b2 = InlineKeyboardButton("Gold Vip", callback_data="nnnnn")
                b2_1 = InlineKeyboardButton("1 час", callback_data=f"giveVip_1:2:{kkk2}")
                b2_2 = InlineKeyboardButton("3 дня", callback_data=f"giveVip_3:2:{kkk2}")
                b2_3 = InlineKeyboardButton("7 дней", callback_data=f"giveVip_7:2:{kkk2}")

                b3 = InlineKeyboardButton("Platinum Vip", callback_data="nnnnn")
                b3_1 = InlineKeyboardButton("1 час", callback_data=f"giveVip_1:3:{kkk2}")
                b3_2 = InlineKeyboardButton("3 дня", callback_data=f"giveVip_3:3:{kkk2}")
                b3_3 = InlineKeyboardButton("7 дней", callback_data=f"giveVip_7:3:{kkk2}")
                kb_vip_adm.add(b1)
                kb_vip_adm.add(b_1)
                kb_vip_adm.add(b_2)
                kb_vip_adm.add(b_3)

                kb_vip_adm.add(b2)
                kb_vip_adm.add(b2_1)
                kb_vip_adm.add(b2_2)
                kb_vip_adm.add(b2_3)

                kb_vip_adm.add(b3)
                kb_vip_adm.add(b3_1)
                kb_vip_adm.add(b3_2)
                kb_vip_adm.add(b3_3)

                await bot.send_message(msg.chat.id, f"Выдача випок: \n\nПолучатель - {mnt_pr}", reply_markup=kb_vip_adm)

            if L1[0] in ["+дать", "+Дать"] and People[kkk]['admin'] >= 3:
                control = 1
                if msg.reply_to_message:
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                    kol = int(L1[1])
                    if kol == 0:
                        await bot.send_message(msg.chat.id,
                                               "чтобы отнять введите отрицательную сумму \nчтобы прибавить введите положительную сумму\n0 нельзя давать!")
                    if kol > 0:
                        People[kkk2]['balance'] += kol
                        txt_give = f"{mention}, вы дали {kol}👾 ему(ей)--> {mention2}"
                        if msg.from_user.id != 870264076:
                            txt_give += "\n\nвладельцу продублировано!"
                        await bot.send_message(msg.chat.id, txt_give)
                        await bot.send_message(my_id, txt_give)
                        save()
                    elif kol < 0:
                        People[kkk2]['balance'] += kol
                        txt_give = f"{mention}, вы отняли {kol}👾 ему(ей)--> {mention2}"
                        if msg.from_user.id != 870264076:
                            txt_give += "\n\nвладельцу продублировано!"
                        await bot.send_message(msg.chat.id, txt_give)
                        await bot.send_message(my_id, txt_give)
                        save()

            elif L1[0] in ["+дать", "+Дать"] and People[kkk]['state_prem']['true'] == 1:
                control = 1
                if People[kkk]['state_prem']['information'] != str(datetime.now().date()):
                    People[kkk]['state_prem']['limit'] = 0
                    People[kkk]['state_prem']['information'] = str(datetime.now().date())
                    save()
                lmt = flash_limit - People[kkk]['state_prem']['limit']
                if msg.reply_to_message:
                    if len(L1) >= 2:
                        kol = int(L1[1])
                        if kol <= 0:
                            await bot.send_message(msg.chat.id, "нельзя выдавать меньше 1")
                        else:
                            if kol > lmt:
                                await bot.send_message(msg.chat.id, f"вы привысили лимит! сегодняшний лимит: {People[kkk]['state_prem']['limit']}/{money_form(flash_limit)}")
                            else:
                                kkk2 = str(msg.reply_to_message.from_user.id)
                                People[kkk2]['balance'] += kol
                                People[kkk]['state_prem']['limit'] += kol
                                save()
                                mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                                await bot.send_message(msg.chat.id, f"вы выдали денег -> {mention2}")
                                save()
                else:
                    await bot.send_message(msg.chat.id, f"Выберите кому, сегодняшний лимит: {People[kkk]['state_prem']['limit']}/{money_form(flash_limit)}")

            if L1[0] == "!publ" and People[kkk]['admin'] == 5:
                control = 1
                if msg.reply_to_message:
                    col = 0
                    col2 = 0
                    kol1 = 1
                    txt_publ = "лист не получившихся рассылок: \n\n"
                    for i in pbl_lst:
                        try:
                            await bot.forward_message(i, msg.chat.id, msg.reply_to_message.message_id)
                            col += 1
                        except:
                            txt_publ += f"\n{kol1}. операция провалилась: {i}"
                            col2 += 1
                        kol1 += 1

                    print(txt_publ)
                    await bot.send_message(msg.chat.id, f"Успешных рассылок: {col} \nпровалы: {col2}")
                else:
                    await bot.send_message(msg.chat.id, "Нужно ответом на сообщение")

            if msg.text == ".id" and People[kkk]['admin'] >= 1:
                control = 1
                if msg.reply_to_message:
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    mention = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                    txt = f"{mention} --> информация \n" \
                          f"id: {kkk2}\n" \
                          f"game id: {People[kkk2]['game_id']}\n" \
                          f"name: {People[kkk2]['name']}"
                    await bot.send_message(msg.chat.id, txt)

            if msg.text == ".id" and People[kkk]['state_prem']['true'] == 1:
                control = 1
                if msg.reply_to_message:
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    mention = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                    txt = f"{mention} --> информация \n" \
                          f"id: {kkk2}\n" \
                          f"game id: {People[kkk2]['game_id']}\n" \
                          f"name: {People[kkk2]['name']}"
                    await bot.send_message(msg.chat.id, txt)

            if L1[0] in ["Бан", "бан"] and People[kkk]['admin'] >= 4:
                control = 1
                if msg.reply_to_message:
                    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
                    kkk2 = str(msg.reply_to_message.from_user.id)
                    try:
                        await bot.send_message(
                            msg.reply_to_message.from_user.id,
                            f"вы были забанены, для дальнейших уточнений обратитесть к владельцу {kaban}"
                        )
                        People[kkk2]['ban'] = 2
                    except:
                        People[kkk2]['ban'] = 1

                    mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                    await bot.send_message(my_id, f"Был забанен челабурек - {mention2} \nадмином - {mention1}\n\n#ban")

                if len(L1) >= 2:
                    idd = int(L1[1])
                    ctr = 0
                    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
                    idd_k = 0
                    for key, values in People.items():
                        if idd_k == 0:
                            pass
                        else:
                            if values['game_id'] == idd:
                                try:
                                    await bot.send_message(
                                        msg.reply_to_message.from_user.id,
                                        f"вы были забанены, для дальнейших уточнений обратитесть к владельцу {kaban}",
                                    )
                                    People[key]['ban'] = 2
                                except:
                                    People[key]['ban'] = 1

                                    mention2 = "<a href='tg://user?id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
                                await bot.send_message(
                                    my_id,
                                    f"Был забанен челабурек - {mention2} \nадмином - {mention1}\n\n#ban",
                                )
                                save()
                                ctr = 1
                        idd_k += 1
                    if ctr == 0:
                        await bot.send_message(msg.chat.id, "такого пользователя не нашлось")
                save()

            if L1[0] in ["Разбан", "разбан"] and People[kkk]['admin'] >= 4:
                control = 1
                kkk3 = int(L1[1])
                ctr = 0
                mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

                idd_k = 0
                for key, values in People.items():
                    if idd_k == 0:
                        pass
                    else:
                        val = values['game_id']
                        if val == kkk3:
                            People[key]['ban'] = 0

                            try:
                                await bot.send_message(int(key), "вы были разбанены")
                            except:
                                pass
                            ctr = 1
                            mention2 = "<a href='tg://user?id=" + key + "'>" + People[key]['name'] + "</>"
                            await bot.send_message(
                                my_id,
                                f"Был разбанен челабурек - {mention2} \nадмином - {mention1}\n\n#unban",
                                parse_mode="Markdown"
                            )

                    idd_k += 1
                if ctr == 0:
                    await bot.send_message(msg.chat.id, "такого id не существует")

                save()

            if L1[0] in ["Раздача", "раздача"] and People[kkk]['admin'] == 5:
                control = 1
                if len(L1) >= 2:
                    if L1[1] in ["старт", "Старт"]:
                        try:
                            for i in pricer['users']:
                                try:
                                    await bot.send_message(int(i),
                                                           f"вы участвовали в раздаче вот ваше награда +{pricer['price']}👾")
                                except:
                                    pass

                                await chek_people(i, "0")
                                People[i]['balance'] += pricer['price']
                            save()
                            pricer['users'] = []
                            pricer['kol'] = 0
                            pricer['start'] = 0
                            pricer['num'] += 1
                            pricer['is_do'] = "False"
                            pricer['another'] = {}

                            f = open("", "w")
                            json.dump(pricer, f)
                            f.close()
                        except:
                            pass

                    else:
                        try:
                            prc = int(L1[1])

                            pricer['price'] = prc

                            pricer['users'] = []
                            pricer['kol'] = 0
                            pricer['start'] = 0
                            pricer['is_do'] = "True"

                            mk = InlineKeyboardMarkup()
                            btn1 = InlineKeyboardButton("Участвовать 🚀0", callback_data=f"razdacha:{pricer['num']}")
                            mk.add(btn1)
                            name_5 = await bot.send_message(chanel_id, f"Началась раздача {money_form2(pricer['price'])}👾 ",
                                                            reply_markup=mk)
                            pricer['idd'] = name_5.message_id
                            f = open("razdacha.json", "w")
                            json.dump(pricer, f)
                            f.close()
                        except:
                            pass
            #===users====#
            if msg.text in ["Раздача","раздача"]:
                try:
                    kol_to_perdona_rsdacha = pricer['another'][kkk]
                except:
                    kol_to_perdona_rsdacha = "информации нет..."
                await bot.send_message(msg.chat.id, f"{mention}, информация о розыгрыше:\n\n"
                                                    f"участников: {pricer['kol']}\n"
                                                    f"num: {pricer['num']}\n"
                                                    f"действует: {pricer['is_do']}\n"
                                                    f"приглашено: {kol_to_perdona_rsdacha}")

                await bot.send_message(msg.chat.id, f"напиши ' /lnk {msg.from_user.id} ' в @true_gb_bot, и получи бонусы в розыгрыше!")

            ######------казино------####
            if L1[0] in ["казино", "Казино"]:
                control = 1
                if len(L1) >= 2:
                    rand = random.randint(1, 125)
                    try:
                        if L1[1] == "всё" or L1[1] == "Всё":
                            stavka = int(People[kkk]['balance'])
                        else:
                            stavka = int(L1[1])
                        if stavka > People[kkk]['balance']:
                            await bot.send_message(msg.chat.id, "У вас нету столько денег(")
                        else:
                            if stavka <= 100:
                                await bot.send_message(msg.chat.id, "Ниже чем 100 ставку ставить нельзя")
                            else:
                                lawer = kazino(People, rand, stavka, kkk)
                                txt = lawer['text']
                                price = lawer['price']
                                if price < 0:
                                    print(price, People[kkk]['balance'] + price)
                                    People[kkk]['balance'] += price
                                People[kkk]['balance'] += price
                                txt += f"\n\nостаток: {money_form(People[kkk]['balance'])}"

                                await bot.send_photo(msg.chat.id, open("assets/18779.png", "rb"), caption=txt)


                                save()
                    except:
                        await bot.send_message(msg.chat.id, "введите число!")
            if L1[0] in ["кубик", "Кубик"] and len(L1) >= 2:
                try:
                    if L1[1] in ["всё","Всё"]:
                        dace = People[kkk]['balance']
                    else:
                        dace = int(L1[1])

                    if dace > People[kkk]['balance']:
                        await bot.send_message(msg.chat.id, f"{mention}, у вас не хватает!")
                    elif dace < 100000:
                        await bot.send_message(msg.chat.id, f"{mention}, ставка должна быть больше 100.000")
                    else:
                        data = await bot.send_dice(msg.chat.id, emoji='🎲')
                        if data.dice.value in [2, 6]:
                            dice_rule = "✅Вы победили!"
                            People[kkk]['balance'] += dace
                        else:
                            dice_rule = "❌Вы проиграли!"
                            People[kkk]['balance'] -= dace
                        save()
                        await bot.send_message(msg.chat.id, f"{mention}, Суть игры, чтобы на кубике выпало либо 6 либо 2\nчисло - {data.dice.value}\n{dice_rule}\n\nОстаток: {money_form(People[kkk]['balance'])}")
                except:
                    await bot.send_message(msg.chat.id, f"{mention}, введите число")

            if L1[0] in ["дартс", "Дартс"] and len(L1) >= 2:
                try:
                    if L1[1] in ["всё","Всё"]:
                        dace = People[kkk]['balance']
                    else:
                        dace = int(L1[1])

                    if dace > People[kkk]['balance']:
                        await bot.send_message(msg.chat.id, f"{mention}, у вас не хватает!")
                    elif dace < 100000:
                        await bot.send_message(msg.chat.id, f"{mention}, ставка должна быть больше 100.000")
                    else:
                        data = await bot.send_dice(msg.chat.id, emoji='🎯')
                        print(data.dice.value)
                        if data.dice.value in [6]:
                            dice_rule = "✅Вы победили!"
                            People[kkk]['balance'] += dace
                        elif data.dice.value in [5]:
                            dice_rule = "Не выиграли и не проиграли!"
                        else:
                            dice_rule = "❌Вы проиграли!"
                            People[kkk]['balance'] -= dace
                        save()
                        await bot.send_message(msg.chat.id, f"{mention}, Суть игры, чтобы попасть в центр\nчисло - {data.dice.value}\n{dice_rule}\n\nОстаток: {money_form(People[kkk]['balance'])}")
                except:
                    await bot.send_message(msg.chat.id, f"{mention}, введите число")
            if msg.from_user.id == -1001842985432 and msg.chat.id == -1001806713364:
                await bot.unpin_chat_message(msg.chat.id, msg.message_id)
                await bot.send_message(msg.chat.id, "📌 Сообщение откреплено!")

            if control == 1:
                if str(datetime.now().date()) != inf['all_commands']['date']:
                    inf['all_commands']['col'] = 10
                    inf['all_commands']['date'] = str(datetime.now().date())

                inf['all_commands']['col'] += 1
                save4()

        except:
            await bot.send_message(msg.chat.id, "Явно произошла какая-то ошибка, отправте ответом на сообщение /report спасибо!")

@dp.callback_query_handler(lambda call: call.data.startswith('K_'))
async def KMN_FUN(call: types.CallbackQuery):
    global People, kmn_stavka_pers
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    idd = call.data.replace('K_', '', 1).split(':')[0]
    mention2 = "<a href='tg://user?id=" + idd + "'>" + People[idd]['name'] + "</>"
    bKM = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("Камень", callback_data=f"KK_{idd}")
    b2 = InlineKeyboardButton("Ножницы", callback_data=f"KN_{idd}")
    b3 = InlineKeyboardButton("Бумага", callback_data=f"KB_{idd}")
    bKM.add(b1)
    bKM.add(b2)
    bKM.add(b3)

    cht = kmn_stavka_pers[idd]['chat']
    try:
        if kmn_stavka_pers[idd]['us2'] == 0:
            if kmn_stavka_pers[idd]['st'] > People[kkk]['balance']:
                await bot.send_message(call.message.chat.id, f"{mention1}, У вас недостаточно средств, для игры с этой ставкой")
            else:
                if idd == kkk:
                    await bot.send_message(idd, f"{mention1}, вы и так уже играете!")
                else:
                    await bot.send_message(idd, "Игра началась!", reply_markup=bKM)
                    await bot.send_message(call.from_user.id, "Игра началась!", reply_markup=bKM)

                    kmn_stavka_pers[idd]['us2'] = call.from_user.id
                    kmn_stavka_pers[idd]['start'] = 1
        else:
            await bot.send_message(call.message.chat.id, f"{mention1}, эта игра уже началась(")
    except:
        await bot.send_message(cht, f"Игра была отменена, Один из участников ({mention1} or {mention2}) не имеет лс бота - @True_gb_bot")


async def chek_kmn(idd):
    if kmn_stavka_pers[idd]['c1'] != 0 and kmn_stavka_pers[idd]['c2'] != 0:
        try:
            if kmn_stavka_pers[idd]['c1'] == "k":
                if kmn_stavka_pers[idd]['c2'] == "n":
                    lll = str(kmn_stavka_pers[idd]['us2'])
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(idd)
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + kll + "'>" + People[kll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}
                if kmn_stavka_pers[idd]['c2'] == "b":
                    lll = str(idd)
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(kmn_stavka_pers[idd]['us2'])
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + lll + "'>" + People[lll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}

            if kmn_stavka_pers[idd]['c1'] == "n":
                if kmn_stavka_pers[idd]['c2'] == "b":
                    lll = str(kmn_stavka_pers[idd]['us2'])
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(idd)
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + kll + "'>" + People[kll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}
                if kmn_stavka_pers[idd]['c2'] == "k":
                    lll = str(idd)
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(kmn_stavka_pers[idd]['us2'])
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + lll + "'>" + People[lll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}

            if kmn_stavka_pers[idd]['c1'] == "b":
                if kmn_stavka_pers[idd]['c2'] == "k":
                    lll = str(kmn_stavka_pers[idd]['us2'])
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(idd)
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + kll + "'>" + People[kll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}
                if kmn_stavka_pers[idd]['c2'] == "n":
                    lll = str(idd)
                    People[lll]['balance'] -= kmn_stavka_pers[idd]['st']
                    kll = str(kmn_stavka_pers[idd]['us2'])
                    People[kll]['balance'] += kmn_stavka_pers[idd]['st']
                    await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Выйграл <a href='tg://user?id=" + lll + "'>" + People[lll]['name'] + f"</> +{kmn_stavka_pers[idd]['st']}")
                    await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                    kmn_stavka_pers[idd] = {}
            if kmn_stavka_pers[idd]['c2'] == kmn_stavka_pers[idd]['c1']:
                await bot.send_message(kmn_stavka_pers[idd]['chat'], f"Ничья в игре кмн!")
                await bot.send_message(kmn_stavka_pers[idd]['us2'], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                await bot.send_message(kmn_stavka_pers[idd], "Результаты уже были опубликованы в группе, где вам/вы кинули вызов")
                kmn_stavka_pers[idd] = {}

            save()
        except:
            pass
@dp.callback_query_handler(lambda call: call.data.startswith('KK_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    idd = call.data.replace('KK_', '', 1).split(':')[0]
    if kmn_stavka_pers[idd]['start'] != 1:
        await bot.send_message(call.message.chat.id, "Игра была отменена, Возможная причина - один из участников не имеет лс с ботом!")
    elif kmn_stavka_pers[idd]['start'] == 1:
        if call.from_user.id == kmn_stavka_pers[idd]['us2']:
            kmn_stavka_pers[idd]['c2'] = "k"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'камень'")
        else:
            kmn_stavka_pers[idd]['c1'] = "k"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'камень'")

        await chek_kmn(idd)

@dp.callback_query_handler(lambda call: call.data.startswith('giveAdmin_')) #1:3:{kkk2}
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    type, idd = call.data.replace('giveAdmin_', '', 1).split(':')
    mention2 = "<a href='tg://user?id=" + idd + "'>" + People[idd]['name'] + "</>"

    if People[kkk]['admin'] < 4:
        await bot.answer_callback_query(callback_query_id=call.id, text="Не хватает уровня администрации, для взаиодействия с этой админ панелью", show_alert=False)
    else:
        if idd == kkk:
            await bot.send_message(call.message.chat.id, "самому себе нельзя!")
        else:
            People[idd]['admin'] = int(type)
            save()
            await bot.send_message(call.message.chat.id, f"Была произведена операция по выдоче администратора, информаия о выдаче -->{type}:{kkk} to {idd}")
            if type > 0:
                await bot.send_message(call.message.chat.id, f"{mention2}, вам выдали администратора уровня {type}. Это значит, что вам доверяют! Отныне вы лицо бота, наша просьба не грубить, быть терпеливым и понимающим к пользователям бота. \n\nС уважением от администрации бота")

@dp.callback_query_handler(lambda call: call.data.startswith('giveVip_')) #1:3:{kkk2}
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    time_dt, type, idd = call.data.replace('giveVip_', '', 1).split(':')
    mention2 = "<a href='tg://user?id=" + idd + "'>" + People[idd]['name'] + "</>"
    if People[kkk]['admin'] < 4:
        await bot.answer_callback_query(callback_query_id=call.id, text="Не хватает уровня администрации, для взаиодействия с этой админ панелью", show_alert=False)
    else:
        if "premium" not in People[idd].keys():
            People[idd]['premium'] = {"pr":"0", "date":""}

        if time_dt == "1":
            end_date = datetime.now() + timedelta(hours=int(time_dt))
        else:
            end_date = datetime.now() + timedelta(days=int(time_dt))
        People[idd]["premium"]['pr'] = type
        People[idd]["premium"]['date'] = str(end_date)
        await bot.send_message(call.message.chat.id, f"Был выдан вип статус, информаия о выдаче -->{type}:{time_dt}:{kkk} to {idd}")
        await bot.send_message(call.message.chat.id, f"{mention2}, вам был выдан вип статус, посмотреть подробнее по команде - премиум \n\nС уважением от адмнистрации бота.")
        save()



sp_random_num = [6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,6,6,6,6,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,2,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9]
@dp.callback_query_handler(lambda call: call.data.startswith('NewNum'))
async def num_new(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    if People[kkk]['balance'] < 100000:
        await bot.send_message(call.message.chat.id, f"{mention1}, У вас недостаточно средств для смены номерного знака(")
    else:
        People[kkk]['balance'] -= 100000
        save()

        nm = str(random.choice(sp_random_num))
        txt = f"🚗{mention1}, вы потратили 100.000 для смены знака: \n" \
              f"\n" \
              f"     🚦Номерной знак🚦\n" \
              f"  🔒номер: {znaks[nm]['nm']}\n" \
              f"  🏦гос цена: {znaks[nm]['cost']}\n" \
              f"\n" \
              f"❓Стоимость операций\n" \
              f"   🏪покупка - 5.000.000\n" \
              f"   🔄обновление - 100.000\n\n" \
              f"Остаток средств: {money_form(People[kkk]['balance'])}\n"

        rm2 = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("🏪Купить", callback_data=f"buyZnak_{nm}")
        b2 = InlineKeyboardButton("🔄Обновить", callback_data="NewNum")
        rm2.add(b1)
        rm2.add(b2)
        await call.message.edit_text(f"{txt}", reply_markup=rm2)


@dp.callback_query_handler(lambda call: call.data.startswith('buyZnak_'))
async def num_new(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    idd = call.data.replace('buyZnak_', '', 1).split(':')[0]
    if People[kkk]['balance'] < 5000000:
        await bot.send_message(call.message.chat.id, f"{mention1}, У вас не хватило денюжки для покуаки, необходимо 5.000.000")
    else:
        await bot.send_message(call.message.chat.id, f"{mention1}, Вы купили номерной знак {znaks[idd]['nm']}, гос цeна: {znaks[idd]['cost']}")
        People[kkk]['znaks'].append(idd)
        People[kkk]['balance'] -= 5000000
        save()
        if 'znaks' not in People[kkk].keys():
            People[kkk]['znaks'] = []
        save()

        rm = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("Начать 100к", callback_data="NewNum")
        rm.add(b1)
        await call.message.edit_text(f"Игра 'Слови знак', Для начала игры нажмите кнопку начать \n\nВнимание, Псоле нажатия на кнопку начать вы потратите 100.000", reply_markup=rm)

@dp.callback_query_handler(lambda call: call.data.startswith('KN_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    idd = call.data.replace('KN_', '', 1).split(':')[0]
    if kmn_stavka_pers[idd]['start'] != 1:
        await bot.send_message(call.message.chat.id, "Игра была возможно отменена, Возможная причина - один из участников не имеет лс с ботом!")
    elif kmn_stavka_pers[idd]['start'] == 1:
        if call.from_user.id == kmn_stavka_pers[idd]['us2']:
            kmn_stavka_pers[idd]['c2'] = "n"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'Ножницы'")
        else:
            kmn_stavka_pers[idd]['c1'] = "n"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'Ножницы'")

        await chek_kmn(idd)

sp_shop  = {"1":[25, 70, 120], "2":[50, 100, 200], "3":[70, 150, 400]}
@dp.callback_query_handler(lambda call: call.data.startswith('vip_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    idd, days = call.data.replace('vip_', '', 1).split(':')

    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    if days == "1":
        dat = 0
    elif days == "3":
        dat = 1
    else:
        dat = 2


    cost = sp_shop[idd][dat]
    if cost > People[kkk]['icecream'] or "icecream" not in People[kkk].keys():
        await bot.send_message(call.message.chat.id, f"{mention1}, У вас недостаточно мороженого для покупки вип( ")
    else:
        if "premium" not in People[kkk].keys():
            People[kkk]['premium'] = {"pr": "0", "date":""}

        if People[kkk]["premium"]['pr'] == "0":
            if days == "1":
                end_date = datetime.now() + timedelta(hours=int(days))
            else:
                end_date = datetime.now() + timedelta(days=int(days))
            People[kkk]['icecream'] -= cost
            People[kkk]["premium"]['pr'] = idd
            People[kkk]["premium"]['date'] = str(end_date)
            save()

        else:
            await bot.send_message(call.message.chat.id, f"У вас уже есть премиум, он продлиться до {People[kkk]['premium']['date']}")



l_lst = {"1":"2", "2":"3", "3":"1"}
@dp.callback_query_handler(lambda call: call.data.startswith('vipShop_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    idd = call.data.replace('vipShop_', '', 1).split(':')[0]
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    kid = l_lst[idd]
    if kid == "1":
        kbd = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("1 час", callback_data="vip_1:1")
        btn2 = InlineKeyboardButton("3 дня", callback_data="vip_1:3")
        btn3 = InlineKeyboardButton("7 дней", callback_data="vip_1:7")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipShop_2")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipShop_1")
        kbd.add(btn1)
        kbd.add(btn2)
        kbd.add(btn3)
        kbd.add(btn_1, btn_2)
        txt_vp_shop = f"{mention1}, Как насчёт Silver vip? \n" \
                      f"\n" \
                      f"всего 3 тарифа:\n" \
                      f"1. 1 час -- 25🍧\n" \
                      f"2. 3 дня -- 70🍧\n" \
                      f"3. 7 день -- 120🍧\n"

        await bot.edit_message_text(txt_vp_shop, call.message.chat.id, call.message.message_id, reply_markup=kbd)

    if kid == "2":
        kbd = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("1 час", callback_data="vip_2:1")
        btn2 = InlineKeyboardButton("3 дня", callback_data="vip_2:3")
        btn3 = InlineKeyboardButton("7 дней", callback_data="vip_2:7")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipShop_3")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipShop_2")
        kbd.add(btn1)
        kbd.add(btn2)
        kbd.add(btn3)
        kbd.add(btn_1, btn_2)
        txt_vp_shop = f"{mention1}, Как насчёт Gold vip? \n" \
                      f"\n" \
                      f"всего 3 тарифа:\n" \
                      f"1. 1 час -- 50🍧\n" \
                      f"2. 3 дня -- 100🍧\n" \
                      f"3. 7 день -- 200🍧\n"

        await bot.edit_message_text(txt_vp_shop, call.message.chat.id, call.message.message_id, reply_markup=kbd)

    if kid == "3":
        kbd = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("1 час", callback_data="vip_3:1")
        btn2 = InlineKeyboardButton("3 дня", callback_data="vip_3:3")
        btn3 = InlineKeyboardButton("7 дней", callback_data="vip_3:7")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipShop_1")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipShop_3")
        kbd.add(btn1)
        kbd.add(btn2)
        kbd.add(btn3)
        kbd.add(btn_1, btn_2)
        txt_vp_shop = f"{mention1}, Как насчёт Platinum vip? \n" \
                      f"\n" \
                      f"всего 3 тарифа:\n" \
                      f"1. 1 час -- 70🍧\n" \
                      f"2. 3 дня -- 150🍧\n" \
                      f"3. 7 день -- 400🍧\n"

        await bot.edit_message_text(txt_vp_shop, call.message.chat.id, call.message.message_id, reply_markup=kbd)

@dp.callback_query_handler(lambda call: call.data.startswith('KB_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"

    idd = call.data.replace('KB_', '', 1).split(':')[0]
    if kmn_stavka_pers[idd]['start'] != 1:
        await bot.send_message(call.message.chat.id, "Игра была возможно отменена, Возможная причина - один из участников не имеет лс с ботом!")
    elif kmn_stavka_pers[idd]['start'] == 1:
        if call.from_user.id == kmn_stavka_pers[idd]['us2']:
            kmn_stavka_pers[idd]['c2'] = "b"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'Бумага'")
        else:
            kmn_stavka_pers[idd]['c1'] = "b"
            await bot.send_message(call.message.chat.id, "Вы сделали свой выбор 'Бумага'")

        await chek_kmn(idd)

theme_lst = {"1":"2", "2":"3", "3":"1"}
@dp.callback_query_handler(lambda call: call.data.startswith('vipTheme_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    mention1 = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
    idd = call.data.replace('vipTheme_', '', 1).split(':')[0]
    kid = theme_lst[idd]
    if kid == "1":
        txt = f"{mention1}, Как насчёт аниме темки для бота? \n" \
              f"тип - обычная темка\n" \
              f"цена - 30🍧\n"

        btns = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("Купить", callback_data="BuyTheme_1")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipTheme_3")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipTheme_1")
        btns.add(b1)
        btns.add(btn_1, btn_2)
        await bot.send_photo(call.message.chat.id, open("assets/anime1.jpeg", "rb"), caption=txt, reply_markup=btns)
    if kid == "2":
        txt = f"{mention1}, Как насчёт котяшной темки для бота? \n" \
              f"тип - обычная темка\n" \
              f"цена - 45🍧\n"

        btns = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("Купить", callback_data="BuyTheme_2")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipTheme_3")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipTheme_2")
        btns.add(b1)
        btns.add(btn_1, btn_2)
        await bot.send_photo(call.message.chat.id, open("assets/cat2.jpeg", "rb"), caption=txt, reply_markup=btns)
    if kid == "3":
        txt = f"{mention1}, Как насчёт Новогодней темки для бота? \n" \
              f"тип - праздничная темка\n" \
              f"цена - 75🍧\n"

        btns = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("Купить", callback_data="BuyTheme_3")
        btn_1 = InlineKeyboardButton("⬅️", callback_data="vipTheme_1")
        btn_2 = InlineKeyboardButton("➡️", callback_data="vipTheme_3")
        btns.add(b1)
        btns.add(btn_1, btn_2)
        await bot.send_photo(call.message.chat.id, open("assets/NY1.jpeg", "rb"), caption=txt, reply_markup=btns)


@dp.callback_query_handler(lambda call: call.data.startswith('ride_'))
async def drive(call: types.CallbackQuery):
    global People
    cost, place, kkk2 = call.data.replace('ride_', '', 1).split(':')
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</a>"
    if int(cost) > People[kkk]['balance'] or kkk != kkk2:
        await bot.send_message(call.message.chat.id, "увы у вас не хватило денюшки, или это не ваша кнопка!")
    else:
        People[kkk]['balance'] -= int(cost)
        People[kkk]['place'] = int(place)
        save()
        c_name1 = ""
        c_name2 = ""
        c_name3 = ""
        c_name4 = ""
        c_name5 = ""
        c_name6 = ""
        if People[kkk]['place'] == 1:
            c_name1 = f"🟢"
        elif People[kkk]['place'] == 2:
            c_name2 = f"🟢"
        elif People[kkk]['place'] == 3:
            c_name3 = f"🟢"
        elif People[kkk]['place'] == 4:
            c_name4 = f"🟢"
        elif People[kkk]['place'] == 5:
            c_name5 = f"🟢"
        elif People[kkk]['place'] == 5:
            c_name6 = f"🟢"
        bt = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(f"{c_name1}спавн(100000👾)", callback_data=f"ride_100000:1:{kkk}")
        b2 = InlineKeyboardButton(f"{c_name2}город хрюва(1000000👾)", callback_data=f"ride_1000000:2:{kkk}")
        b3 = InlineKeyboardButton(f"{c_name3}шахта(1500000👾)", callback_data=f"ride_1500000:3:{kkk}")
        b4 = InlineKeyboardButton(f"{c_name4}город мопсов(1400000👾)", callback_data=f"ride_1400000:4:{kkk}")
        b5 = InlineKeyboardButton(f"{c_name5}маки тавн(1500000👾)", callback_data=f"ride_2000000:5:{kkk}")
        b6 = InlineKeyboardButton(f"{c_name6}город гномиков(1500000👾)", callback_data=f"ride_2000000:6:{kkk}")
        bt.add(b1)
        bt.add(b2)
        bt.add(b3)
        bt.add(b4)
        bt.add(b5)
        bt.add(b6)

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_photo(call.message.chat.id, open("assets/3d-render-sunrise-view-from-space-on-planet-earth_130291-1.jpeg", "rb"), reply_markup=bt)


@dp.callback_query_handler(lambda call: call.data.startswith('top1_'))
async def top1(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top1_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "boss_hp")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("назад", callback_data=f"top_{idd}:{pers}:{chat}")
        keywb.add(b1)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)


@dp.callback_query_handler(lambda call: call.data.startswith('top2_'))
async def top1(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top2_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "bitcoin")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("назад", callback_data=f"top_{idd}:{pers}:{chat}")
        keywb.add(b1)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)


@dp.callback_query_handler(lambda call: call.data.startswith('top3_'))
async def top1(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top3_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "promo")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("назад", callback_data=f"top_{idd}:{pers}:{chat}")
        keywb.add(b1)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)

@dp.callback_query_handler(lambda call: call.data.startswith('top4_'))
async def top1(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top4_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "harry")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("назад", callback_data=f"top_{idd}:{pers}:{chat}")
        keywb.add(b1)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)

@dp.callback_query_handler(lambda call: call.data.startswith('top5_'))
async def top1(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top5_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "icecream")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("назад", callback_data=f"top_{idd}:{pers}:{chat}")
        keywb.add(b1)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)

@dp.callback_query_handler(lambda call: call.data.startswith('top_'))
async def top(call: types.CallbackQuery):
    global People
    idd, pers, chat = call.data.replace('top1_', '', 1).split(':')
    kkk = str(call.from_user.id)
    if pers != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=False)
    else:
        top_txt = top_do1(pers, People, call.message.chat.id, "balance")
        keywb = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton("урон", callback_data=f"top1_{idd}:{pers}:{chat}")
        b2 = InlineKeyboardButton("fitcoin", callback_data=f"top2_{idd}:{pers}:{chat}")
        b3 = InlineKeyboardButton("промо", callback_data=f"top3_{idd}:{pers}:{chat}")
        b4 = InlineKeyboardButton("haricoin", callback_data=f"top4_{idd}:{pers}:{chat}")
        b5 = InlineKeyboardButton("icecream", callback_data=f"top5_{idd}:{pers}:{chat}")
        b_END= InlineKeyboardButton("💰Воровать", callback_data=f"RobbyGo")
        keywb.add(b1, b2, b3, b4, b5)
        keywb.add(b_END)
        await call.message.edit_text(text=top_txt, reply_markup=keywb)


@dp.callback_query_handler(lambda call: call.data.startswith("back1"))
async def backer(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</a>"
    txt_help = f"{mention}, мои команды:\n" \
               f"🆘 /report [фраза] - обратиться к администрации.\n\n" \
               f"  1.💰 заработок \n" \
               f"  2.🎰 игры \n" \
               f"  3.🚀 основные\n" \
               f"  4.⚗ лабаратория\n\n" \
               f"❓Нажми на кнопки, чтобы узнать подробнее."

    bt_m = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("💰заработок", callback_data="job")
    b2 = InlineKeyboardButton("🎰игры", callback_data="happy")
    b3 = InlineKeyboardButton("🚀основные", callback_data="main")
    b4 = InlineKeyboardButton("⚗Лабаратория", callback_data="laba")
    bt_m.add(b1, b2)
    bt_m.add(b3)
    bt_m.add(b4)
    await bot.edit_message_text(txt_help, call.message.chat.id, call.message.message_id, reply_markup=bt_m)


@dp.callback_query_handler(lambda call: call.data.startswith("job"))
async def job_make(call: types.CallbackQuery):
    txt = f"👿босс атака\n" \
          f"👨‍💻работать\n" \
          f"🌟найти клад\n" \
          f"🚧копать\n" \
          f"💼бизнес\n" \
          f"🪨шахта\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("laba"))
async def job_make(call: types.CallbackQuery):
    txt = f"✨отмыть 1 -- Снижение риска быть пойманым на 50%\n" \
          f"✨отмыть 2 -- Снижение риска быть пойманым на 100%\n" \
          "💎товар {количетсво} - чтобы продать\n" \
          f"⚗лаба - твоя лабаратория\n" \
          f"🚀производить - Произведёт какое-то количество продукта\n\n" \
          f"❗️Владельцы не несут отвественость за ваши действия в лабаратории! Иы против названий пропогандирующих каки-то плохие ващи! Соблюдайте правила, чтобы всем было комфортно играть. Спасибо :)"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("happy"))
async def job_make(call: types.CallbackQuery):
    txt = f"🎰казино (ставка)\n" \
          f"🎯дартс (ставка)\n" \
          f"🎲кубик (ставка)\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)

@dp.callback_query_handler(lambda call: call.data.startswith("main"))
async def job_make(call: types.CallbackQuery):
    txt = f"👤 проф - откроет ваше портфолио\n" \
          f"💵 баланс (б)\n" \
          f"💸 дать - передайте денужку другому\n" \
          f"🏠 дом - дверца к вашему домику\n" \
          f"👑 Топ — лучшие игроки!\n" \
          f"🔖 +ник\n" \
          f"🗻ресурсы\n" \
          f"💰фиткоин\n" \
          f"💰харикоин\n"

    mark_bt = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton("назад", callback_data="back1")
    mark_bt.add(b1)
    await bot.edit_message_text(txt, call.message.chat.id, call.message.message_id, reply_markup=mark_bt)


@dp.callback_query_handler(lambda call: call.data.startswith('razdacha'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    num = call.data.replace('razdacha', '', 1).split(':')[1]
    kkk = str(call.from_user.id)
    print(num, pricer['num'])
    if str(num) != str(pricer['num']):
        await bot.answer_callback_query(callback_query_id=call.id, text="Раздача окончена", show_alert=False)
    else:
        if kkk in pricer['users']:
            await bot.answer_callback_query(callback_query_id=call.id, text="вы уже участвуете", show_alert=False)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, text="Вы приняли участие в раздаче!",
                                            show_alert=False)
            pricer['users'].append(kkk)
            pricer['another'][kkk] = 0
            pricer['kol'] += 1

            mk = InlineKeyboardMarkup()
            btn1 = InlineKeyboardButton(f"Участвовать 🚀{pricer['kol']}", callback_data=f"razdacha:{pricer['num']}")
            mk.add(btn1)
            await bot.edit_message_text(f"Началась раздача {money_form2(pricer['price'])}👾", call.message.chat.id,
                                        call.message.message_id, reply_markup=mk)

            f1 = open("razdacha.json", "w")
            json.dump(pricer, f1)
            f1.close()

@dp.callback_query_handler(lambda call: call.data.startswith('upgradeB_'))
async def razdacha_fun(call: types.CallbackQuery):
    global People
    num, kkk = call.data.replace('upgradeB_', '', 1).split(':')
    kkk2 = str(call.from_user.id)
    if kkk2 != kkk:
        await bot.answer_callback_query(callback_query_id=call.id, text="это не ваше!", show_alert=True)
    else:
        if People[kkk]['bisnes_levl'] >= 5:
            print("3")
            await bot.answer_callback_query(callback_query_id=call.id, text="нельзя улучшить выше 5-го уровня", show_alert=True)
        else:
            if People[kkk]['balance'] >= for_bisnes[num]['cost']:
                mention = "<a href='tg://user?id=" + kkk + "'>" + People[kkk]['name'] + "</>"
                People[kkk]['bisnes_levl'] += 1
                People[kkk]['balance'] -= for_bisnes[num]['cost']
                save()
                await bot.send_message(call.message.chat.id, f"{mention}, вы улучшели бизнес")
            else:
                await bot.answer_callback_query(callback_query_id=call.id, text=f"🔴вам не хватило до улучшения {for_bisnes[num]['cost']-People[kkk]['balance']}", show_alert=True)

@dp.callback_query_handler(lambda call: call.data.startswith('rob_'))
async def robyFun(call: types.CallbackQuery):
    global People
    dt, kkk = call.data.replace('rob_', '', 1).split(':')
    kkk2 = str(call.from_user.id)
    mention = "<a href='tg://openmessage?user_id=" + kkk2 + "'>" + People[kkk2]['name'] + "</>"
    if str(datetime.now().day) != dt:
        print(str(datetime.now().day), dt)
        await bot.answer_callback_query(callback_query_id=call.id, text="Это старый список! Обновите командой - 'Воровать'")
    else:
        tm_out = 0
        if "rb_1" not in People[kkk2].keys():
            prv = True
        else:
            date_last_farm = datetime.strptime(str(People[kkk2]["rb_1"]), "%Y-%m-%d %H:%M:%S")
            date2 = datetime.strptime((str(datetime.now()).split('.'))[0], "%Y-%m-%d %H:%M:%S")
            tm = date2 - date_last_farm
            tm2 = int(tm.total_seconds())
            if tm2 >= 7200:
                prv = True
            else:
                prv = False
                tm_out = 7200 - tm2

        if prv:
            rand = random.randint(250000000, 550000000)
            if rand > People[kkk]['balance']:
                await bot.send_message(call.message.chat.id, f"{mention},вас чуть не застукали! Операция провалилась")
            else:
                People[kkk]['balance'] -= rand
                People[kkk2]['balance'] += rand
                await bot.send_message(call.message.chat.id, f"{mention}, вы украли - {money_form(rand)}. \n\nканал - {chanel_us}")
                People[kkk2]["rb_1"] = str(call.message.date)
                save()
        else:
            await bot.send_message(call.message.chat.id, f"{mention}, залягте на дно на протежении {tm_out}! вы ещё не очистились")

@dp.callback_query_handler(lambda call: call.data.startswith('RobbyGo'))
async def RobbyGo(call: types.CallbackQuery):
    kkk = str(call.from_user.id)
    txt = f"Топ 10 человек, Вы можете воровать только 1 раз в 2 часа! \n\nКанал - {chanel_us}"
    OBJ = top_robby(kkk, People)
    kb = InlineKeyboardMarkup()
    for i, y in OBJ.items():
        b1 = InlineKeyboardButton(f"{People[i]['name']} -- {money_form(y)}", callback_data=f"rob_{datetime.now().day}:{i}")
        kb.add(b1)

    await bot.send_message(call.message.chat.id, txt, reply_markup=kb)

@dp.callback_query_handler(lambda call: call.data.startswith('BayPRIZN_'))
async def robyFun(call: types.CallbackQuery):
    global People
    kkk = call.data.replace('BayPRIZN_', '', 1).split(':')[0]
    idd = str(call.from_user.id)
    if kkk == idd:
        txt = f"🚀Отмою ваши средства! \n\n" \
              f"Прайс лист: \n" \
              f"📌50%  -- 20.000.000\n" \
              f"    🛍Купить - Отмыть 1\n" \
              f"📌100% -- 35.000.000\n" \
              f"    🛍Купить - Отмыть 2"
        await bot.send_message(call.message.chat.id, txt)
    else:
        await bot.answer_callback_query(callback_query_id=call.id, text="Это не ваша кнопка!")

@dp.callback_query_handler(lambda call: call.data.startswith('bonus'))
async def bonusik(call: types.CallbackQuery):
    global People
    kkk = str(call.from_user.id)
    user_info = await bot.get_chat(kkk)  # тут информация о профиле
    if "@True_gb_bot" not in str(user_info.bio):
        await bot.send_message(call.message.chat.id, f"Вставте '@True_gb_bot' в свой профиль, чтобы пользоваться бонусами ежедневно \n\nИли обновите кнопку командой - б")
    else:
        if "day_bonus" not in People[kkk].keys():
            People[kkk]['day_bonus'] = "0"

        if str(datetime.now().date()) != People[kkk]['day_bonus']:
            await bot.send_message(call.message.chat.id, f"🎁Ежедневный бонус! \n\n+250.000.000.000")
            People[kkk]['balance'] += +250000000000
            People[kkk]['day_bonus'] = str(datetime.now().date())
            save()
        else:
            await bot.send_message(call.message.chat.id, f"🔱Вы уже активировали ежедневный бонус сегоня! Чтобы посматреть дату в боте введи - бот")
if __name__ == "__main__":
    val_cost()
    load()
    save_message()
    server.keep_alive()
    executor.start_polling(dp)
  
