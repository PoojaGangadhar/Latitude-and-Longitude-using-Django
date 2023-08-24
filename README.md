# Latitude-and-Longitude-using-Django
Django Rest Framework application to fetch the latitude and longitude of a place entered by user. \n
The latitude and longitude of a place is fetched using the Opencage Geocoding API\n
https://opencagedata.com/ \n
After signing up a 30 charcter long alphanumeric string is assigned as your API Key, which is necessary for obtaining the latitude and longitude \n
An example of reverse geocoding (getting the place by passing latitude and longitude values)\n

from opencage.geocoder import OpenCageGeocode <br>
from pprint import pprint <br>

key = // provide your API key withing '' <br>
geocoder = OpenCageGeocode(key) <br>

results = geocoder.reverse_geocode(13.3379, 77.1173) <br>
pprint(results) <br>

Url to run django application: <br>
http://127.0.0.1:8000/api/
