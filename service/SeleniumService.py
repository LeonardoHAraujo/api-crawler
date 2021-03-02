import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumService:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def search(self, link, xpath):
        self.driver.get(link)
        sleep(1)

        title = self.driver.find_element_by_xpath(xpath).text

        resp = {
            'Título': title,
            'Link': link
        }

        return json.dumps(resp)