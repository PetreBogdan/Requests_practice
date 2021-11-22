from requestapi import RequestsApi
import textwrap
from datetime import datetime


class Todo:

    def __init__(self, todo_dict):
        self.todo = {'id': todo_dict['id'],
                     'user_id': todo_dict['user_id'],
                     'title': todo_dict['title'],
                     'due_on': Todo.format_date_in(todo_dict['due_on']),
                     'status': todo_dict['status']}

    @staticmethod
    def get_id_by_title(title):
        """
        Makes a get request and returns the id of the instance
        :param title: title of the instance
        :return: id of the instance
        """
        endpoint = f"todos?title={title}"
        response = RequestsApi.get_something(endpoint)
        return response['data'][0]['id']

    def post_todo(self):
        """
        Posts the to do
        :return:
        """
        RequestsApi.post_something(self.todo, 'todos')
        self.todo['id'] = Todo.get_id_by_title(self.todo['title'])

    def display_todo_instance(self):
        """
        Get the body from API and calls display method
        :return:
        """
        response = RequestsApi.get_something(f"todos?id={self.todo['id']}")
        Todo._display_todo(response['data'][0])

    @staticmethod
    def _display_todo(dictionary):
        """
        Formating the data for display
        :param dictionary:
        :return:
        """
        print(textwrap.dedent(f"""
                            id: {dictionary['id']}
                            User_id: {dictionary['user_id']}
                            Title: {dictionary['title']}
                            due_on: {Todo.format_date_out(dictionary['due_on'])}
                            status: {dictionary['status']}"""))

    @staticmethod
    def format_date_out(string):
        """
        Formats the date from 2021-11-28T00:00:00.000+05:30 to 28-11-2021 00:00:00 AM
        :param string: original string
        :return: formated string
        """
        dateobj = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f%z')
        dateobj = dateobj.strftime('%d-%m-%Y %I:%M:%S %p')
        return dateobj

    @staticmethod
    def format_date_in(string):
        """
        Formats the date from 28-11-2021 00:00:00 AM to 2021-11-28T00:00:00.000+05:30
        :param string: original string
        :return: formated string
        """
        dateobj = datetime.strptime(string, '%d-%m-%Y %I:%M:%S %p')
        dateobj = dateobj.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        return dateobj

    @staticmethod
    def get_todo_and_sort(how_many):
        """
        Get the list of to do items and returns them sorted by due date
        :param how_many: How many to do items
        :return: To do items sorted by due date
        """
        todos = []
        print(f"The first {how_many} users that are active are:\n")
        for page in range(0, how_many // 20 + 1):
            response = RequestsApi.get_something(f'todos?page={page + 1}')
            if how_many >= response['meta']['pagination']['limit']:
                nr = response['meta']['pagination']['limit']
                how_many -= 20
            else:
                nr = how_many % 20
            for todo in range(nr):
                # Todo._display_todo(response['data'][todo])
                todos.append(response['data'][todo])
        # return todos
        for todo in sorted(todos, key=lambda x: datetime.strptime(x['due_on'], '%Y-%m-%dT%H:%M:%S.%f%z')):
            Todo._display_todo(todo)
