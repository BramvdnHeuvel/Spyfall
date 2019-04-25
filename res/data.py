import random

groups = {}

standard_locations = ['Airplane', 'Bank', 'Beach', 'Circus Tent', 'Crusader Army', 'Day Spa', 'Embassy']

class Group:
    def __init__(self, name, locations=standard_locations):
        newplayer = Player(name)

        self.players = {name : newplayer}
        self.locations = locations
        self.started = False

        if "https://imgur.com/x0DkNO7" not in self.locations and "Elon Musk" in self.players:
            self.locations.append("https://imgur.com/x0DkNO7")
            print("Adding special location!")
    
    def __used_ids(self):
        print('Hela hela ho lala')
        return [player.id for player in self.players.values()]
    ids = property(__used_ids)

    def add_player(self, name, role="none"):
        new_player = Player(name, self.ids, role)
        self.players[name] = new_player

        print("Adding player!")
        if "https://imgur.com/DHsOCaA" not in self.locations and "Elon Musk" in self.players:
            self.locations.append("https://imgur.com/DHsOCaA")
            print("Adding special location!")

        return new_player


class Player:
    def __init__(self, name, exclude_id=[], role="none"):
        self.name = name
        self.role = role
        self.id = generate_random_id(exclude_id)
    
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
        if not id in exclude:
            return id

def create_group(name):
    existing_ids = groups.keys()
    id = generate_random_id(existing_ids)
    groups[id] = Group(name)

    return {"successful": True, "group": id, "secretId": groups[id].players[name].id}

def joingroup(group_id,name):
    information = {"successful" : False, "players" : [], "error" : "", "id": ""}

    if group_id in groups:
        group = groups[group_id]

        if name in group.players:
            information["error"] = "Name already occupied."

        else:
            new_player = group.add_player(name)
            lijst = list(group.players.keys())

            information["successful"] = True
            information["players"] = lijst
            information["id"] = new_player.id
    
    else:
        information["error"] = "Unknown group."

    return information




