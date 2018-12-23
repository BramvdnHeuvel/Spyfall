import sqlite3
import config
import random

groups = {}

class group:
    def __init__(self, name):
        newplayer = player(name, "none")
        self.players = {name : newplayer}
        self.locations = []

class player:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def generate_random_id(exclude):
    while(True):
        id = ""
        for i in range(6):
            random_int = random.randint(1,36)
            if(random_int <= 26):
                random_int += 96
            else:
                random_int += 21
            id += str(chr(random_int))
        if not id in exclude:
            return id

def create_group(name):
    existing_ids = groups.keys()
    id = generate_random_id(existing_ids)
    groups[id] = group(name)
    return id



