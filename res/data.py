import random

groups = {}

standard_locations = ['Airplane', 'Bank', 'Beach', 'Circus Tent', 'Crusader Army', 'Day Spa', 'Embassy']

class Group:
    def __init__(self, name, locations=standard_locations):
        newplayer = Player(name)

        self.players = {name : newplayer}
        self.locations = locations
        self.started = False

class Player:
    def __init__(self, name, role="none"):
        self.name = name
        self.role = role
    
    def __repr__(self):
        return f'<Player {self.name} ({self.role})>'

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
        if not id in groups:
            return id

def create_group(name):
    existing_ids = groups.keys()
    id = generate_random_id(existing_ids)
    groups[id] = Group(name)
    return id

def joingroup(group,name):
    information = {"successful" : False, "players" : [], "error" : ""}

    if group in groups:
        if name in groups[group].players:
            information["error"] = "Name already occupied."

        else:
            new_player = Player(name, "none")
            groups[group].players[name] = new_player
            lijst = list(groups[group].players.keys())

            information["successful"] = True
            information["players"] = lijst
    
    else:
        information["error"] = "Unknown group."

    return information




