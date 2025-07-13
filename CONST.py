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
    'o' : ['the dead bodies', 'journal', 'sketchbook', '1Password password'],
    'm' : ['snack stash'],
    'u' : ['regular services'],
    'g' : ['limited services'], 
    'Joe' : ['camera work'],
    'Regnarts' : ['gaming laptop', 'Razer gaming chair'],
    'Tanner' : ['electric keyboard'],
}

def authentication(uname):
    match uname:
        # Owner (me, ofc)
        case 'AnomaliScript':
            return 'o'
        # Moderators
        case 'Regnarts' | 'MrPumpkin' | 'DiligentBuilder':
            return 'm'
        # Users
        case 'Joe' | 'Ammar' | 'Issac' | 'Maro' | 'Lexie' | 'Tanner' | 'London' | 'Eli' | 'Ryan' | 'Josh':
            return 'u'
        # Guests
        case 'Guest' | 'guest':
            return 'g'
        # Not Valid
        case _:
            return None
        
def authorization(uname, stat):
    permissions = []
    personals = []
    # list what can or can't be seen
    return permissions, personals