from bs4 import BeautifulSoup

from request.main import get_page
from util.env_vars import config


def get_info(timestamp: str) -> None:
    """
    Extrae informacion de un web site y crea un archivo .csv con un timestamp dado

    Args:
        timestamp (str): Una marca de tiempo para poder crear un archivo .csv asociado
    """
    amount_of_pages = config["amount_of_pages"]
    page_number = 1
    rawData = []
    while page_number <= amount_of_pages:
        query = get_page(page_number)
        html_object = BeautifulSoup(query, "html.parser")
        print(html_object)
        html_specific_elements = html_object.find_all(
            "div", class_="vtex-flex-layout-0-x-flexRow--product-info-container")
        rawData.append(html_specific_elements)
        print(html_specific_elements)
        page_number += 1

    print(rawData)
