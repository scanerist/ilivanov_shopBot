import requests

import xml.etree.ElementTree as ET


def cny_to_rub_converter(value: int) -> float:
    cny_rate = float(
        ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text)
        .find("./Valute[CharCode='CNY']/Value")
        .text.replace(",", ".")) + 1
    return cny_rate * value
