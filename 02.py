
from telebot import *
import telebot
import logging

bot = telebot.TeleBot('5698706371:AAHwmortZrLj-0IAkbx4tMqqno1p9YKpwJY')

import telebot

from telebot import types
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",

)
logger = logging.getLogger(__name__)
logger = logging.LoggerAdapter(logger, {"app": "тестовое приложение"})



@bot.message_handler(commands=['start'])
def welcome(message):
    logger.info("Калькулятор стартует") 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Калькулятор для рациональных чисел")
    item2 = types.KeyboardButton("Калькулятор для комплексных чисел")
    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, "Выберите калькулятор".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, main)
 
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Калькулятор для рациональных чисел':
     logger.info("Калькулятор вычисляет рациональное число") 
     msg = bot.send_message(message.chat.id, "Введите два числа через запятую затем знак, например- 2,36,*  :\n")
     bot.register_next_step_handler(msg, calc)   
    elif message.text == 'Калькулятор для комплексных чисел':
     logger.info("Калькулятор вычисляет комплексное число")
     msg = bot.send_message(message.chat.id, "Введите два числа комплексных числа через запятую затем знак, например- 3 + 3j,3 + 3j,*  :\n")
     bot.register_next_step_handler(msg, calc2)
        
    else:
     bot.send_message(message.chat.id, 'Я не знаю что ответить :(')

def calc(message):
    a, b, c = message.text.split(',')
    a = int(a)
    b = int(b)
    
    bot.send_message(message.chat.id, f'Результат  = {res(a, b, c)}')

def calc2(message):
    a, b, c = message.text.split(',')
    
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a = complex(a)
    b = complex(b)
    bot.send_message(message.chat.id, f'Результат  = {res(a, b, c)}')


def res(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b    
    elif c == '/':
        try:
            return a / b
        except: 'делить на 0 нельзя' 

bot.polling(none_stop=True)