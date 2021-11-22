import textwrap

from requestapi import RequestsApi
from post import Post
from todo import Todo


class User:

    def __init__(self, user_dict):
        self.user = {'id': user_dict['id'],
                     'name': user_dict['name'],
                     'email': user_dict['email'],
                     'gender': user_dict['gender'],
                     'status': user_dict['status']}
        self.posts = []
        self.todos = []

    def post_user(self):
        """
        Make a post request of the instance created
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
        Displays the instance created from get
        :return:
        """
        response = RequestsApi.get_something(f"users?id={self.user['id']}")
        User._display_user(response['data'][0])

    @staticmethod
    def display_user_by_id(id_user):
        """
        Displays the data of the non created user from a get request by id
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
        Displays the users that have a middle name
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
        response = RequestsApi.patch_something(f"users/{self.user['id']}", json_data)
        if response == 200:
            self.user['email'] = email
        self.display_instance()
