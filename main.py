import telebot
from telebot import types
import random
import requests
from bs4 import BeautifulSoup
import datetime
from random import choice


#Анекдоты
url = 'https://nekdo.ru/short/1/'
r = requests.get(url)
# print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
anekdots = soup.find_all('div', class_='text')
# print(anekdots)
all_anek = []
for i in anekdots:
    all_anek.append(i.getText())

#Парсинг Курса валют
TOKEN = "5944905857:AAFkw61-C09GtPKOfNKN6wo6pTkhqRT7rgs"

bot = telebot.TeleBot(TOKEN)



#https://t.me/KorostikDima
url_avt = 'https://www.instagram.com/dima_korostik/'
url = 'https://myfin.by/bank/kursy_valjut_nbrb/usd'
url2 = 'https://myfin.by/bank/kursy_valjut_nbrb/eur'

source = requests.get(url)
# main_text = source.text
soup = BeautifulSoup(source.text, 'html.parser')

dollar = soup.find('div', class_="h1")
dollar_cena = dollar.text

source2 = requests.get(url2)
soup = BeautifulSoup(source2.text, 'html.parser')
evro = soup.find('div', class_="h1")
evro2 = evro.text

print(dollar_cena)
print(evro2)








@bot.message_handler(commands=['start'])
def start(message):
    marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Другое ✓ ')
    item2 = types.KeyboardButton('Информация 💁')
    item3 = types.KeyboardButton('Курс валют 💸')
    item4 = types.KeyboardButton('Рандомное число')

    marcup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет 👋 {0.first_name}!'.format(message.from_user), reply_markup=marcup)


@bot.message_handler(content_types=['text'])
def bot_message(message, marcup=None):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, 'Ваще число: ' + str(random.randint(0, 1000)))
        elif message.text == 'Курс валют 💸':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('US Курс Доллара 💵')
            item2 = types.KeyboardButton('EU Курс Евро 💶')
            back = types.KeyboardButton('Назад 🔙')
            marcup.add(item1, item2, back)


            bot.send_message(message.chat.id, 'Курс валют 💸', reply_markup=marcup)

        elif message.text == 'US Курс Доллара 💵':
            bot.send_message(message.chat.id, 'Курс Доллара 💵 ' + dollar_cena)

        elif message.text == 'EU Курс Евро 💶':
            bot.send_message(message.chat.id, 'Курс Евро 💶 ' + evro2)


        elif message.text == 'Информация 💁':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('О боте 🤖')
            item2 = types.KeyboardButton('Что в коробке 📦')
            back = types.KeyboardButton('Назад 🔙')
            marcup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Информация 💁', reply_markup=marcup)



        elif message.text == 'Другое ✓':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Анекдот 🤣')
            item2 = types.KeyboardButton('Подписка на Автора  📩')
            item3 = types.KeyboardButton('Стикер 🧘')
            back = types.KeyboardButton('Назад 🔙')
            marcup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Другое ✓', reply_markup=marcup)

        elif message.text == 'Анекдот 🤣':
            bot.send_message(message.chat.id, choice(all_anek))

        elif message.text == 'Подписка на Автора  📩':
            bot.send_message(message.chat.id, 'Подпишись на автора :) ' + url_avt)

        elif message.text == 'Назад 🔙':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item1 = types.KeyboardButton('Другое ✓ ')
            item2 = types.KeyboardButton('Информация 💁')
            item3 = types.KeyboardButton('Курс валют 💸')
            item4 = types.KeyboardButton('Рандомное число')

            marcup.add(item1, item2, item3, item4)


            bot.send_message(message.chat.id, 'Назад 🔙', reply_markup=marcup)



        elif message.text == 'Стикер 🧘':
            stick = open('static/glaz.webp', 'rb')
            bot.send_sticker(message.chat.id, stick)



bot.polling(none_stop=True)
