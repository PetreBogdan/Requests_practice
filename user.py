import pprint
import textwrap

from requestapi import RequestsApi


class User:

    def __init__(self, user_dict):
        self.user = {'id': user_dict['id'],
                     'name': user_dict['name'],
                     'email': user_dict['email'],
                     'gender': user_dict['gender'],
                     'status': user_dict['status']}

    # Creating a new user
    def post_user(self):
        RequestsApi.post_something(self.user, 'users')
        self.user['id'] = User.get_id_by(self.user['name'])

    # Searching for a specific user by name and returns ID
    @staticmethod
    def get_id_by(name):
        endpoint = f"users?name={name}"
        response = RequestsApi.get_something(endpoint)
        return response['data'][0]['id']

    def display_instance(self):
        for key in self.user.keys():
            print(f"Key: {key} Value: {self.user[key]}\n")

    # Returns number of users to verify the new added user
    @staticmethod
    def number_of_users():
        response = RequestsApi.get_something('users')
        return response['meta']['pagination']['total']

    # @staticmethod
    # def get_something_by_name(name):
    #     url = f"https://gorest.co.in/public/v1/users?name={name}"
    #     response = requests.get(url, verify=False, headers=RequestsApi.headers)
    #     print(f"Request response: {response.status_code}")
    #     return response.json()['data'][0]['id']

    def display_user_created(self):
        response = RequestsApi.get_something(f"users?id={self.user['id']}")
        print(textwrap.dedent(f"""
                            id of the user: {response['data'][0]['id']}
                            Name: {response['data'][0]['name']}
                            Email: {response['data'][0]['email']}
                            Gender: {response['data'][0]['gender']}
                            Status: {response['data'][0]['status']}"""))

    @staticmethod
    def display_user(id_user):
        response = RequestsApi.get_something(f"users?id={id_user}")
        print(textwrap.dedent(f"""
                            id of the user: {response['data'][0]['id']}
                            Name: {response['data'][0]['name']}
                            Email: {response['data'][0]['email']}
                            Gender: {response['data'][0]['gender']}
                            Status: {response['data'][0]['status']}"""))
