from pygeocoder import Geocoder
import const

if __name__ == '__main__':
    gc = Geocoder(api_key=const.API_KEY)
    address = '207 N. Defiance St, Archbold, OH'
    print(gc.geocode(address)[0].coordinates)
