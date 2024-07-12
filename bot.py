import telebot

bot = telebot.TeleBot('7357518923:AAGVpjjVmUBCI_-3bVdGErBqMcsU4sjJBR4')

@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        # Create a keyboard with a button to open the Web App
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text='STORE', url='https://t.me/qwertyshoping_bot/SHOP')
        keyboard.add(url_button)

        # Send the keyboard to the user
        bot.send_message(message.chat.id, 'Добро пожаловать в QWERTY SHOP! Прошу Вас перейти в Web App для доступа ко всем товарам:', reply_markup=keyboard)
    except Exception as e:
        print(f'An error occurred: {e}')

bot.polling()