import pprint
import textwrap

from requestapi import RequestsApi
from post import Post


class User:

    def __init__(self, user_dict):
        self.user = {'id': user_dict['id'],
                     'name': user_dict['name'],
                     'email': user_dict['email'],
                     'gender': user_dict['gender'],
                     'status': user_dict['status']}
        self.posts = []

    def post_user(self):
        """
        Make a post request and of the instance created
        :return:
        """
        RequestsApi.post_something(self.user, 'users')
        self.user['id'] = User.get_id_by_name(self.user['name'])

    @staticmethod
    def get_id_by_name(name):
        """
        Makes a get request and returns the id of the instance
        :param name: name of the instance
        :return: id of the instance
        """
        endpoint = f"users?name={name}"
        response = RequestsApi.get_something(endpoint)
        return response['data'][0]['id']

    @staticmethod
    def number_of_users():
        """
        Returns the number of users from the API
        :return: the number of users
        """
        response = RequestsApi.get_something('users')
        return response['meta']['pagination']['total']

    def display_instance(self):
        """
        Displays attributes of the instance created
        :return:
        """
        response = RequestsApi.get_something(f"users?id={self.user['id']}")
        User._display_user(response['data'][0])

    @staticmethod
    def display_user_by_id(id_user):
        """
        Displays the data of the user from a get request
        :param id_user: the id of the user
        :return:
        """
        response = RequestsApi.get_something(f"users?id={id_user}")
        User._display_user(response['data'][0])

    @staticmethod
    def _display_user(dictionary):
        """
        Display users
        :param dictionary: the user data
        :return:
        """
        print(textwrap.dedent(f"""
                            id of the user: {dictionary['id']}
                            Name: {dictionary['name']}
                            Email: {dictionary['email']}
                            Gender: {dictionary['gender']}
                            Status: {dictionary['status']}"""))

    @staticmethod
    def display_active_users(how_many):
        """
        Displays the number of active users
        :param how_many: The number of users
        :return:
        """
        print(f"The first {how_many} users that are active are:\n")
        for page in range(0, how_many//20+1):
            response = RequestsApi.get_something(f'users?status=active&page={page+1}')
            if how_many >= response['meta']['pagination']['limit']:
                nr = response['meta']['pagination']['limit']
                how_many -= 20
            else:
                nr = how_many % 20
            for user in range(nr):
                User._display_user(response['data'][user])

    @staticmethod
    def display_users_middle_name(nr_users):
        """
        Displays the users thats have a middle name
        :param nr_users: how many users
        :return:
        """
        while nr_users > 0:
            page = 1
            response = RequestsApi.get_something(f"users?page={page}")
            for user in response['data']:
                if len(user['name'].split()) > 2:
                    User._display_user(user)
                    nr_users -= 1
                    if nr_users == 0:
                        break
            page += 1

    def create_post(self, json_data):
        """
        Creates a post for an user
        :param json_data: the body of the post
        :return:
        """
        json_data['user_id'] = self.user['id']
        self.post = Post(json_data)
        self.posts.append(self.post)