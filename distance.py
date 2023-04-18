from math import radians, cos, sin, asin, sqrt


async def distance(Longitude1, Longitude2, Breadth1, Breadth2):

    Breadth1 = radians(Breadth1)
    Breadth2 = radians(Breadth2)
    Longitude1 = radians(Longitude1)
    Longitude2 = radians(Longitude2)

    # Distance calculation using the Haversin formula
    a = sin(
        (Longitude2 - Longitude1)/ 2)**2 + cos(Longitude1) * cos(Longitude2) * sin((Breadth2 - Breadth1) / 2
                                                                                   )**2
 
    c = 2 * asin(sqrt(a))

    r = 6371	                                                                # The radius of the earth in kilometers
    
    result = round((c * r) / 2, 2)
    return(result)

# Longitude1 = 55.110485	                                                        # Longitude of the current point
# Breadth1 = 37.962350	                                                        # Latitude of the current point
# Longitude2 = 55.108175	                                                        # The longitude of the destination point
# Breadth2 = 37.975712	                                                        # Latitude of the destination point
# print(round(distance(Longitude1, Longitude2, Breadth1, Breadth2), 2), "km")