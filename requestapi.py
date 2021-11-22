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

    @staticmethod
    def patch_something(endpoint, data):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.patch(url, data=data, verify=False, headers=RequestsApi.headers)
        print(f"Request response: {response.status_code}")
        return response.status_code
