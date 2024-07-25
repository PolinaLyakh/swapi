import requests
from pathlib import Path


class APIRequester:

    def __init__(self, url=''):
        self.base_url = url

    def get(self, url):
        try:
            response = requests.get(self.base_url + url)
            response.raise_for_status()
            return response
        except requests.HTTPError:
            print('Сервер не отвечает. Воспользуйтесь зеркалами')
        except requests.RequestException:
            print('Возникла ошибка при выполнении запроса')


class SWRequester(APIRequester):

    def get_sw_categories(self, url='/'):
        response = self.get(url)
        resp_dict = response.json()
        resp_list = resp_dict.keys()
        return resp_list

    def get_sw_info(self, sw_type: str):
        item = '/' + sw_type + '/'
        response = self.get(item)
        return response.text


def save_sw_data():
    url = 'https://swapi.dev/api'
    swr_obj = SWRequester(url)
    Path("data").mkdir(exist_ok=True)    # ~/Dev/SWAPI/data
    category_list = swr_obj.get_sw_categories()
    for item in category_list:
        with open(f'data/{item}.txt', 'w', encoding='utf-8') as f:
            f.write(swr_obj.get_sw_info(item))


# url = 'https://swapi.dev/api'    # базовый url
# url_mirror = 'https://swapi.dev/api'
# url_mirror_2 = 'https://swapi.dev/api'
save_sw_data()
