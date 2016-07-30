# Rumbler Chasers
Group project in Python using the Pylot MVC to allow people to register with the site, add locations they care about, and see earthquake activity near those locations. Planned additions include text notifications within minutes of activity. 

The project uses the Facebook Oauth API, the Google Maps API, and GeoJSON data from www.usgs.com. Written by Mike Lee, John Morales, Adi Surya and Nate Watkins, this project won the July 2016 Python Hackathon at the Coding Dojo in San Jose, CA. 

# Installation
You will need a Facebook developer key for the Oauth registration. Also, a Google Maps API key to enable map calls. Look for KEEE in the index.html and dashboard.html files. 

#Configure the Pylot MVC environment 
Start by deleting the pylotVenv directory, if it exists. Then run 
'''
python setup.py
'''

Follow the instructions on screen. You will need to run this twice the first time, followed by:
'''
python manage.py runserver
'''

# Database
The SQL file is included in the root of the repository. You may also need to reconfigure the database settings for your system. The setting are contained in /app/config/databse.py and should be well documented. 
