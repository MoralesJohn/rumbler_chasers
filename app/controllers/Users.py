
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.load_model('Location')
        self.load_model('Event')
        self.db = self._app.db


   
    def index(self):
        latitude = 20
        longitude = 0
        zoom = 2
        if 'id' in session:
            user_id = session['id']
            info = self.models['User'].get_user(user_id)
            user_locations = self.models['Location'].get_user_locations(user_id)
            return self.load_view('dashboard.html', user_locations = user_locations, info = info[0], dash_longitude = longitude, dash_latitude = latitude, dash_zoom = zoom, user_id=user_id)
        return self.load_view('index.html')

    def register(self):
        info = {
				'name': request.form['nick'],
				'fbid': request.form['fbid']
        }
        session['id'] = self.models['User'].register(info)
        return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')

    def edit_profile(self):
        user_id = session['id']
        user = self.models['User'].get_user(user_id)
        return self.load_view('edit_profile.html', user = user[0])

    def edit_phone(self):
        user_id = session['id']
        info = request.form
        print user_id, "******"
        print info
        self.models['User'].edit_phone(user_id, info)
        return redirect('/')

    def location(self, latitude = 0, longitude = 0):
        if longitude == 0 and latitude == 0:
            zoom = 2
        else:
            zoom = 10
        if 'id' in session:
            user_id = session['id']
            info = self.models['User'].get_user(user_id)
            user_locations = self.models['Location'].get_user_locations(user_id)
        return self.load_view('dashboard.html', user_locations = user_locations, info = info[0], dash_longitude = longitude, dash_latitude = latitude, dash_zoom = zoom, user_id = user_id)
