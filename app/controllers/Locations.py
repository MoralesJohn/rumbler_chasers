
from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)

        self.load_model('User')
        self.load_model('Location')
        self.load_model('Event')
        self.db = self._app.db


   
    def index(self):

        return self.load_view('index.html')

    def add(self):
        return self.load_view('add_location.html')

    def add_location(self):
        address = request.form['street'] + request.form['apt'] + request.form['city'] + request.form['state'] + request.form['zip']
        print address
        api_key = "AIzaSyC0UV-WwcSVIjZ0qqa7s5gwxyC8Yaxexpw"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            name = request.form['loc_name']
            user_id = session['id']
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            info = {'loc_name': name, 'latitude': latitude, 'longitude': longitude, 'user_id': user_id}
            self.models['Location'].add_location(info)
            return redirect('/')
        else:
            flash('Invalid address!')
            return redirect('/add')

    def delete(self, id):
        location_id = id
        location = self.models['Location'].get_location(location_id)
        print location
        return self.load_view('delete_location.html', location = location[0])

    def delete_location(self, id):
        location_id = id
        self.models['Location'].delete_location(location_id)
        return redirect('/')



