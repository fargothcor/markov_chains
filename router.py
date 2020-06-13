import telebot
from aui import aue

bot = telebot.TeleBot('1282178960:AAEgAUQThoWDDMq98MoEwxPLsLnrvha6-bU')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вечер в Телегу, брат. Научу тебя уму-разуму. '
                                      'Напиши любое слово или символ - отвечу цитаткой')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, aue())
    print(message['json']['text'])


bot.polling()
