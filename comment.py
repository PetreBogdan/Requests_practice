from requestapi import RequestsApi
from apientity import Entity


class Comment(Entity):

    def __init__(self, comment_dict):
        try:
            self.comment = {'id': comment_dict['id'],
                            'post_id': comment_dict['post_id'],
                            'name': comment_dict['name'],
                            'email': comment_dict['email'],
                            'body': comment_dict['body']}
        finally:
            response = RequestsApi.post_request(comment_dict, "comments")
            self.comment['id'] = response['data']['id']

    def update_comment(self):
        """
        Makes an update of the attributes from id
        :return:
        """
        endpoint = f"comment?id={self.comment['id']}"
        response = RequestsApi.get_request(endpoint)
        self.comment['post_id'] = response['data'][0]['post_id']
        self.comment['name'] = response['data'][0]['name']
        self.comment['email'] = response['data'][0]['email']
        self.comment['body'] = response['data'][0]['body']

    def display_comment(self):
        """
        Displays the comment entity from id attribute
        :return:
        """
        response = RequestsApi.get_request(f"comments?id={self.comment['id']}")
        Comment.display_entity(response['data'][0])

    @staticmethod
    def display_comment_by_id(id_comment):
        """
        Displays any comment by id form the API
        :param id_comment:
        :return:
        """
        Comment.display_entity_by_id("comments", id_comment)
