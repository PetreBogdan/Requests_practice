from requestapi import RequestsApi
from user import User
from post import Post


if __name__ == '__main__':

    # user_dict = {'id':'500', 'name': 'AppTest',
    #              'email':'AppTest@test.com', 'gender': 'male',
    #              'status': 'active'}
    # user1 = User(user_dict)
    # user1.post_user()
    # user1.display_user()
    # print(User.search_by_name('AppTest'))
    # user1.display_instance()
    # User.display_user(29)
    print(User.number_of_users())