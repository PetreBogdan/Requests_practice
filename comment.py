from requestapi import RequestsApi
import textwrap


class Comment:

    def __init__(self, comment_dict):
        self.comment = {'id': comment_dict['id'],
                     'post_id': comment_dict['post_id'],
                     'name': comment_dict['name'],
                     'email': comment_dict['email'],
                     'body': comment_dict['body']}


    def post_comment(self):
        """
        Post the comment
        :return:
        """
        RequestsApi.post_something(self.comment, 'comments')
        self.comment['id'] = Comment.get_id_by_name(self.comment['name'])

    def display_comment(self):
        """
        Get the body from API and displays nice formatted data
        :return:
        """
        response = RequestsApi.get_something(f"comments?id={self.comment['id']}")
        print(textwrap.dedent(f"""
                                    id of the comment: {response['data'][0]['id']}
                                    Comment_id: {response['data'][0]['post_id']}
                                    Name: {response['data'][0]['name']}
                                    Email: {response['data'][0]['email']}
                                    Body: {response['data'][0]['body']}"""))

    @staticmethod
    def get_id_by_name(name):
        """
        Makes a get request and returns the id of the instance
        :param title: name of the instance
        :return: id of the instance
        """
        endpoint = f"comments?name={name}"
        response = RequestsApi.get_something(endpoint)
        return response['data'][0]['id']
