from requestapi import RequestsApi
from comment import Comment
from apientity import Entity


class Post(Entity):

    def __init__(self, post_dict):
        response = RequestsApi.post_request(post_dict, "posts")
        self.post = dict(id=post_dict['id'], user_id=post_dict['user_id'], title=post_dict['title'],
                         body=post_dict['body'])
        self.post['id'] = response['data']['id']
        self.comments = []

    def update_post(self):
        """
        Makes an update of the attributes from id
        :return:
        """
        endpoint = f"posts?id={self.post['id']}"
        response = RequestsApi.get_request(endpoint)
        self.post['user_id'] = response['data'][0]['user_id']
        self.post['title'] = response['data'][0]['title']
        self.post['body'] = response['data'][0]['body']

    @staticmethod
    def display_post_by_id(post_id):
        """
        Displays any post by id
        :param post_id:
        :return:
        """
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
        Displays the instance created from internal id
        :return:
        """
        response = RequestsApi.get_request(f"posts?id={self.post['id']}")
        Post.display_entity(response['data'][0])
