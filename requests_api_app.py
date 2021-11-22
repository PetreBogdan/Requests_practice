import pprint
from requestapi import RequestsApi
from user import User
from post import Post
from todo import Todo


if __name__ == '__main__':

    # Creating an user
    user_dict = {'id': '500', 'name': 'bodi',
                 'email': 'AppTest@test.com', 'gender': 'male',
                 'status': 'active'}
    user1 = User(user_dict)
    user1.post_user()

    user1.display_instance()
    # User.display_active_users(20)
    # User.display_users_middle_name(10)
    # print(User.number_of_users())
    user1.display_instance()

    # Modifying email
    user1.modify_email('AppTestPatched@test.com')

    # Creating a post for an user
    post_dict = {"id": 1325, "user_id": 214, "title": "Test", "body": "TestTestTest"}
    user1.create_post(post_dict)
    user1.post.post_post()
    # print(user1.post.get_id_by_title('Test'))
    user1.post.display_post()

    # Creating a comment for an user
    comment_dict = {"id": 1, "post_id": 2, "name": "AppTest2",
                    "email": "AppTest2@test.com",
                    "body": "Test"}
    user1.post.create_comment(comment_dict)
    user1.post.comment.post_comment()
    user1.post.comment.display_comment()

    # Creating a to do for an user
    todo_data = {"id": 4, "user_id": 4,
                 "title": "AppTodo",
                 "due_on": "13-06-2021 5:43:02 PM",
                 "status": "pending"}
    user1.create_todo(todo_data)
    user1.todo.post_todo()
    user1.todo.display_todo_instance()

    # Todo.get_todo_and_sort(8)
