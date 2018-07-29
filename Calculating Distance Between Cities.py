#To calculate Distance between cities:-
 
         import requests

        GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

        params = {
            'address': 'Ambrosia, Oracle Park, Mulshi Rd, Bavdhan, Pune',
            'sensor': 'false',
            'region': 'india'
                }
                # Do the request and get the response data
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()

        # Use the first result
        result = res['results'][0]

        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']

        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
        Latitue1=geodata['lat']
        Longitude1=geodata['lng']
        print(Latitue1)
        print(Longitude1)
        
       
	   
        import requests

        GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

        params = {
            'address': 'Bhunde Vasti, Bavdhan, Pune, Maharashtra',
            'sensor': 'false',
            'region': 'india'
                }
                # Do the request and get the response data
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()

        # Use the first result
        result = res['results'][0]

        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']

        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
        Latitue2=geodata['lat']
        Longitude2=geodata['lng']
        print(Latitue2)
        print(Longitude2)
		
		
		
	from math import sin, cos, sqrt, atan2,radians	
        R = 6373.0
        lat1=radians(Latitue1)
        lat2=radians(Latitue2)
        lon1=radians(Longitude1)
        lon2=radians(Longitude2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        #a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        #c = 2 * atan2(sqrt(a), sqrt(1-a))
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        distance = R * c
        
        print(distance)