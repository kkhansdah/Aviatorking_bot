import requests
from bs4 import BeautifulSoup

def get_latest_multipliers():
    url = "https://kwgvip5.com/"

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        divs = soup.find_all("div", class_="profit__number")
        multipliers = []

        for d in divs[:10]:
            text = d.text.strip().replace("x", "")
            if text:
                multipliers.append(float(text))

        return multipliers[::-1]
    except Exception as e:
        print("❌ Error fetching:", e)
        return []
