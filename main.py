from Defaults import defaults
from Defaults import city

from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()

from PIL import Image
import requests
from io import BytesIO

from matplotlib import pyplot as plt

import folium

import time

c1 = city.City(defaults.Tehran)
bound = c1.get_bound()
flights = fr_api.get_flights(bounds = bound)

starttime = time.time()
saver = []
while True:
    flights = fr_api.get_flights(bounds = bound)
    for counter in flights:
        if(flights != None):
            details = fr_api.get_flight_details(flights[flights.index(counter)].id)
            aircraft = details['aircraft']
            if aircraft in saver:
                continue
            else:
                saver.append(aircraft)
                print(flights[flights.index(counter)])
                flights[flights.index(counter)].set_flight_details(details)
                img = flights[flights.index(counter)].aircraft_images
                if img != None:
                    response = img['large'][0]['src']
                    response = requests.get(response)
                    img2 = Image.open(BytesIO(response.content))

                # Show the loaded image
                #img2.show()

                    plt.imshow(img2,cmap='gray')
                    plt.show()
        else:
            print("Not Yet!")
                
    # Remove the Time taken by code to execute
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
