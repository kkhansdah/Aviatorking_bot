import telebot
from predictor import predict_from_list

BOT_TOKEN = '7832938380:AAFcNqOFR6uIcU9_Yfak4ijddMBxlj8_ScY'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "👋 Aviator Predictor Bot चालू हो गया है!\n\n🧠 Prediction पाने के लिए /predict कमांड भेजें:\nउदाहरण:\n/predict 1.5 2.1 3.0 1.9 5.4")

@bot.message_handler(commands=['predict'])
def predict(m):
    try:
        text = m.text.replace('/predict', '').strip()
        nums = [float(x) for x in text.replace(',', ' ').split()]
        if len(nums) < 5:
            return bot.reply_to(m, "⚠️ कृपया कम से कम 5 multipliers दें!\nउदाहरण: /predict 2.1 1.9 3.0 4.2 1.8")
        result = predict_from_list(nums)
        bot.reply_to(m, f"📊 आखिरी Rounds: {nums[-5:]}\n{result['message']}")
    except:
        bot.reply_to(m, "❌ Format सही नहीं है!\nउदाहरण: /predict 1.5 2.3 3.1 1.8 4.0")

bot.polling()
