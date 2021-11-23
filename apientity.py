from requestapi import RequestsApi
import textwrap


class Entity:

    @staticmethod
    def display_entity(dictionary):
        for key in dictionary.keys():
            print(f"{key}: {dictionary[key]}")
        print()

    @staticmethod
    def get_list_of_entities(how_many, url):
        entity_list = []
        for page in range(0, how_many // 20 + 1):
            response = RequestsApi.get_request(f'{url}{page + 1}')
            if how_many >= response['meta']['pagination']['limit']:
                nr = response['meta']['pagination']['limit']
                how_many -= 20
            else:
                nr = how_many % 20
            for entity in range(nr):
                entity_list.append(response['data'][entity])
        return entity_list

    @staticmethod
    def display_entity_by_id(entity, id_entity):
        response = RequestsApi.get_request(f"{entity}?id={id_entity}")
        Entity.display_entity(response['data'][0])
