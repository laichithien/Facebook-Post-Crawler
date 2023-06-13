import json
import argparse
def parse_arg():
    parser = argparse.ArgumentParser(
        description='Crawl FB page with page name')
    parser.add_argument('--page', help='ID of page')
    args = parser.parse_args()
    return args

def load():
    args = parse_arg()
    # Opening JSON file
    f = open(f'./data/{args.page}.json', encoding='utf-8')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    for e,datum in enumerate(data):
        print(f'Post {e+1}')
        print(f'Content: {datum["content"]}')
        print(f'Comment: ')  
        for comment in datum['comments']:
            print(f'\t{comment["user"]}: {comment["comment_detail"]}')
        if e>10:
            break
    pass

if __name__=='__main__':
    load()