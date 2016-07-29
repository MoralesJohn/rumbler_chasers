from system.core.model import Model

class Event(Model):
    def __init__(self):
        super(Event, self).__init__()

    def pull_items(self):
    	return self.db.query_db("SELECT quakes.id, quakes.created_at FROM quakes")

    def clear_event(self, each):
    	query = "DELETE FROM quakes WHERE id = :id"
    	data = {'id': each['id']}
    	return self.db.query_db(query, data)

   	def new_event(self, lat_coord, long_coord, mag, title, event_time):
   		query = "INSERT INTO quakes (title, latitude, longitude, magnitude, event_time, created_at, updated_at) VALUES (:title, :lat, :long, :mag, :event_time, NOW(), NOW())"
   		data = {'title': title, 'lat': lat_coord, 'long': long_coord, 'mag': mag, 'event_time': event_time}
   		return self.db.query_db(query, data)

   	def past_events(self):
   		dicty = self.db.query_db("SELECT quakes.title FROM quakes")
   		arr = []
   		for item in dicty:
   			arr.push(item['title'])
   		return arr