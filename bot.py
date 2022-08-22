# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:43:08 2022

@author: Samsung
"""

from transliterator import to_latin, to_cyrillic
import telebot

TOKEN = ' //Please your TOKEN// '

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "👋Assalomu alaykum, Xush kelibsiz !"
    javob += "\n🤖Bu bot orqali siz istalgan so`zingizni"
    javob += " kirilldan lotindan kirilga o`girishingiz mumkin."
    javob += "\n🧑‍💻Dasturchi: @hs_feruz"
    bot.reply_to(message,javob)

@bot.message_handler(commands=['help'])
def send(message):
    javob = "✍️ Kirill alifbosidagi xabarni jo`natsangiz bot sizga"
    javob += " lotin alifbosiga o`girib beradi va aksincha."
    javob += "\n🤖Botdan foydalanish uchun shunchaki xabar jo`nating."
    javob += "\n🧑‍💻Dasturchi: @hs_feruz"
    bot.reply_to(message, javob)

@bot.message_handler(commands=['coder'])
def send(message):
    javob = "\n🧑‍💻Dasturchi: @hs_feruz"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    javob += "\n🧑‍💻Dasturchi: @hs_feruz"
    bot.reply_to(message, javob)

bot.polling()
