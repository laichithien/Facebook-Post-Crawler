from tqdm import tqdm

class Post:
    def __init__(self, post):
        self.post = post
        self.content, self.comments = self.parse_post()

    def parse_post(self):
        post_content = self.get_post_content()
        comments = self.get_comments()
        return post_content, comments
    
    def get_comments(self):
        all_comments = self.post.find_all(class_="xwib8y2")
        list_comments = []
        print('Collecting comments...')
        for comment in tqdm(all_comments):
            # breakpoint()
            user = comment.find('span',{'dir':'auto', 'class':'x4zkp8e'})
            comment_detail = comment.find('span',{'dir':'auto', 'class':'xudqn12'})
            if user is not None and comment_detail is not None:
                user = user.text
                comment_detail = comment_detail.text
                list_comments.append({'user':user, 'comment_detail':comment_detail})
        return list_comments

    def get_post_content(self):
        first_post_content = self.post.find('div', {'class':True, 'dir':'auto'})
        if first_post_content is not None:

            content = first_post_content.find_all('div',{'dir':'auto'})
            content_text = [c.text for c in content]
            full = '\n'.join(content_text)
            return full
        return None