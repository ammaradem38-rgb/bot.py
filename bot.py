import telebot

# 👇 حط توكن البوت متاعك من @BotFather
TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 أهلاً بك في بوت فري فاير! اكتب /help لمزيد من الأوامر 🔥")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """
📜 أوامر البوت:
• /start - بداية البوت
• /info - معلومات عن فري فاير
• /code - يعطيك كود يومي 🔥
    """)

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "🎯 فري فاير لعبة بقاء ممتعة، العب وكن آخر من يبقى حياً!")

@bot.message_handler(commands=['code'])
def code(message):
    bot.reply_to(message, "🎁 كود اليوم: FFRE1234XYZ")

print("✅ Bot is running...")
bot.polling()
