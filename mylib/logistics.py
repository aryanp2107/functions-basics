"""
This module deals with distance and calculates distances between two points 
on the Earth using the Haversine formula.
The Haversine formula is an equation that gives the distance between two points
It also calculates the distance between two points using the geopy library, which provides

"""

import geopy

# build a list of 10 cities with their latitude and longitude

cities = [
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"name": "Chicago", "lat": 41.8781, "lon": -87.6298},
    {"name": "Houston", "lat": 29.7604, "lon": -95.3698},
    {"name": "Phoenix", "lat": 33.4484, "lon": -112.0740},
    {"name": "Philadelphia", "lat": 39.9526, "lon": -75.1652},
    {"name": "San Antonio", "lat": 29.4241, "lon": -98.4936},
    {"name": "San Diego", "lat": 32.7157, "lon": -117.1611},
    {"name": "Dallas", "lat": 32.7767, "lon": -96.7970},
    {"name": "San Jose", "lat": 37.3382, "lon": -121.8863},
]

# build a function to calculate the distance between two points using the Haversine formula
def distance(city1, city2):
    """Calculate the distance between two cities using the Haversine formula."""
    from math import radians, sin, cos, sqrt, atan2

    # convert latitude and longitude from degrees to radians
    lat1 = radians(city1["lat"])
    lon1 = radians(city1["lon"])
    lat2 = radians(city2["lat"])
    lon2 = radians(city2["lon"])

    # haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers

    return distance


# build a function to calculate the time it takes to travel between two cities at a given speed
def travel_time(city1, city2, speed):
    """Calculate the time it takes to travel between two cities at a given speed."""
    distance = distance(city1, city2)
    time = distance / speed  # time = distance / speed
    return time
