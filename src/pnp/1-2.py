import requests
import const


def geocode(address):
    parameters = {'address': address,
                  'sensor': 'false',
                  'key': const.API_KEY
                  }
    base = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
