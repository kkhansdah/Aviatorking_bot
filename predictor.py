def predict_from_list(multipliers):
    avg = sum(multipliers[-5:]) / 5

    if any(x >= 10 for x in multipliers[-5:]):
        return {
            'message': '🔥 10x या उससे ज़्यादा आया है!\n💸 सलाह: 3x – 5x के अंदर Cashout करें।',
            'level': 'high'
        }
    elif avg >= 3:
        return {
            'message': '📈 Pattern अच्छा दिख रहा है।\n💡 सलाह: 2.5x – 3.0x के बीच Cashout करें।',
            'level': 'medium'
        }
    elif avg >= 2:
        return {
            'message': '📊 Pattern Medium है।\n💡 सलाह: 1.8x – 2.5x के बीच Cashout करें।',
            'level': 'low'
        }
    else:
        return {
            'message': '⚠️ Pattern Risky है!\n❌ जल्दी Cashout करें: 1.5x – 2.0x',
            'level': 'risky'
        }
