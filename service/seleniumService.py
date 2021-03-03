import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumService:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def search(self, search):
        """ Bunge function on the site all tasty (capture of the first 3 recipes) """

        self.driver.get(f'https://www.tudogostoso.com.br/busca?q={search}')
        sleep(1)

        # RECIPES CAPTURED
        recipe_1 = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]')
        recipe_2 = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[3]')
        recipe_3 = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[4]')

        # TITLE AND LINKS OF RECIPES
        title_recipe_1 = recipe_1.find_element_by_class_name('title').text
        a_recipe_1 = recipe_1.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/a')
        link_recipe_1 = a_recipe_1.get_attribute('href')
        img_recipe_1 = recipe_1.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/a/picture/img')
        avatar_recipe_1 = img_recipe_1.get_attribute('src')

        title_recipe_2 = recipe_2.find_element_by_class_name('title').text
        a_recipe_2 = recipe_2.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/a')
        link_recipe_2 = a_recipe_2.get_attribute('href')
        img_recipe_2 = recipe_2.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[3]/a/picture/img')
        avatar_recipe_2 = img_recipe_2.get_attribute('src')

        title_recipe_3 = recipe_3.find_element_by_class_name('title').text
        a_recipe_3 = recipe_3.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/a')
        link_recipe_3 = a_recipe_3.get_attribute('href')
        img_recipe_3 = recipe_3.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[4]/a/picture/img')
        avatar_recipe_3 = img_recipe_3.get_attribute('src')

        recipes = [
            {
                'Title': title_recipe_1,
                'Link': link_recipe_1,
                'Avatar': avatar_recipe_1
            },
            {
                'Title': title_recipe_2,
                'Link': link_recipe_2,
                'Avatar': avatar_recipe_2
            },
            {
                'Title': title_recipe_3,
                'Link': link_recipe_3,
                'Avatar': avatar_recipe_3
            },
        ]

        resp = {
            'Status': 200,
            'Message': 'Essas são as três primeiras receitas de Tudo Gostoso',
            'Receitas': recipes
        }

        return json.dumps(resp)