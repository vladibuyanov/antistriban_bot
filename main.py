import os
from telebot import TeleBot

bot = TeleBot(os.environ.get('TOKEN'))
ID = os.environ.get('ID')
text = 'ДАННАЯ ХРЮКАНИНА СОЗДАНА И (ИЛИ) РАСПРОСТРАНЕНА ПОГАНЫМ ЖАЛОМ, ' \
       'НЕ ЗАКУСИВШИМ УДИЛА, И (ИЛИ) ВЫПОЛНЯЮЩИМ ФУНКЦИИ ШТРИБАНА.'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Тест на штрибана")


@bot.message_handler(content_types=['text'])
def stop_striban(message):
    print(message.from_user.id)
    if message.from_user.id == ID:
        bot.reply_to(message, text)


bot.infinity_polling()
