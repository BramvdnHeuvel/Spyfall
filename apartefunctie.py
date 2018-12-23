def joingroup(group,name):
    information = {"succesful" : False, "players" : []}

    if group in groups:
        information["succesful"] = True
        new_player = player(name, "none")
        groups[group].players[name] = new_player
        list = players.keys()
        information["players"] = list
        return information

    return information