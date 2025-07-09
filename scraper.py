import requests
from bs4 import BeautifulSoup

def get_live_data():
    try:
        url = "https://kwgvip5.com"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        blocks = soup.find_all("div", class_="crash-point")[:10]
        multipliers = []

        for block in blocks:
            text = block.text.strip().replace("x", "")
            try:
                multipliers.append(float(text))
            except:
                continue

        round_id = "LIVE"
        return multipliers, round_id

    except Exception as e:
        print("❌ Scraper Error:", e)
        return [], "N/A"
