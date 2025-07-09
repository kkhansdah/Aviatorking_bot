import random

def analyze_pattern_ai(multipliers):
    if len(multipliers) < 5:
        return "❌ कम से कम 5 multipliers दो।\nउदाहरण: /predict 1.2 1.5 2.0 1.8 3.5"

    last5 = multipliers[-5:]
    low_count = sum(1 for x in last5 if x <= 1.5)
    high_count = sum(1 for x in last5 if x >= 5)
    avg = sum(last5) / len(last5)

    msg = "📊 पिछली उड़ानें: " + ' | '.join([f"{x}x" for x in last5]) + "\n\n"
    suggestions = []

    if low_count >= 3:
        msg += "⚠️ *Crash pattern देखा गया है!*\n"
        suggestions += [
            "💡 1.5x – 2.0x के बीच cashout करो",
            "⏱️ Rebound का इंतज़ार कर सकते हो",
            "🚫 Over-bet मत करो"
        ]
    elif high_count >= 2:
        msg += "🔥 *High multiplier streak चल रहा है!*\n"
        suggestions += [
            "💰 3x – 5x के बीच cashout करो",
            "🎯 Medium risk – High reward strategy",
            "🧠 धीरज रखो और सही समय पर निकलो"
        ]
    elif avg >= 3.0:
        msg += "📈 *Stable pattern मिला है.*\n"
        suggestions += [
            "✅ 2x – 3x तक try कर सकते हो",
            "🧘 Calm play recommended",
            "🔄 Predictable flight"
        ]
    else:
        msg += "☁️ *Neutral pattern दिख रहा है.*\n"
        suggestions += [
            "🎯 2.0x के अंदर cashout बेहतर रहेगा",
            "💤 Low risk strategy",
            "🧠 Observe and play safe"
        ]

    advice = random.choice(suggestions)
    msg += f"\n💡 सलाह: {advice}"
    return msg
