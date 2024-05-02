import requests
from util.env_vars import config


def get_page(page: int) -> object:
    """
    Envia una solicitud a la web site base a una pagina especifica

    Args:
        page (num): Numero de la pagina que se quiere obtener

    Returns:
        query: Un objeto de html
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    query = requests.get(f'{config["web_site"]}&page={page}', headers=headers)

    return query.text
