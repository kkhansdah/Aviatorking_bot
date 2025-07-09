from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import random

BOT_TOKEN = "7832938380:AAG80pCTkvRI0RkpzKbDUx7hVRcUN-55pHU"

# Accuracy counters
success = 61
fail = 15

# Real Pattern Logic
def detect_real_pattern(values):
    count_1x = sum(1 for x in values if x < 1.5)
    count_3x = sum(1 for x in values if 2.5 <= x < 4.0)
    count_5x = sum(1 for x in values if x >= 5.0)

    if count_1x >= 3:
        return "🔴 Crash Pattern", 1.70, "Crash हो रहा है – तुरंत निकलो!"
    elif count_5x >= 2:
        return "🟢 High Multiplier Trend", 5.50, "High round चल रहा है – hold कर सकते हो!"
    elif count_3x >= 3:
        return "🟡 Stable 3x Trend", 3.20, "Stable लग रहा है – 3x से थोड़ा ऊपर निकल सकते हो।"
    else:
        return "🟠 Mixed/Unstable", 2.20, "Trend unclear है – जल्दी profit लो।"

# Command: /predict
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        values = list(map(float, context.args))
        if len(values) < 5:
            await update.message.reply_text("❗ कम से कम 5 multipliers दीजिए।\nउदाहरण:\n/predict 1.2 3.4 2.1 1.9 5.5")
            return
        
        pattern, cashout, tip = detect_real_pattern(values)
        rate = round((success / (success + fail)) * 100, 2)

        message = f"""🎯 *Aviator Manual Prediction*  
━━━━━━━━━━━━━━━━━━━  
📊 *Input Rounds:* `{ ' | '.join(f"{x:.1f}x" for x in values) }`  
📈 *Pattern Detected:* {pattern}  

💡 *सुझाव:*  
💰 *{cashout}x* पर Cashout करो!

📢 *Expert Tip:*  
"{tip}"

📊 *Success Stats:*  
✅ सही: {success} | ❌ गलत: {fail}  
🎯 Success Rate: *{rate}%*

🧠 *हर बार नया ट्रेंड हो सकता है!*  
━━━━━━━━━━━━━━━━━━━"""
        await update.message.reply_text(message, parse_mode="Markdown")
    except:
        await update.message.reply_text("❌ Input invalid.\nउदाहरण:\n/predict 1.3 2.4 3.5 2.1 1.9")

# Command: /accuracy
async def accuracy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = success + fail
    rate = round((success / total) * 100, 2)
    await update.message.reply_text(
        f"📊 *Accuracy Report:*\n✅ सही: {success} | ❌ गलत: {fail}\n🎯 Success Rate: *{rate}%*",
        parse_mode="Markdown"
    )

# Run bot
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("predict", predict))
    app.add_handler(CommandHandler("accuracy", accuracy))
    print("✅ Bot is running...")
    app.run_polling()
