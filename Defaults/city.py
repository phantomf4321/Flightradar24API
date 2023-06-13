from matplotlib import pyplot as plt
import folium


from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()

class City:
    def __init__(city, data):
            CIAO = data[0]
            city.bound = data[1]
            city.name = data[2]
            
            city.ciao = []
            city.airport_name = []
            city.airport_coordinate = []
            
            city.city_bound = []
            
            for airport_counter in CIAO:
                curr_ciao = CIAO[CIAO.index(airport_counter)]
                city.ciao.append(curr_ciao)
                
                curr_airport = fr_api.get_airport(curr_ciao)
                city.airport_name.append(curr_airport['name'])
                
                curr_coordinate = [curr_airport['position']['latitude'], curr_airport['position']['longitude']]
                city.airport_coordinate.append(curr_coordinate)
                
                
                
                
                
    def printer(city):
        print("Welcome to ", city.name, sep="")
        print("Bound ", city.bound, " is under observation!", sep="")
        print("Airports within the range:")
        for airport_counter in city.ciao:
            print("   ", city.airport_name[city.ciao.index(airport_counter)], "/", city.ciao[city.ciao.index(airport_counter)], sep="")
            print("   Located on: ", city.airport_coordinate[city.ciao.index(airport_counter)], sep="")
