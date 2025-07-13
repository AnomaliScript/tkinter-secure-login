password_map = {
    'AnomaliScript' : '24Af7NP5XassY$@',
    'Regnarts' : 'c00lk|d',
    'MrPumpkin' : 'm&ng0',
    'DiligentBuilder' : 's4ck0feye$',
    'Joe' : 'what$up3verybody',
    'Ammar' : 's1ckdUd3',
    'Issac' : 'He%m4n',
    'Maro' : 'm@#n3rW',
    'Lexie' : 'g0OdmYrn][g',
    'Tanner' : '0nth3ke&s',
    'London' : 'pr3ci@teiT',
    'Eli' : 'h3re4ndN+w',
    'Ryan' : 'aVp3rs*n',
    'Josh' : 'P4rad^dD!e'
}

# To be used
all_permissions = {
    4 : ['the dead bodies', 'journal', 'sketchbook', '1Password password'],
    3 : ['snack stash'],
    2 : ['regular services'],
    1 : ['limited services'], 
    'Joe' : ['camera work'],
    'Regnarts' : ['gaming laptop', 'Razer gaming chair'],
    'Tanner' : ['electric keyboard'],
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
        
def authorization(uname, stat):
    permissions = []
    personals = []
    for i in range(stat, 0, -1):
        for j in range(len(all_permissions[i])):
            permissions.append[j]
    if uname in all_permissions:
        for i in range(len(all_permissions[uname])):
            personals.append[i]

    return permissions, personals