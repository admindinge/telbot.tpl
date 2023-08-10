from telebot import types
import telebot

TOKEN = '6421938969:AAFnmK88ngnOJkPxK4ITDL7m0kAyCkUsxSc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    start_message = """
გამარჯობა, მე ვარ ბოტი!
აი რით შემიძლია დაგეხმარო,
ჩემი შესახებ ინფორმაცია არის აქ: /info
კონსულტაციის მისაღებად: /cons
    """
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(commands=['cons'])
def consultation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("პროგრამები")
    item2 = types.KeyboardButton("რემონტი")
    item3 = types.KeyboardButton("ქსელი")
    
    markup.add(item1, item2, item3)

    msg = bot.send_message(message.chat.id, "Please choose the type of consultation you need:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_consultation_type)

def process_consultation_type(message):
    chat_id = message.chat.id
    if message.text == "პროგრამები":
        bot.send_message(chat_id, "დამიწერეთ თქვენი პრობლემის არსი")
    elif message.text == "რემონტი":
        bot.send_message(chat_id, "რისი რემონტი გსურთ?")
    elif message.text == "ქსელი":
        bot.send_message(chat_id, "Please describe your network issue. Our technicians will respond soon.")
    else:
        bot.send_message(chat_id, "Sorry, I didn't understand that. Please select a valid option from the keyboard.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Handle the user's text messages
    # You can extend this to send the user's messages to your backend or database for further processing
    bot.send_message(message.chat.id, f"You wrote: {message.text}. We'll get back to you shortly!")

if __name__ == '__main__':
    bot.infinity_polling()
