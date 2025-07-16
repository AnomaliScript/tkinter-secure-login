password_map = {
    'AnomaliScript' : '24Af7NP5XassY$@',
    'Regnarts' : 'Vh2@Ay%mO',
    'MrPumpkin' : 'EOI2w*E5q',
    'DiligentBuilder' : '$qGYzn9Ax',
    'Joe' : '#H0FClkZu',
    'Ammar' : '3BtaP9gX#',
    'Issac' : '79Rx@TJ!U',
    'Maro' : '1J$Pls!#Z',
    'Lexie' : '^5v^bSgAS',
    'Tanner' : 'qN$IvC1#q',
    'London' : 'p%3&rdWn0',
    'Eli' : '#3Qkv*dbi',
    'Ryan' : 'u%RHyH29@',
    'Josh' : 'x%q0kwS4s'
}

# To be used
all_permissions = {
    4 : ['the dead bodies', 'journal', 'sketchbook', '3D-Printed Glock 19', '1Password password'],
    3 : ['snack stash', '2D Printer', 'Anomali\'s setuid'],
    2 : ['regular services'],
    1 : ['limited services'], 
    'Joe' : ['camera work'],
    'Regnarts' : ['gaming laptop', 'Razer gaming chair'],
    'Tanner' : ['electric keyboard'],
}

authority_enums = {
    4 : "Boss", 
    3 : "Underboss", 
    2 : "Capo", 
    1 : "Soldier"
}

def authentication(uname):
    match uname:
        # Owner (me, ofc)
        case 'AnomaliScript':
            return 4
        # Moderators
        case 'Regnarts' | 'MrPumpkin' | 'DiligentBuilder':
            return 3
        # Users
        case 'Joe' | 'Ammar' | 'Issac' | 'Maro' | 'Lexie' | 'Tanner' | 'London' | 'Eli' | 'Ryan' | 'Josh':
            return 2
        # Guests
        case 'Guest' | 'guest':
            return 1
        # Not Valid
        case _:
            return None
        
def authorization(uname, authority):
    permissions = []
    personals = []
    for i in range(authority, 0, -1):
        for j in range(len(all_permissions[i])):
            permissions.append(all_permissions[i][j])
    if uname in all_permissions:
        for i in range(len(all_permissions[uname])):
            personals.append(all_permissions[uname][i])

    return permissions, personals