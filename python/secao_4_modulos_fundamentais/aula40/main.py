#  type: ignore
from pathlib import Path
import time

CAMINHO_RAIZ = Path(__file__).parent
CHROMEDRIVER_EXEC = CAMINHO_RAIZ / 'drivers' / 'chromedriver.exe'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """
    :param options: Opção para adicionar
    :return: retorna o navegador
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


if __name__ == '__main__':

    TIME_TO_WAIT = 10
    options = ()

    chrome_browser.get('https://www.google.com')
    time.sleep(TIME_TO_WAIT)

