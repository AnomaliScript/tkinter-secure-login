# Optimally, these passwords shouldn't even be visible, but eh I can't do that yet ¯\_(ツ)_/¯
# At least the new accounts' passwords will be safe
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

authorities = {
    'AnomaliScript' : 4,
    'Regnarts' : 3,
    'MrPumpkin' : 3,
    'DiligentBuilder' : 3,
    'Joe' : 2,
    'Ammar' : 2,
    'Issac' : 2,
    'Maro' : 2,
    'Lexie' : 2,
    'Tanner' : 2,
    'London' : 2,
    'Eli' : 2,
    'Ryan' : 2,
    'Josh' : 2
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
    return authorities[uname]
        
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