# Install package via pip: pip install geopy
#

from geopy.geocoders import Nominatim
import sys

geolocator = Nominatim()
location = geolocator.geocode("marion county Oregon")
print(location.latitude, location.longitude)
