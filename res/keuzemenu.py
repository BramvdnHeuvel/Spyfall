events = [
    {
        'name': 'Lasergamen',
        'desc': 'In Amersfoort een uurtje lasergamen met max. 13 personen... wie wil dat nou niet?',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Een cafeetje pakken',
        'desc': 'Een drankje doen met je matties in een heerlijk café.',
        'yes': [],
        'probably': ['Brom'],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Spelletjes spelen',
        'desc': 'Lekker met zijn allen een avondje spelletjes spelen bij iemand thuis!',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Sietse helpen daten',
        'desc': 'Sietse is alleen, eenzaam en single. Wie helpt hem aan een vriendin? en Bram is Gay.',
        'yes': [],
        'probably': [],
        'maybe': ['Brom'],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Escape room',
        'desc': 'Wat is er nou leuker dan een escape room doen? Het staat al zo lang in ons vizier, tijd om het nu ECHT te doen!',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Bram helpen klussen',
        'desc': 'Bram heeft een nieuwe kamer... wie zou hem nou niet willen ondersteunen in het opknappen van zijn kamer?',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Niks doen',
        'desc': 'Soms kan het zo simpel zijn.',
        'yes': [],
        'probably': [],
        'maybe': [],
        'hmm': ['Brom'],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Picknick en zwemmen',
        'desc': 'Zeg nou zelf, wat is er leuker op een warme zomerdag dan gezellig picknicken en af en toe zwemmen op een prachtige locatie?',
        'yes': ['Brom'],
        'probably': [],
        'maybe': ['Brom'],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'LAN Party',
        'desc': 'De mensen die hieraan meegedaan hebben, kunnen in geuren en kleuren vertellen hoe leuk het is; spelletjes spelen, maar dan digitaal! Niets is leuker dan je kapot lachen bij het spelen van debiele spelletjes, het competitief spelen van een shooter of het proberen samen te werken in een klungelige cooperative game.',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Poulen',
        'desc': 'Het is een relaxte bezigheid, maar wie zou er nou niet willen chillen met ballen en stokken?',
        'yes': [],
        'probably': ['Brom'],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Hackathon',
        'desc': 'De Spyfall website waar we ons NU op bevinden - is best wel een troep. Het idee om terug te gaan, nog een poging te wagen en menig hart te verblijden, zal iedereen gelukkig maken.',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'DnD Oneshot',
        'desc': 'Voor de D&D liefhebbers is er niets leukers dan te proberen een klein avontuur te beleven met hun favoriete X-Files vrienden!',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    },
    {
        'name': 'Minecraft Marathon',
        'desc': 'Laat je verbazen hoe leuk het kan zijn om te proberen een halve dag te overleven in een simpel spelletje zoals Minecraft. Team building, eindeloze gesprekken tijdens het werken en rustige samenwerkingen gegarandeerd!',
        'yes': ['Brom'],
        'probably': [],
        'maybe': [],
        'hmm': [],
        'no': [],
        'NA': ["Harissa", "Mork", "Swammy", "Seneca", "Egdar", "Mickey", "Riineer", "Meesje"],
    }
]

def calculate_event_score(event):
    score = 4*event['yes'] + 3*event['probably'] + 2*event['maybe'] + event['hmm']
    total = 4*(event['yes'] + event['probably'] + event['maybe'] + 
        event['hmm'] + event['no'] + event['NA']
    )
    
    return score/total