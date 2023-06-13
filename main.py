from driver import Driver
from page import Page
from post import Post
import argparse

def parse_arg():
    parser = argparse.ArgumentParser(
        description='Crawl FB page with page name')
    parser.add_argument('--headless',action='store_true', help='Hide the chrome UI')
    parser.add_argument('--page', help='ID of page')
    parser.add_argument('--scroll',default=-1, help='Scrolling count')
    args = parser.parse_args()
    return args

def crawl():
    args = parse_arg()
    print(f'Scrawling posts and comments from page {args.page} with count scroll: {args.scroll}')
    driver = Driver(args.headless, args.page)
    driver.start(scroll=int(args.scroll))
    page = Page(args.page)
    page.save()

if __name__=='__main__':
    crawl()