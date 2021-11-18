import requests
import pprint


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

    @staticmethod
    def number_of_users(endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.get(url, verify=False, headers=RequestsApi.headers)
        return response.json()['meta']['pagination']['total']


if __name__ == '__main__':

    response_app = RequestsApi.get_something('users')
    pprint.pprint(response_app)
    # print(response)
    # print(RequestsApi.number_of_users())
    json_data = {'email': 'ApiAppTest2@gmail.com',
                 'gender': 'male', 'id': 1523, 'name': 'ApiAppTest',
                 'status': 'active'}
    # RequestsApi.post_something(json_data,'users')
    # RequestsApi.delete_something('users/2122')
    # print(RequestsApi.number_of_users())
