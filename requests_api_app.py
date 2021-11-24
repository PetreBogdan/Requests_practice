import pprint
from requestapi import RequestsApi
from user import User
from post import Post
from todo import Todo

if __name__ == '__main__':

    # Create user
    user_dict = {'id': '500', 'name': 'bodi',
                 'email': 'AppTest@test.com', 'gender': 'male',
                 'status': 'active'}
    user1 = User(user_dict)
    user1.display_user()
    user1.modify_email('AppTest2@test.com')
    user1.display_user()

    todo_data = {"id": 4, "user_id": 4,
                 "title": "AppTodo",
                 "due_on": "13-06-2021 5:43:02 PM",
                 "status": "pending"}

    user1.create_todo(todo_data)
    user1.todo.display_todo()

    # comment_dict = {"id": 1, "post_id": 2, "name": "AppTest2",
    #                 "email": "AppTest2@test.com",
    #                 "body": "Test"}

    # post_dict = {"id": 1325, "user_id": 214, "title": "Test", "body": "TestTestTest"}

    user1.delete_user()
