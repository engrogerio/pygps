import math

class coordinate:
    
    def __init__(self, latitude: float, longitude: float)
        self.latitude = latitude
        self.longitude = longitude


PI = math.pi
TWOPI = 2*PI
lat_array = []
long_array = []
    
""" This is the polygon bounding box, if you plot it, 
    you'll notice it is a rough tracing of the parameter of 
    the state of Florida starting at the upper left, moving 
    clockwise, and finishing at the upper left corner of florida.
"""

def get_poligon_sample(self):
    polygon_lat_long_pairs = []
    polygon_lat_long_pairs.append(coordinate(31.000213, -87.584839))  
    # lat/long of upper left tip of florida.
    polygon_lat_long_pairs.append(coordinate(31.009629, -85.003052))
    polygon_lat_long_pairs.append(coordinate(30.726726, -84.838257))
    polygon_lat_long_pairs.append(coordinate(30.584962, -82.168579))
    polygon_lat_long_pairs.append(coordinate(30.73617, -81.476441)) 
    # lat/long of upper right tip of florida.
    polygon_lat_long_pairs.append(coordinate(29.002375, -80.795288))
    polygon_lat_long_pairs.append(coordinate(26.896598, -79.938355))
    polygon_lat_long_pairs.append(coordinate(25.813738, -80.059204))
    polygon_lat_long_pairs.append(coordinate(24.93028, -80.454712))
    polygon_lat_long_pairs.append(coordinate(24.401135, -81.817017))
    polygon_lat_long_pairs.append(coordinate(24.700927, -81.959839))
    polygon_lat_long_pairs.append(coordinate(24.950203, -81.124878))
    polygon_lat_long_pairs.append(coordinate(26.0015, -82.014771))
    polygon_lat_long_pairs.append(coordinate(27.833247, -83.014527))
    polygon_lat_long_pairs.append(coordinate(28.8389, -82.871704))
    polygon_lat_long_pairs.append(coordinate(29.987293, -84.091187))
    polygon_lat_long_pairs.append(coordinate(29.539053, -85.134888))
    polygon_lat_long_pairs.append(coordinate(30.272352, -86.47522))
    polygon_lat_long_pairs.append(coordinate(30.281839, -87.628784))
    return polygon_lat_long_pairs

assert test_point_is_inside_polygon(25.7814014, -80.186969,
        lat_array, long_array))

assert False = coordinate_is_inside_polygon(25.831538, -1.069338,
        lat_array, long_array))

def get_angle(point1_lat, point1_lgt, lat1, lgt1, lat1, lgt1):

def  coordinate_is_inside_polygon(lat: float, lgt: float, polygon: list):

    n = len(polygon)
    for i in range(0, n-1):
        point1_lat = polygon[i].latitude - lat
        point1_long = polygon[i].longitude - lgt
        point2_lat = polygon[(i+1)%n] - lat
        point2_long = polygon[(i+1)%n] - lgt
        angle = angle + get_angle(lat, lgt, polygon[i].latitude, polygon[i].longitude, polygon[i+1].latitude, polygon[i+1].longitude)


   if (Math.abs(angle) < PI)
      return false;
   else
      return true;
}

def angle2d(y1: float, x1: float, y2: float, x2: float):

   theta1 = math.atan2(y1,x1)
   theta2 = math.atan2(y2,x2);
   dtheta = theta2 - theta1;
   while (dtheta > PI)
      dtheta -= TWOPI;
   while (dtheta < -PI)
      dtheta += TWOPI;

   return(dtheta);
}

public static boolean is_valid_gps_coordinate(double latitude, 
    double longitude)
{
    //This is a bonus function, it's unused, to reject invalid lat/longs.
    if (latitude > -90 && latitude < 90 && 
            longitude > -180 && longitude < 180)
    {
        return true;
    }
    return false;
}
}
