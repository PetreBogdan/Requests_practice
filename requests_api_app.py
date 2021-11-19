import pprint
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
    # User.display_user_from_get(500)
    # User.display_active_users(20)
    # User.display_users_middle_name(10)
    print(User.number_of_users())
