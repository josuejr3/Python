
#### Selenium - Parte 2

-  Documentação do Selenium

	https://selenium-python.readthedocs.io/locating-elements.html


```Python
#  type: ignore  
from pathlib import Path  
import time  
  
CAMINHO_RAIZ = Path(__file__).parent  
CHROMEDRIVER_EXEC = CAMINHO_RAIZ / 'drivers' / 'chromedriver.exe'  
  
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service  
  
def make_chrome_browser(*options: str) -> webdriver.Chrome:  
    """  
    :param options: Opção para adicionar    :return: retorna o navegador  
    """  
    chrome_options = webdriver.ChromeOptions()  
  
    # chrome_options.add_argument('--headless')  
    if options is not None:  
        for option in options:  
            chrome_options.add_argument(option)  # type: ignore  
  
    chrome_service = Service(  
        executable_path=str(CHROMEDRIVER_EXEC),  
    )  
  
    browser = webdriver.Chrome(  
        service=chrome_service,  
        options=chrome_options  
    )  
  
    return browser  
  
  
  
# Opções do navegador  
chrome_options = webdriver.ChromeOptions()  
# Informa qual vai ser o serviço que vai usar o chromedriver  
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))  
# Navegador em si  
chrome_browser = webdriver.Chrome(  
    service=chrome_service,  
    options=chrome_options,  
)  
  
  
# Para fazer seleção de "coisas" em uma página, devemos importar a classe "By"  
from selenium.webdriver.common.by import By  
# Fazer import para aguardar o elemento aparecer na tela  
from selenium.webdriver.support.wait import WebDriverWait  
# Importando condições esperadas  
from selenium.webdriver.support import expected_conditions as EC  
# Importando para utilizar botões do teclado  
from selenium.webdriver.common.keys import Keys  
  
  
if __name__ == '__main__':  
  
    TIME_TO_WAIT = 300  
    options = ()  
  
    # Abre o navegador na página do google  
    chrome_browser.get('https://www.google.com.br/')  
  
    # Espera para encontrar o input  
    search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(  
        EC.presence_of_element_located(  
            (By.NAME, 'q')  
        )  
    )  
    search_input.send_keys("youtube")  
    search_input.send_keys(Keys.ENTER)  
  
    time.sleep(10)  
  
    results = chrome_browser.find_element(By.ID, 'res')  
    links = results.find_elements(By.TAG_NAME, 'a')  
    links[0].click()
```

