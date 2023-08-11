import telebot
from telebot import types

token='<აქ ჩაწერთ თქვენი ბოტის ტოკენს>'

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'გამარჯობა, რით შემიძლია დაგეხმაროთ?')

@bot.message_handler(commands=['info'])
def info(message):
    keyboard=types.InlineKeyboardMarkup()
    url_button=types.InlineKeyboardButton(text='ჩემი გვერდი', url='https://avto.din.ge')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'ჩემი გვერდი', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text) 

# bot.polling(none_stop=True)

if __name__ == '__main__':
    # bot.polling(none_stop=True)
    # bot.polling(none_stop=True, interval=0, timeout=20)
    # bot.polling()

    bot.infinity_polling()
