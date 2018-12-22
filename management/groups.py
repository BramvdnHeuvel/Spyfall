import sqlite3
import config

class Database:
    def __init__(self):
        pass
    
    def get_users(self, group):
        return ['Bram', 'Sietse', 'Mick', 'Larissa', 'Mark', 'Sam']
    
    def add_user(self, user, group):
        pass
    
    def del_user(self, user, group):
        pass

    def group_exist(self, group):
        return False