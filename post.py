from requestapi import RequestsApi


class Post:

    # Create a post for a user
    @staticmethod
    def post_user_post():
        json_dummy = {"id": 'id', "user_id": "user_id",
                      "title": "title",
                      "body": "body"}
        for key in json_dummy.keys():
            match key:
                case 'id':
                    json_dummy['id'] = input('Enter id of the post: ')
                case 'user_id':
                    json_dummy['user_id'] = input('Enter the id of the user: ')
                case 'title':
                    json_dummy['title'] = input('Enter the title of the post: ')
                case 'body':
                    json_dummy['body'] = input('Enter your story: ')
        RequestsApi.post_something(json_dummy, 'posts')