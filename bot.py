import telebot

bot = telebot.TeleBot('7357518923:AAGVpjjVmUBCI_-3bVdGErBqMcsU4sjJBR4')

@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        # Send a welcome message
        bot.reply_to(message, 'Hello! Welcome to the bot.')

        # Create a keyboard with a button to open the Web App
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text='Open Web App', url='https://t.me/qwertyshoping_bot/SHOP')
        keyboard.add(url_button)

        # Send the keyboard to the user
        bot.send_message(message.chat.id, 'Click the button below to open the Web App:', reply_markup=keyboard)
    except Exception as e:
        print(f'An error occurred: {e}')

bot.polling()