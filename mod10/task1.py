import requests
import json


def get_swapi_data(url):
    response = requests.get(url)
    return response.json()


def get_planet_info(planet_url):
    planet_data = get_swapi_data(planet_url)
    return {
        'name': planet_data['name'],
        'url': planet_url
    }


def get_millennium_falcon_info():
    base_url = 'https://swapi.dev/api'
    starships_url = f'{base_url}/starships'

    response = requests.get(starships_url, params={'search': 'Millennium Falcon'})
    data = response.json()

    if data['count'] == 0:
        print("Корабль Millennium Falcon не найден")
        return

    falcon_data = data['results'][0]
    pilots_info = []
    for pilot_url in falcon_data['pilots']:
        pilot_data = get_swapi_data(pilot_url)
        planet_info = get_planet_info(pilot_data['homeworld'])
        pilot_info = {
            'имя': pilot_data['name'],
            'рост': pilot_data['height'],
            'вес': pilot_data['mass'],
            'родная планета': planet_info['name'],
            'ссылка на информацию о родной планете': planet_info['url']
        }
        pilots_info.append(pilot_info)

    millennium_falcon_info = {
        'название': falcon_data['name'],
        'максимальная скорость': falcon_data['max_atmosphering_speed'],
        'класс': falcon_data['starship_class'],
        'список пилотов': pilots_info
    }

    return millennium_falcon_info


def main():
    millennium_falcon_info = get_millennium_falcon_info()

    if millennium_falcon_info:
        print(json.dumps(millennium_falcon_info, ensure_ascii=False, indent=4))
        with open('millennium_falcon_info.json', 'w', encoding='utf-8') as file:
            json.dump(millennium_falcon_info, file, ensure_ascii=False, indent=4)
    else:
        print("Информация о Millennium Falcon не найдена.")


if __name__ == "__main__":
    main()
