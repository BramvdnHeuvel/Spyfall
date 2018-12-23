import sqlite3
import config

class groups:
    def __init__(self):
        self.groups = {}

class group:
    def __init__(self):
        self.players = {}
        self.locations = []

class player:
    def __init__(self, name, role, leader):
        self.name = name
        self.role = role
        self.leader = leader



