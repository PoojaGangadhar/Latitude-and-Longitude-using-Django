from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = 'a219b1dbbf3c442c9b7f4c788fed3f81'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(13.3379, 77.1173)
pprint(results)
