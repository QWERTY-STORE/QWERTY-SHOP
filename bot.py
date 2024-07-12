import telebot
from flask import Flask

# Initialize the Telegram bot
bot = telebot.TeleBot('7357518923:AAGVpjjVmUBCI_-3bVdGErBqMcsU4sjJBR4')

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World!'

# Define a route for handling Telegram bot commands
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Hello! Welcome to the bot.')

# Start the Flask app with HTTPS
if __name__ == '__main__':
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'))