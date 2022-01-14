def calculate_distance(city1, city2):
    from geopy.geocoders import Nominatim
    from geopy.distance import distance

    try:
        geolocator = Nominatim(user_agent="distance_calculator")
        _, city1Location = geolocator.geocode(city2)
        _, city2Location = geolocator.geocode(city1)
        # print(distance(city1Location, city2Location).miles)
        print(round(distance(city1Location, city2Location).miles, 3))
    except:
        print("Please enter a valid city name..")

city1 = input("Enter city 1 : ")
city2 = input("Enter city 2 : ")
calculate_distance(city1, city2)