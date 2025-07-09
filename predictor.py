def predict_from_list(nums):
    result = {"3x": 0, "5x": 0, "10x": 0, "20x": 0}
    for num in nums:
        if num >= 3:
            result["3x"] += 1
        if num >= 5:
            result["5x"] += 1
        if num >= 10:
            result["10x"] += 1
        if num >= 20:
            result["20x"] += 1
    return result

def get_message_for_result(result):
    if result["20x"] >= 1:
        return "🚨 पिछले round में 20x आया है – अब crash होने का खतरा ज्यादा है। Safe entry नहीं है।"
    elif result["10x"] >= 1:
        return "🔥 अभी 10x आया है – अगले कुछ round में crash जल्दी हो सकता है।"
    elif result["5x"] >= 2:
        return "🟠 लगातार 5x दिख रहा है – pattern moderate risk में है।"
    elif result["3x"] >= 3:
        return "🟢 Stable trend दिख रहा है – 3x लगातार आ रहा है। Low risk entry संभव है।"
    else:
        return "🔴 कोई भी strong pattern नहीं दिखा – अभी entry avoid करो।"

def get_cashout_suggestion(result):
    if result["20x"] >= 1:
        return "🔻 सिर्फ 1.5x तक ही cashout करो – ज़्यादा देर hold मत करना।"
    elif result["10x"] >= 1:
        return "💸 5x – 7x तक safe cashout zone है।"
    elif result["5x"] >= 2:
        return "📈 3x – 4.5x तक cashout सही रहेगा।"
    elif result["3x"] >= 3:
        return "🟢 2x – 3.2x तक आराम से hold कर सकते हो।"
    else:
        return "⚠️ High risk zone – 1.5x के बाद निकल जाना ठीक रहेगा।"
