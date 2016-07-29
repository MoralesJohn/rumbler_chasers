
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/start'] = 'Events#start'
routes['/logout'] = 'Users#logout'
routes['POST']['/register'] = 'Users#register'
routes['/add'] = 'Locations#add'
routes['POST']['/locations/add_location'] = 'Locations#add_location'
routes['/locations/delete/<id>'] = 'Locations#delete'
routes['/locations/delete_location/<id>'] = 'Locations#delete_location'
routes['/users/edit_profile/'] = 'Users#edit_profile'
routes['POST']['/users/edit_phone'] = 'Users#edit_phone'
routes['GET']['/loc/<longitude>/<latitude>'] = 'Users#location'
