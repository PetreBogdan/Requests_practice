import requests


class RequestsApi:

    with open('Authorization Token', 'r') as file:
        token = file.read()
    headers = {'Authorization': f'Bearer {token}'}

    @staticmethod
    def get_something(endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.get(url, verify=False, headers=RequestsApi.headers)
        print(f"Request response: {response.status_code}")
        return response.json()

    @staticmethod
    def post_something(data, endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.post(url, data=data, verify=False, headers=RequestsApi.headers)
        print(f"Request response: {response.status_code}")

    @staticmethod
    def delete_something(endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.delete(url, verify=False, headers=RequestsApi.headers)
        print(f"Request response: {response.status_code}")

    #Create a to do for a user
    @staticmethod
    def post_todo_user():
        json_dummy = {"id": 'id', "user_id": 'user_id',
                      "title": 'title',
                      "due_on": "2021-12-07T00:00:00.000+05:30",
                      "status": "pending"}