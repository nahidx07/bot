import telebot

BOT_TOKEN = "8309162687:8309162687:AAERSYrMuvbnlLabDjuUOheTb1N1rJ3Oi4c"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(
        message,
        "👋 স্বাগতম!\n\n"
        "🤖 আমাদের Telegram Bot-এ আপনাকে স্বাগতম।\n"
        "✨ বটটি ব্যবহার করতে নিচের নির্দেশনা অনুসরণ করুন।\n\n"
        "ধন্যবাদ ❤️"
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "আপনার মেসেজ পেয়েছি! ✅")

print("Bot is running...")
bot.infinity_polling()
