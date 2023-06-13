from bs4 import BeautifulSoup
import json
import os
from post import Post
from tqdm import tqdm

class Page:
    def __init__(self, page):
        self.page = page
        self.page_source = self.load_page_source()
        self.posts = self.get_all_post()
        self.page_data = self.parse_page()

    def parse_page(self):
        all_post_info = []
        print('Getting info of posts...')
        for post in tqdm(self.posts):
            all_post_info.append(self.post_info(post))
        return all_post_info
    
    def load_page_source(self):
        with open(f"./page_source/{self.page}.html", "r", encoding="utf-8") as f:
            page_source = f.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        return soup
    
    def get_all_post(self):
        return self.page_source.find_all('div', {'role': 'article', 'aria-posinset':True})
    
    def post_info(self, post):
        post_obj = Post(post)

        post_content = post_obj.content
        post_comments = post_obj.comments
        return {'content': post_content, 'comments': post_comments}
    
    def save(self):
        filename = f'./data/{self.page}.json'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.page_data, f, ensure_ascii=False)
    