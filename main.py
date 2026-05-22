import telebot
from telebot import types
import os
from flask import Flask
import threading

API_TOKEN = '8642685517:AAGGVKJqFf18lkILr_WImf1GxLyjhVEDJNo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("✈️ Мой Telegram", url="https://t.me/Aidoriginal"))
    markup.row(types.InlineKeyboardButton("📸 Мой Instagram", url="https://www.instagram.com/arifmmzde/"))
    markup.row(types.InlineKeyboardButton("💬 Мой Discord", url="https://discord.com/users/1249423387248300134"))

    welcome_text = f"Привет, {message.from_user.first_name}! 👋\n\n Ниже мои соцсети:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

app = Flask(__name__)
@app.route('/')
def home():
    return "Бот работает!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print("Бот запущен на Render!")
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
