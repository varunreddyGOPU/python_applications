# #importing package
# import phonenumbers
# #number imported form test.py file
# from test import number

# #geocoder imported for fetching the country name
# from phonenumbers import geocoder

# ch_number = phonenumbers.parse(number , "CH")
# print(geocoder.description_for_number(ch_number , "en"))

# #carrier imported for fetching the service provider name
# from phonenumbers import carrier

# service_number = phonenumbers.parse(number , "RO")
# print(carrier.name_for_number(service_number , "en"))
import phonenumbers
import folium
import requests

from test import number
from phonenumbers import geocoder

Key= '59644a070dc54f4fb5571d0b69958d09'

yugalNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(yugalNumber, "en")

print(yourLocation)

#get Service provoder

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)
result = geocoder.geocode(query)

#print(result)
lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']

print(lat,lng)
myMap = folium.Map(Location=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng],popup = yourLocation).add_to((myMap))

# lat = 37.7749
# lng = -122.4194
response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}")
address = response.json()["display_name"]
print(address)


# save map in html file

myMap.save("myLocation.html")