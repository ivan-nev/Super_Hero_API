import requests

# from pprint import pprint
list_hero = ['Hulk', 'Captain America', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/"


def get_intelligence(name):
    resp = requests.get(f'{url}/search/{name}')
    if resp.json()['response'] == 'success':
        return int(resp.json()['results'][0]['powerstats']['intelligence'])
    else:
        return 0


def dict_heroes(heroes):
    # dict_hero = {}
    # for hero in heroes:
    #     intelligence = get_intelligence(hero)
    #     if intelligence:
    #         dict_hero[hero] = int(intelligence)
    return {name: get_intelligence(name) for name in heroes}


heroes_intelligence = dict_heroes(list_hero)
print(heroes_intelligence)
print(max(heroes_intelligence, key=heroes_intelligence.get))
