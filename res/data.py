import random
import datetime as dt
import time

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
        
        if "https://imgur.com/x0DkNO7" not in self.locations and "Elon Musk" in self.players:
            self.locations.append("https://imgur.com/x0DkNO7")
            print("Adding special location!")

        if "Beatrix" in self.players and "Becca" in self.players and "Bella" in self.players:
            if "YO MOMMA's FAT" not in self.locations:
                self.locations.append("YO MOMMA's FAT")
        
        if "Chris Messina" in self.players:
            if "==> 8" not in self.locations:
                self.locations.append("==> 8")

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

    if group_id == 'DEMABE':
        if 'DEMABE' not in groups:
            groups['DEMABE'] = Group('Elon Musk')

        req = dt.datetime(2019, 6, 3, 17, 40, 0, 0)
        now = dt.datetime.now()
        timedelta = req - now
        timedelta = timedelta.days * 24 * 3600 + timedelta.seconds

        if timedelta > 0:
            timedelta = bin(timedelta)[2:]
        else:
            timedelta = 'PDF'

        groups['DEMABE'].locations = ['Beatrix', '/destination', 'Bella', str(timedelta), '2ZKB7fV', 'uggcf://fclsny.urebxhncc.pbz/fgbelgvzr', 'Becca', '(52.35433, 4.95876)']

    if group_id == '81T81T':
        if '81T81T' not in groups:
            groups['81T81T'] = Group('Smart presentation viewer')
            groups['81T81T'].locations = ['Ops team', '/erinsletter/answer', 'Why Snapchat?', 'bit.ly/test', 'GROUP: 6 accidents']

    if group_id == '``````':
        if '``````' not in groups:
            groups['``````'] = Group('Memory Keeper')
            groups['``````'].locations = ['==> X']

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

def look_at_time(advent_days):
    req = dt.datetime(2019, 7, 29, 17, 30, 0, 0)
    now = dt.datetime.now()
    timedelta = req - now
    timedelta = timedelta.days * 24 * 3600 + timedelta.seconds

    if timedelta > advent_days * 3600 * 24:
        return False
    return True

def create_hints():
    return [
        {
            'number' : 1,
            'solved' : False,
            'letter' : 'A',
            'opened' : look_at_time(1),
            'desc'   : 'Look at all the provided letters!'
        },
        {
            'number' : 2,
            'solved' : False,
            'letter' : 'R',
            'opened' : look_at_time(2),
            'desc'   : '<!-- Bit = 49.867 -->'
        },
        {
            'number' : 3,
            'solved' : False,
            'letter' : 'D',
            'opened' : look_at_time(3),
            'desc'   : 'Snapchat is mostly known for its augmented reality filters.'
        },
        {
            'number' : 4,
            'solved' : False,
            'letter' : 'E',
            'opened' : look_at_time(4),
            'desc'   : 'DE-MA-BE'
        },
        {
            'number' : 5,
            'solved' : False,
            'letter' : 'N',
            'opened' : look_at_time(5),
            'desc'   : 'The answer to where we\'re going, is written behind the Nick Cage painting.'
        },
        {
            'number' : 6,
            'solved' : False,
            'letter' : 'N',
            'opened' : look_at_time(6),
            'desc'   : 'MOM\'s MAYO'
        },
        {
            'number' : 7,
            'solved' : False,
            'letter' : 'E',
            'opened' : look_at_time(7),
            'desc'   : 'Perhaps it\'s not the pointed letters, perhaps it\'s NOT the provided letters!'
        },
        {
            'number' : 8,
            'solved' : False,
            'letter' : 'N',
            'opened' : look_at_time(8),
            'desc'   : '/erinsletter/answer'
        },
        {
            'number' : 9,
            'solved' : False,
            'letter' : 'B',
            'opened' : look_at_time(9),
            'desc'   : '==> J    \n==> W    \n==> K    \n==> F'
        },
        {
            'number' : 10,
            'solved' : False,
            'letter' : 'E',
            'opened' : look_at_time(10),
            'desc'   : 'http://spyfal.herokuapp.com/clicker'
        },
        {
            'number' : 11,
            'solved' : False,
            'letter' : 'L',
            'opened' : look_at_time(11),
            'desc'   : '==> H    \n==> C   \n==> T   \n==> P'
        },
        {
            'number' : 12,
            'solved' : True,
            'letter' : 'G',
            'opened' : look_at_time(12),
            'desc'   : 'Go to /my-guess/<yourname>/<thelocation> to submit a guess where we\'re going to!'
        },
        {
            'number' : 13,
            'solved' : False,
            'letter' : 'I',
            'opened' : look_at_time(13),
            'desc'   : 'Why did the first series of puzzles end with a Snapchat filter?'
        },
        {
            'number' : 14,
            'solved' : True,
            'letter' : 'E',
            'opened' : look_at_time(14),
            'desc'   : 'Hmmmm...... Team Unilever would sure thing enjoy making an anagram out of "YO MOMMA\'S"!'
        }
    ]
