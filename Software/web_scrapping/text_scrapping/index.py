'''
Para este caso usaremos "selenium" para nuestro scrapper, de selenium tomammos lo
siguiente:

 - argv: Sirve para dar al software la capacidad de tomar datos desde la terminal

 - webdriver: Basicamente nos permitira usar un navegador en concreto para nuestro
 scrapper. Para escoger el respectivo driver según el navergador es necesario
 visitar el link (Sacado de la documentacion de Selenium):

 https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

 - common.by: Nos ayuda a buscar por parametros especificos, selectores id, class,
 tags, etc; de HTML y CSS

 - common.keys: Nos permite emular el comportamiento de un teclado en nuestro
 navegador

 - support.ui (WebDriverWait): Paginas con lazy loading a que simplemente cargan
 la información de forma inteligente nos obligan a usar esta facilidad, como el
 nombre indica a Selenium que ha de esperar una cantidad especifica de tiempo para
 que el contenido de la pagina llegue a cargar del todo ya sea para esperar a la
 carga de imagenes (Como en facebook por ejemplo) o para la carga de grandes porciones
 texto como ocurre con algunos PDF

 - expected_conditions: Indica a Selenium que es lo que debe esperar que suceda
 para proceder con la ejecución de lo que se tenga de codigo, por ejemplo pueden
 ser condiciones como la carga de cierto contenido especifico o la carga de algun
 componente
'''

from sys import argv as ar
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ecs


# Ajustes de producción

'''
Agregando las opciones del navegador en este caso firefox, podemos "saltar" el
paso de mostrar la instancia del navegador, lo cual es más comodo. Para ello se
hace uso de la headless = True
'''

from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

# Agregando un proxy

'''
Para este caso, el proxy no es realmente necesario, pero puede ayudar con otro
tipo de busquedas. Dicho eso los proxies ayudan a hacer de la busqueda algo
más eficiente
'''

PROXY = "127.63.13.19:3184"
options.add_argument('--proxy-server=%s' % PROXY)

'''
Hay 2 formas de generar la instancia del navegador, como se indica a continuación
o usando un "PATH", de la siguiente manera:

PATH = "ruta_de_driver_del_navegador_que_estemos_usando/geckodriver"
driver = webdriver.<tu_navegador>(PATH)

Ya que este condigo está corriendo sobre un entorno virtual no tendremos este
problema; la ruta que se está usando en este caso es la que viene por defecto
en Selenium, es decir:

$ echo $PATH

De la que usamos: "./scrapper/bin/geckodriver"; puedes buscar más información en:
https://www.selenium.dev/documentation/en/webdriver/driver_requirements/ de todos
modos usaremos la variable para no presentar problemas

'''

# Version de desarollo
# path = './scrapper/bin/geckodriver'
# web_scrapper = Firefox(executable_path=path)

# Version de producción
path = './scrapper/bin/geckodriver'
web_scrapper = Firefox(executable_path=path, options=options)

'''
Ahora que tenemos una instancia del navegador, hemos de enviar un dominio para
realizar nuestra busqueda, para este caso; usaremos la imagenes de google como
ejemplo
'''

web_scrapper.get('https://github.com/')

'''
El parametro de busqueda "query" se refiere a la barra de busqueda que vamos a
usar, ya que el dominio que usamos es "simple", solo necesitamos seleccionar una
input
'''

query = web_scrapper.find_element(By.CSS_SELECTOR, 'input.form-control.header-search-input')

'''
Ya que tenemos el buscador de la respectiva pagina, ahora vamos a usar el metodo
send_keys() para enviar nuestra busqueda al navegador respectivo, para el caso de
ejemplo usaremos la palabra "gatitos", luego al mismo parametro le daremos la
instrucción Keys.RETURN para  ejecutar la busqueda (Basicamente seria como dar enter)
'''

query.send_keys(ar[1])
query.send_keys(Keys.RETURN)

'''
Ahora que a hemos ingresado una consulta al buscador falta recoger los datos que esta nos
arroje, para ello usaremos una variable llamada "search_res" (Resultado de la busqueda),
dado que dependiendo de una serie de variable como la conección a internet, la pagina, los
servidores, etc; la consulta que se ingresa puede llegar a tardar un rato, usaremos la
la función WebDriverWait (importada como "wait") para dar una espera a la consulta que
usando la función "until" y las condiciones de espera "ecs" haran que el scrapper espera
el timepo que se especifico (20), hasta que aparescan las etiquetas HTML "img"
'''

search_res = wait(web_scrapper, 20)\
    .until(ecs.presence_of_element_located((By.CSS_SELECTOR, 'ul.repo-list')))

# print(search_res.get_attribute("textContent")) # Es muy util para debugs

# Mejoras en la busqueda

'''
Mediante la opcion execute_script() pordemos ejecutar scripts en nuestro scrapper usualmente
estos seran de JS; esto resulta util cuando la pagina no carga toda la información que
le solicitamos en nuestro query, por ejemplo sucede con las imagenes de google pues
estos son lazy loaders
'''

scroll_page_down = 'window.scrollTo(0, document.body.scrollHeight);'
web_scrapper.execute_script(scroll_page_down)

'''
Ahora que la busqueda se ha completado, nos queda expresar los resultados de la busqueda
para que lo podamos ver, para ello haremos usos de un find_elements_by_css_selector
que nos dara los elementos por un selector de CSS, porteriormente veremos los resultados
de esto con un simple bucle for
'''

repositories = search_res.find_elements(By.CSS_SELECTOR, 'a.v-align-middle')

for res in range(len(repositories)):
    print("Repositorio: ", repositories[res].text, "\nURL: ", repositories[res].get_attribute("href"))

'''
Por último, como buena practica, cerramos la instancia del navegador con la que hemos hecho
toda nuestra busqueda
'''

web_scrapper.quit()
