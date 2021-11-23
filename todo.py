from requestapi import RequestsApi
import textwrap
from datetime import datetime
from apientity import Entity


class Todo(Entity):

    def __init__(self, todo_dict):
        try:
            self.todo = {'id': todo_dict['id'],
                         'user_id': todo_dict['user_id'],
                         'title': todo_dict['title'],
                         'due_on': Todo.format_date_in(todo_dict['due_on']),
                         'status': todo_dict['status']}
        finally:
            RequestsApi.post_request(todo_dict, 'posts')
            self.update_todo()

    def update_todo(self):
        endpoint = f"todo?title={self.todo['title']}"
        response = RequestsApi.get_request(endpoint)
        self.todo['id'] = response['data'][0]['id']
        self.todo['user_id'] = response['data'][0]['user_id']
        self.todo['title'] = response['data'][0]['title']
        self.todo['due_on'] = response['data'][0]['due_on']
        self.todo['status'] = response['data'][0]['status']

    def display_todo(self):
        """
        Get the body from API and calls display method
        :return:
        """
        response = RequestsApi.get_request(f"todos?id={self.todo['id']}")
        Todo.display_entity(response['data'][0])

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
    def get_todo_sorted_list(how_many):
        """
        Get the list of to do items and returns them sorted by due date
        :param how_many: How many to do items
        :return: To do items sorted by due date
        """
        url = 'todos?page='
        todos = Todo.get_list_of_entities(how_many, url)
        for todo in sorted(todos, key=lambda x: datetime.strptime(x['due_on'], '%Y-%m-%dT%H:%M:%S.%f%z')):
            Todo.display_entity(todo)

    @staticmethod
    def display_todo_by_id(todo_id):
        Todo.display_entity_by_id("todos", todo_id)
