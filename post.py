from requestapi import RequestsApi
from comment import Comment
from apientity import Entity


class Post(Entity):

    def __init__(self, post_dict):
        try:
            self.post = {'id': post_dict['id'],
                         'user_id': post_dict['user_id'],
                         'title': post_dict['title'],
                         'body': post_dict['body']}
        finally:
            RequestsApi.post_request(post_dict, "posts")
            self.update_post()
        self.comments = []

    def update_post(self):
        endpoint = f"posts?title={self.post['title']}"
        response = RequestsApi.get_request(endpoint)
        self.post['id'] = response['data'][0]['id']
        self.post['user_id'] = response['data'][0]['user_id']
        self.post['title'] = response['data'][0]['title']
        self.post['body'] = response['data'][0]['body']

    @staticmethod
    def display_post_by_id(post_id):
        Post.display_entity_by_id("posts", post_id)

    def create_comment(self, json_data):
        """
        Creates a comment instance
        :param json_data: comment body
        :return:
        """
        json_data['post_id'] = self.post['id']
        self.comment = Comment(json_data)
        self.comments.append(self.comment)

    def display_post(self):
        """
        Displays the instance created from get
        :return:
        """
        response = RequestsApi.get_request(f"posts?id={self.post['id']}")
        Post.display_entity(response['data'][0])