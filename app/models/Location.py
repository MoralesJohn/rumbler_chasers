
from system.core.model import Model

class Location(Model):
    def __init__(self):
        super(Location, self).__init__()


    def get_all(self):
    	return self.db.query_db("SELECT locations.loc_name, locations.longitude, locations.latitude, users.phone FROM locations LEFT JOIN users ON locations.user_id = users.id")

    def add_location(self, info):
    	query = "INSERT INTO locations (loc_name, longitude, latitude, created_at, updated_at, user_id) VALUES (:loc_name, :longitude, :latitude, NOW(), NOW(), :user_id)"
    	data = {'loc_name': info['loc_name'], 'longitude': info['longitude'], 'latitude': info['latitude'], 'user_id': info['user_id']}
    	return self.db.query_db(query, data)

    def get_user_locations(self, user_id):
    	query = "SELECT DISTINCT locations.id, locations.loc_name, locations.longitude, locations.latitude FROM locations LEFT JOIN users ON locations.user_id = :user_id WHERE users.id = :user_id"
    	data = {"user_id": user_id}
    	return self.db.query_db(query, data)

    def get_location(self, location_id):
    	query = "SELECT locations.id, locations.loc_name, locations.longitude, locations.latitude FROM locations WHERE locations.id = :location_id"
    	data = {'location_id': location_id}
    	return self.db.query_db(query, data)

    def delete_location(self, location_id):
    	query = "DELETE FROM locations WHERE locations.id = :location_id"
    	data = {'location_id': location_id}
    	return self.db.query_db(query, data)