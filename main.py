import telebot
import time
import threading
from scraper import get_latest_multipliers
from predictor_ai import analyze_pattern_ai

BOT_TOKEN = "7832938380:AAHriQkiKSY9ZK6WGJwJdfL23jxYYYM6smk"
CHAT_ID = None
auto_mode = False

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def start(msg):
    global CHAT_ID
    CHAT_ID = msg.chat.id
    bot.reply_to(msg, "👋 *Aviator Predictor Bot चालू है!*\n\n🧠 Manual prediction: `/predict 1.2 1.8 2.3 1.7 3.1`\n🔄 Auto Mode: /startbot\n⛔ बंद करें: /stopbot")

@bot.message_handler(commands=['predict'])
def manual_predict(msg):
    try:
        nums = list(map(float, msg.text.replace('/predict', '').strip().split()))
        response = analyze_pattern_ai(nums)
        bot.reply_to(msg, response)
    except:
        bot.reply_to(msg, "❌ Format गलत है।\nउदाहरण:\n/predict 1.5 2.1 1.8 3.0 2.5")

@bot.message_handler(commands=['startbot'])
def start_auto(msg):
    global auto_mode, CHAT_ID
    CHAT_ID = msg.chat.id
    auto_mode = True
    bot.reply_to(msg, "🔄 *Auto Mode चालू हो गया है!* हर 15 सेकंड में prediction मिलेगा")
    threading.Thread(target=auto_loop).start()

@bot.message_handler(commands=['stopbot'])
def stop_auto(msg):
    global auto_mode
    auto_mode = False
    bot.reply_to(msg, "⛔ Auto Mode बंद कर दिया गया।")

def auto_loop():
    global auto_mode
    last_data = []
    while auto_mode:
        multipliers = get_latest_multipliers()
        if multipliers and multipliers != last_data:
            last_data = multipliers
            result = analyze_pattern_ai(multipliers[-5:])
            try:
                bot.send_message(CHAT_ID, "📡 *Live Auto Prediction:*\n" + result)
            except Exception as e:
                print("Telegram Error:", e)
        time.sleep(15)

bot.polling()
