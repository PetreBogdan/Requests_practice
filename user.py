import textwrap
from apientity import Entity
from requestapi import RequestsApi
from post import Post
from todo import Todo


class User(Entity):

    def __init__(self, user_dict):
        try:
            self.user = {'id': user_dict['id'],
                         'name': user_dict['name'],
                         'email': user_dict['email'],
                         'gender': user_dict['gender'],
                         'status': user_dict['status']}
        finally:
            RequestsApi.post_request(user_dict, 'users')
            self.update_user()
            self.posts = []
            self.todos = []

    def update_user(self):
        endpoint = f"users?name={self.user['name']}"
        response = RequestsApi.get_request(endpoint)
        self.user['id'] = response['data'][0]['id']
        self.user['name'] = response['data'][0]['name']
        self.user['email'] = response['data'][0]['email']
        self.user['gender'] = response['data'][0]['gender']
        self.user['status'] = response['data'][0]['status']

    @staticmethod
    def get_id_by_name(name):
        """
        Makes a get request and returns the id of the instance
        :param name: name of the instance
        :return: id of the instance
        """
        endpoint = f"users?name={name}"
        response = RequestsApi.get_request(endpoint)
        return response['data'][0]['id']

    @staticmethod
    def number_of_users():
        """
        Returns the number of users from the API
        :return: the number of users
        """
        response = RequestsApi.get_request('users')
        return response['meta']['pagination']['total']

    def display_user(self):
        """
        Displays the instance created from get
        :return:
        """
        response = RequestsApi.get_request(f"users?id={self.user['id']}")
        User.display_entity(response['data'][0])

    @staticmethod
    def display_active_users(how_many):
        """
        Displays the number of active users
        :param how_many: The number of users
        :return:
        """
        url = 'users?status=active&page='
        list_users = User.get_list_of_entities(how_many, url)
        for user in list_users:
            User.display_entity(user)

    @staticmethod
    def display_users_middle_name(nr_users):
        """
        Displays the users that have a middle name
        :param nr_users: how many users
        :return:
        """
        while nr_users > 0:
            page = 1
            response = RequestsApi.get_request(f"users?page={page}")
            for user in response['data']:
                if len(user['name'].split()) > 2:
                    User.display_entity(user)
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

    def create_todo(self, json_data):
        """
        Creates a to do for an user
        :param json_data: the body of the to do
        :return:
        """
        json_data['user_id'] = self.user['id']
        self.todo = Todo(json_data)
        self.todos.append(self.todo)

    def modify_email(self, email):
        """
        Changes the email of an user with a patch request
        :param email: the email modified
        :return: Display the data with the modified email
        """
        json_data = {'email': email}
        RequestsApi.patch_request(f"users/{self.user['id']}", json_data)
        self.user['email'] = email
        self.update_user()

    @staticmethod
    def display_user_by_id(id_user):
        User.display_entity_by_id("users", id_user)

    def delete_user(self):
        RequestsApi.delete_request(f"users/{self.user['id']}")

