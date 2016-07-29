
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def validate(self, user_info):
     	errors = []
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        rule = re.compile(r'/^[0-9]{10,14}$/')

        query_email = 'SELECT email FROM users WHERE email =:user_email'
        value_email = { 'user_email': info['email']}
        email_check =  self.db.query_db(query_email, value_email)
        if len(email_check) !=0:
        	errors.append("Email already in use.")
        if not EMAIL_REGEX.match(info['email']):
        	errors.append('Invalid Email.')
        if not rule.seach('phone'):
        	errors.append('Invalid Phone Numbers.')
        if not str(info['nick']).isalpha():
        	errors.append("Invalid Nick Name.")
        if errors:
            return {'status': False, 'errors': errors}
        return {'status': True}
     	
    def register(self, info):
        print info
        check_query = "SELECT users.id FROM users WHERE users.fbid = :id LIMIT 1"
        check_data = {'id': info['fbid']}
        check = self.db.query_db(check_query, check_data)
        print info, "MODEL"
        if check:
            user_id = check[0]['id']
        else:    
            query = "INSERT INTO users (nick, fbid, created_at, updated_at) VALUES (:nick, :fbid, NOW(), NOW())"
            data = {'nick': info['name'], 'fbid': info['fbid']}
            user_id = self.db.query_db(query, data)
        return user_id

    def get_user(self, user_id):
        query = "SELECT users.nick, users.phone FROM users WHERE users.id = :user_id"
        data = {'user_id': user_id}
        return self.db.query_db(query, data)

    def edit_phone(self, user_id, info):
        print info
        print user_id
        query = "UPDATE users SET phone = :phone WHERE id = :user_id"
        data = {'phone': info['phone'], 'user_id': user_id}
        return self.db.query_db(query, data)