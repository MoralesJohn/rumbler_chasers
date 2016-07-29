from system.core.controller import *
import time, requests
from math import *

class Events(Controller):
    def __init__(self, action):
        super(Events, self).__init__(action)

        self.load_model('User')
        self.load_model('Location')
        self.load_model('Event')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def start(self):
        now = time.time()
        alarms = []
        HOUR = 3600000
        events = self.models['Event']. pull_items()
        for each in events:
            if (now - each['event_time']) > HOUR:
                self.models['Event'].past_events(each)

        quake_data = request.get('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson')
        quake_data = quake_data.json()
        new_events = quake_data['features']
        past_events = self.models['Event'].past_events()
        for new_event in new_events:
            if new_event['properties']['title'] not in past_events:
                long_coord = new_event['geometry']['coordinates'][0]
                lat_coord = new_event['geometry']['coordinates'][1]
                mag = new_event['properties']['mag']
                title = new_event['properties']['title']
                self.models['Event'].new_event(lat_coord, long_coord, mag, title, event_time)
                for locale in locations:
                    long1 = locale['longitude']
                    lat1 = locale['latitude']
                    long2 = long_coord
                    lat2 = lat_coord
                    if abs(long1-long2) > 180:
                        if long1 < long2:
                            long1 += 360
                        else:
                            long2 += 360
                    long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
                    dlong = long2 - long1
                    dlat = lat2 - lat1
                    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
                    c = 2 * asin(sqrt(a))
                    r = 3956
                    distance = c * r
                    if distance < 100:
                        alarms.push({'phone': locale['phone'], 'message': 'From RumblerChasers: ' + distance + ' miles from ' + locale['loc_name'] + '. ' + new_event['properties']['title']})
        return redirect('/')