import telebot
from telebot import types

bot = telebot.TeleBot('5454592147:AAH0moBxHVVM45CcEarkQjGKT4Wg5J7j0RI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}!</b> Напиши, пожалуйста, свой ник', parse_mode='html')

@bot.message_handler()
def get_user(message):
    nick = message.text
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Понедельник', url = 'vk.com'))
    bot.send_message(message.chat.id, f'Очень приятно, {nick}! Выбери дату, на которую хочешь узнать свое расписание:', reply_markup=markup)
    
    

bot.polling(non_stop=True)
