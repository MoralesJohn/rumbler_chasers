from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def get_coordinate(self):
        address = request.form['street'] + request.form['apt'] + request.form['city'] + request.form['state'] + request.form['zip']
        print address
        api_key = "GOOGLE MAP API KEY"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        if api_response_dict['status'] == 'OK':
            latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            print 'Latitude:', latitude
            print 'Longitude:', longitude
            return redirect('/')
        else:
            flash('Invalid address!')
            return redirect('/')
