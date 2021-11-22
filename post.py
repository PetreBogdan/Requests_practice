from requestapi import RequestsApi
from comment import Comment
import textwrap


class Post:

    def __init__(self, post_dict):
        self.post = {'id': post_dict['id'],
                     'user_id': post_dict['user_id'],
                     'title': post_dict['title'],
                     'body': post_dict['body']}
        self.comments = []

    def post_post(self):
        """
        Post the post
        :return:
        """
        RequestsApi.post_something(self.post, 'posts')
        self.post['id'] = Post.get_id_by_title(self.post['title'])

    def display_post(self):
        """
        Get the body from API and displays nice formatted data
        :return:
        """
        response = RequestsApi.get_something(f"posts?id={self.post['id']}")
        print(textwrap.dedent(f"""
                                    id: {response['data'][0]['id']}
                                    User_id: {response['data'][0]['user_id']}
                                    Title: {response['data'][0]['title']}
                                    Body: {response['data'][0]['body']}"""))

    @staticmethod
    def get_id_by_title(title):
        """
        Makes a get request and returns the id of the instance
        :param title: title of the instance
        :return: id of the instance
        """
        endpoint = f"posts?title={title}"
        response = RequestsApi.get_something(endpoint)
        return response['data'][0]['id']

    def create_comment(self, json_data):
        """
        Creates a comment instance
        :param json_data: comment body
        :return:
        """
        json_data['post_id'] = self.post['id']
        self.comment = Comment(json_data)
        self.comments.append(self.comment)