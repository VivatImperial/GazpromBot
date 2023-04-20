from config import API_TOKEN, my_self
from parse import CommandKey, CommandFilter

import telebot
from telebot import types


bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message) -> None:
    """
    Обработка команды /start
    отсылает табло с 3мя кнопками пользователю и поле вводной информации
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поиск с использованием фильтра')
    btn2 = types.KeyboardButton('Поиск по ключевому слову')
    btn3 = types.KeyboardButton('Помогите я застрял в меме')
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id,
        text=my_self
    )

    bot.send_message(
         message.chat.id,
         text="Выберите интересующую вас функцию".format(message.from_user),
         reply_markup=markup
    )


@bot.message_handler(commands=['info', 'help'])
def info(message) -> None:
    """
    Обработка команд /info и /help
    Отсылает вводный текст
    """
    bot.reply_to(message, my_self)


@bot.message_handler(regexp=r'\b[Кк]люч')
def key(message) -> None:
    """
    Ищет слово "ключ" и вызывает функцию
    """
    bot.reply_to(message, CommandKey.key())


@bot.message_handler(regexp=r'\b[Фф]ильтр')
def key(message) -> None:
    """
    Ищет слово "фильтр" и вызывает функцию
    """
    bot.reply_to(message, CommandFilter.filter())


@bot.message_handler(content_types=['text'])
def process(message) -> None:
    """
    Обработка отправленного пользователем текста
    """
    match message.text:

        case 'Помогите я застрял в меме':
            res = f'{CommandKey.__str__()}\n\n{CommandFilter.__str__()}'

        case 'Поиск с использованием фильтра':
            res = CommandFilter.filter()

        case 'Поиск по ключевому слову':
            res = CommandKey.key()

        case _:
            res = 'я не знаю такую команду'

    bot.reply_to(message, res)



if __name__ == '__main__':
    bot.infinity_polling()
