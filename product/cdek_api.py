import requests
import json

def get_region():
    url_region = 'https://api.cdek.ru/v2/location/regions?country_codes=RU'  # api которая выдает список всех регионов
    # Вместо RU можем передать другие странны
    result = requests.get(url_region, headers=register_api())  # отправляем get запрос на получение всех регионов
    result_region = result.json()  # результат: {'country_code': 'RU', 'region': 'Воронежская обл.', 'region_code': 63, 'country': 'Россия'}

    region = {x['region']: x['region_code'] for x in result_region}
    # выбираем конкретно регион, для показа пользователю , и код региона для последущего запроса города доставки
    return region


def get_cities(region_code):  # принимаем код региона, который выбрал пользователь

    url_cities = 'https://api.cdek.ru/v2/location/cities?region_code={}'.format(region_code)

    result = requests.get(url_cities, headers=register_api())

    result_cities = result.json()

    cities = {x['city']: x['code'] for x in
              result_cities}  # получаем все города , и коды городов для дальнейшего расчета
    return cities


def get_cost_delivery(city_code,weight,length,width,height):

    data = {
        'currency': 1,
        'tariff_code':11,
        'from_location': {'code': 278}, # код Красноярска
        'to_location': {'code': city_code},
        'packages':[
            {'weight':weight,
             'length':length,
             'width':width,
             'height':height}
        ]
    }
    data_json = json.dumps(data)
    result = requests.post('https://api.cdek.ru/v2/calculator/tariff', headers=register_api(), data=data_json)
    return result.json()

def register_api():
    get_token = requests.post(url='https://api.edu.cdek.ru/v2/oauth/token?parameters',
                              # регистрируемся cdek api и получаем токен
                              data={'grant_type': 'client_credentials',
                                    'client_id': 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI'
                                  , 'client_secret': 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'})

    access_token = get_token.json()['access_token']  # выбираем сам токен

    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(access_token)}
    return headers
