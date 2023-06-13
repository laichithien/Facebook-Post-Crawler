import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
from tqdm import tqdm

class Driver:
    def __init__(self, headless, page):
        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.page = page
        self.url = f'https://www.facebook.com/{page}'
        
    def start(self, scroll):
        self.driver.get(self.url)
        time.sleep(2)
        self.x_click()
        self.scroll_to_end(scroll)
        self.see_more_click()
        self.see_more_for_post()
        self.save_page_source()

    def x_click(self):
        x_button = self.driver.find_elements_by_css_selector('.x1d69dk1')[5]
        # print(len(self.driver.find_elements_by_css_selector('.x1d69dk1')))
        print('X button clicked')
        self.driver.execute_script("arguments[0].click()", x_button)

    def scroll_to_end(self, scroll):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        # breakpoint()
        print(f'Scrolling...')
        if scroll == -1:
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1.5)
                new_height = self.driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height:
                        break
                last_height = new_height
        else:
            for count in tqdm(range(scroll)):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1.5)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                        break
                last_height = new_height

    def see_more_click(self):
        time.sleep(3)
        count = 0
        try:
            see_more_button = self.driver.find_element_by_css_selector('.x1w0mnb .xi81zsa')
            # see_more_button = driver.find_element(By.XPATH, "//div[contains(text(), 'See more')]")
        except NoSuchElementException:
            see_more_button = None # or whatever default value you want to use
        while(see_more_button is not None):
            self.driver.execute_script("arguments[0].click()", see_more_button)
            count+=1
            print(f'See more clicked: {count}')
            time.sleep(1)
            try:
                see_more_button = self.driver.find_element_by_css_selector('.x1w0mnb .xi81zsa')
                # see_more_button = driver.find_element(By.XPATH, "//div[contains(text(), 'See more')]")
            except NoSuchElementException:
                time.sleep(3)
                try:
                    see_more_button = self.driver.find_element_by_css_selector('.x1w0mnb .xi81zsa')
                except NoSuchElementException:
                    see_more_button = None # or whatever default value you want to use
        return 
    
    def see_more_for_post(self):
        time.sleep(2)
        count = 0
        try:
            # see_more_button = driver.find_element_by_css_selector('.x126k92a .x1s688f')
            see_more_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'See more')]")
        except NoSuchElementException:
            see_more_button = None # or whatever default value you want to use
        while(see_more_button is not None):
            self.driver.execute_script("arguments[0].click()", see_more_button)
            count+=1
            print(f'See more post clicked: {count}')
            time.sleep(1)
            try:
                # see_more_button = driver.find_element_by_css_selector('.x126k92a .x1s688f')
                see_more_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'See more')]")
            except NoSuchElementException:
                time.sleep(3)
                try:
                    see_more_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'See more')]")
                except NoSuchElementException:
                    see_more_button = None # or whatever default value you want to use
        return 
    
    def save_page_source(self):
        page_source = self.driver.page_source
        filename = f"./page_source/{self.page}.html"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(page_source)