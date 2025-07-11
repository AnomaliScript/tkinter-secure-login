import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500")
app.title("Modern Login UI using Customtkinter")

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
permissions = {
    'o' : 'the dead bodies',
    'm' : 'snack stash',
    'u' : 'regular services',
    'g' : 'limited services'
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
            tkmb.showerror(title="Login Failed",message="Invalid Username")
            return None
        
def authorization(uname, stat):
    if (user_pass.get() == password_map[uname]):
        return permissions[stat]
    else:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
            

def login():
    new_window = ctk.CTkToplevel(app)

    new_window.title("Brandon's TKinter Login System")

    new_window.geometry("350x150")

    username = user_entry.get()
    status = authentication(username)
    permissions = authorization(username, status)
    ctk.CTkLabel(new_window,text=f"Welcome, {username}! you have access to {permissions}").pack()


label = ctk.CTkLabel(app,text="This is the main UI page")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text='Modern Login System UI')
label.pack(pady=12,padx=10)

user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)


button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)


app.mainloop()