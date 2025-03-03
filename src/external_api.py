import os

import requests
from dotenv import load_dotenv


def convert_currency(amount: float, from_currency: str, to_currency: str) -> tuple[bool, float]:
    """Конвертация валюты спомощью внешнего API"""
    load_dotenv()
    api_token = os.getenv("API_KEY")
    url = os.getenv("CONVERT_CURRENCY_URL")
    payload = {"amount": str(amount), "from": from_currency, "to": to_currency}
    headers: dict[str, str | None] = {"apikey": api_token}
    response = requests.get(str(url), headers=headers, params=payload)
    if response.status_code != 200:
        return False, 0.0
    return True, response.json()["result"]
