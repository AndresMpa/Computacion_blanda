from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

scrapper = Chrome()
scrapper.get("https://www.carulla.com/pollo-carnes-y-pescado?order=OrderByTopSaleDESC")
scrapper.implicitly_wait(0.5)

button = scrapper.find_element(by=By.CSS_SELECTOR, value="exito-geolocation-3-x-cursorPointer")
button.click()

prices = scrapper.find_elements(by=By.CSS_SELECTOR, value="exito-vtex-components-4-x-currencyContainer")
text = pricess.text
print(text)

scrapper.quit()
