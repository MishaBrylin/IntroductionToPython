import random
import re
import itertools
import telebot

from telebot import types
import random



def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:

        if len(i) == 1:
            i.append(0)
    if pol[-1][1] == pol[-2][1]:
        pol[-2][1] = 1
    for i in range(len(pol)):
        for j in range(0, len(pol[i])-1, 2):
            pol[i][j] = pol[i][j].replace("x", "")

            if pol[i][j] == "":
                pol[i][j] = 1
    for i in range(len(pol)):
        for j in range(len(pol[i])):

            pol[i][j] = int(pol[i][j])

    return pol


def fold_pols(pol11, pol22):
    if len(pol11) < len(pol22):
        pol1 = pol11
        pol2 = pol22
    else:
        pol1 = pol22
        pol2 = pol11
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res


def get_sum_pol(pol):
    var = ['x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)]
               for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = 'x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))


def polynom(k):

    z = random.randint(0, 100)

    if z == 0:
        f = '= 0'
    else:
        f = f'{z} = 0'
    for i in range(int(k)):
        z = random.randint(0, 100)

        if i == 0:
            if z == 0:
                f = f
            else:
                f = f'{z}x + {f} '
        elif z == 0:
            f = f
        elif z == 1:
            f = f'x^{i+1} + {f}'
        else:
            f = f'{z}x^{i+1} + {f}'

    else:
        print('Порпрубуйте еще раз')
    return f


bot = telebot.TeleBot('5698706371:AAHwmortZrLj-0IAkbx4tMqqno1p9YKpwJY')


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Нажмите на эту кномку и введите число")

    markup.add(but1)
    bot.send_message(message.from_user.id, "Добрый день! Этот бот генерирует два многочлена и выводит сумму многочлена. Нажмите на кнопу и введите число, которое будет определять количество элементов. ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Нажмите на эту кномку и введите число":

        bot.send_message(message.from_user.id, 'Введите число ')
        bot.register_next_step_handler(message, get_calc_msg)


def get_calc_msg(message):

    global pol1

    try:
        g = int(message.text)

    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    pol1 = polynom(g)
    bot.send_message(message.from_user.id, f' Ваш многочлен: \n{pol1}')
    bot.send_message(message.from_user.id, f' Введите второе число')
    bot.register_next_step_handler(message, get_calc_msg2)


def get_calc_msg2(message):

    try:

        o = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    pol2 = polynom(o)
    bot.send_message(message.from_user.id, f' Ваш многочлен: \n{pol2}')
    bot.send_message(message.from_user.id,
                     f'Сумма многочленов: \n{get_sum_pol(fold_pols(convert_pol(pol1), convert_pol(pol2)))} ')


bot.polling(none_stop=True, interval=0)
