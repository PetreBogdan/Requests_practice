from requestapi import RequestsApi
import textwrap


class Todo:

    def __init__(self, todo_dict):
        self.todo = {'id': todo_dict['id'],
                     'user_id': todo_dict['user_id'],
                     'title': todo_dict['title'],
                     'due_on': todo_dict['due_on'],
                     'status': todo_dict['status']}
