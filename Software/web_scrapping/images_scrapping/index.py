# Basic
from os import path as os_path
from sys import argv as ar
from random import choice
from io import BytesIO
import os
# Request
from requests import get
# Pillow
from PIL import Image
# Selenim
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ecs

def create_scrapper(driver):
    # Opciones para para la instancia del navegador
    options = Options()
    options.headless = True
    # Implementacion del servicio de proxy
    PROXY = '127.63.13.19:3184'
    options.add_argument('--proxy-server=%s' % PROXY)

    # Instancia del navigador
    new_scrapper = driver(options=options)

    return new_scrapper

def scroll(scrapper):
    scroll_page_down = 'window.scrollTo(0, document.body.scrollHeight);'
    scrapper.execute_script(scroll_page_down)
    wait(scrapper, 20)

def get_urls(images, scrapper):
    # Clickamos cada imagen y guardamos su url
    images_urls = set()
    for img in images[0:len(images)]:
        try:
            img.click()
            wait(scrapper, 20)
        except Exception:
            continue

        # Sacamos lo links de las imagenes
        current_img = scrapper.find_element(By.CSS_SELECTOR, 'img.n3VNCb')
        if 'http' in current_img.get_attribute('src'):
            images_urls.add(current_img.get_attribute('src'))

    return images_urls

def fetch_query(query:str, number_of_images:int, query_scrapper, silence=True):
    # Definimos un proveedor de imagenes
    google_images = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    query_scrapper.get(google_images.format(q=query))

    # Bajamos hasta el final del domento
    scroll(query_scrapper)

    # Recogemos las urls
    res = query_scrapper.find_elements(By.CSS_SELECTOR, 'img.Q4LuWd')
    wait(scrapper, 20)

    # Capturamos las URL de cada imagen
    urls = get_urls(res, query_scrapper)

    # Mostramos la cantidad de imagenes
    if silence == False:
        print("Se han encontractrado", len(urls), " imagenes que coinciden con tu patrón de busqueda, tomaremos solo ", number_of_images ,end='\n')

    # De los links sacamos solo la cantidad requerida
    images = []
    while len(images) <= number_of_images:
        choosen = choice(list(urls))
        if choosen not in images:
            images.append(choosen)

    return images

def check_path(path):
    # En caso de no existir la carpeta esta se crea
    if not os.path.exists(path):
        os.makedirs(path)

def download_res(urls:str, path:str, silence=True):
    # Verificamos que exista la carpeta
    check_path(path)
    cont = 0

    # Descargamos la imagenes del array
    for url in urls:
        try:
            # Se optiene la imagen
            img_content = get(url).content
        except Exception as e:
            if silence == False:
                print('No fue posible descargar la imagen ', str(url) + ' ', end='')
                print(e)

        try:
            # Se genera el archivo de la imagen
            image_file = BytesIO(img_content)
            image = Image.open(image_file).convert('RGB')
            file_path = os_path.join(path + '/imagen_' + str(cont) + '.jpg')

            # Se guarda la imagen
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)

            # Se confirma que se guardo la imagen
            if silence == False:
                print('Guardado exitosamente -' + str(url) + '- en ' + file_path)
        except Exception as e:
            if silence == False:
                print('ERROR - no se pudo guardar la imagen ' + str(url))
                print(e)
        cont += 1

if __name__ == '__main__':
    # Generamos un scrapper
    print(ar[1])
    scrapper = create_scrapper(Firefox)
    res_urls = fetch_query(ar[1], 10, scrapper)
    download_res(res_urls, os.environ['HOME'] + '/Escritorio/Scrapper')
    scrapper.quit()

