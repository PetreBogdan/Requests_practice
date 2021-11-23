import requests


class RequestsApi:

    with open('Authorization Token', 'r') as file:
        token = file.read()
    headers = {'Authorization': f'Bearer {token}'}

    @staticmethod
    def get_request(endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.get(url, verify=False, headers=RequestsApi.headers)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def post_request(data, endpoint): #todo rename
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.post(url, data=data, verify=False, headers=RequestsApi.headers)
        response.raise_for_status()

    @staticmethod
    def delete_request(endpoint):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.delete(url, verify=False, headers=RequestsApi.headers)
        response.raise_for_status()

    @staticmethod
    def patch_request(endpoint, data):
        url = f"https://gorest.co.in/public/v1/{endpoint}"
        response = requests.patch(url, data=data, verify=False, headers=RequestsApi.headers)
        response.raise_for_status()
