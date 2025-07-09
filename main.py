import telebot
from datetime import datetime
from predictor import predict_from_list, get_message_for_result, get_cashout_suggestion
from scraper import get_live_data

BOT_TOKEN = "7832938380:AAFcNqOFR6uIcU9_Yfak4ijddMBxlj8_ScY"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Aviator Predictor Bot चालू है!\n/predict टाइप करें prediction के लिए।")

@bot.message_handler(commands=['predict'])
def handle_predict(message):
    nums, round_id = get_live_data()

    if not nums:
        bot.reply_to(message, "❌ लाइव डेटा नहीं मिल पाया। वेबसाइट डाउन हो सकती है।")
        return

    result = predict_from_list(nums)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prediction = get_message_for_result(result)
    advice = get_cashout_suggestion(result)

    reply = f"""🕒 Time: {now}
🎲 Round ID: #{round_id}

📡 Multipliers: {nums}

🎯 3x+: {result['3x']} बार
💥 5x+: {result['5x']} बार
🔥 10x+: {result['10x']} बार
🚀 20x+: {result['20x']} बार

🧠 Prediction: {prediction}
💸 Cashout Advice: {advice}
"""
    bot.reply_to(message, reply)

print("🤖 Bot चालू हो गया है...")
bot.infinity_polling()
