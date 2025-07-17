import customtkinter as ctk
import tkinter.messagebox as tkmb
from CONST import password_map, authentication, authorization, authority_enums, authorities
from utils import hash_password, verify_password

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x500")
app.title("Brandon's Login System")

# ChatGPT Code Example (Now it's my version)

import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Login Page")
        label.pack(pady=12)

        self.username = ctk.CTkEntry(self, placeholder_text="Username")
        self.username.pack(pady=8)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=8)

        login_btn = ctk.CTkButton(self, text="Login", command=self.login)
        login_btn.pack(pady=8)

        login_btn = ctk.CTkButton(self, text="Don't Have An Account?", command=lambda: controller.show_frame("CreateAccount"))
        login_btn.pack(pady=8)

        self.controller.stored_hashes = {name: hash_password(password_map[name]) for name in password_map}

    def login(self):
        # EMPTY (imperative mood)!
        password_map = {}

        username = self.username.get()
        password = self.password.get()

        # Check if username exists
        if username not in self.controller.stored_hashes:
            tkmb.showerror("Login Failed", "Invalid Username")
            return

        # Get stored hashed password (password checking v2!)
        stored_hash = self.controller.stored_hashes[username]

        # Check password using Argon2
        if not verify_password(stored_hash, password):
            tkmb.showwarning("Wrong Password", "Please check your password")
            return

        # Call authentication logic
        authority = authentication(username)

        if authority is None:
            tkmb.showerror("Login Failed", "Authentication failed.")
            return

        # Store shared data in the controller
        self.controller.shared_data["username"] = username
        self.controller.shared_data["authority"] = authority

        # Move to dashboard
        self.controller.show_frame("DashboardPage")


# This page was created mostly by myself w/o AI
class CreateAccount(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Sign Up!")
        label.pack(pady=12)

        self.username = ctk.CTkEntry(self, placeholder_text="Username")
        self.username.pack(pady=8)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=8)

        submit_btn = ctk.CTkButton(self, text="Submit", command=self.submit)
        submit_btn.pack(pady=8)

    def submit(self):
        username = self.username.get()
        password = self.password.get()

        # password_map[username] = password
        self.controller.stored_hashes[username] = hash_password(password)
        authorities[username] = 1

        # Move back to login screen
        self.controller.show_frame("LoginPage")


class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Welcome to the Dashboard!")
        label.pack(pady=12)

        self.welcome_label = ctk.CTkLabel(self, text="")
        self.welcome_label.pack(pady=8)

        self.authority = ctk.CTkLabel(self, text="")
        self.authority.pack(pady=8)

        self.perm = ctk.CTkLabel(self, text="")
        self.perm.pack(pady=8)

        self.pers = ctk.CTkLabel(self, text="")
        self.pers.pack(pady=4)

        back_btn = ctk.CTkButton(self, text="Log Out", command=lambda: controller.show_frame("LoginPage"))
        back_btn.pack(pady=4)

    def refresh(self):
        # Checking for existence
        username = self.controller.shared_data.get("username")
        authority = self.controller.shared_data.get("authority")

        if not username and not authority:
            self.welcome_label.configure(text="User not found")
            self.authority.configure(text="")
            return

        # Call authorization once
        result = authorization(username, authority)
        if result is not None:
            permissions, personals = result

        # Authority to a more well-known title
        auth = authority_enums[authority]
        
        # Asset Widgets

        
        # Update UI
        self.welcome_label.configure(text=f"Welcome, {username}")
        self.authority.configure(text=f"Status: {auth}")
        self.perm.configure(text=f"You have access to: {permissions}")
        self.pers.configure(text=f"You has personal access to: {personals}")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        print("MainApp initialized!")

        self.title("CTk Secure Sign-In Simulator")
        self.geometry("800x300")

        # Page container
        self.pages = {}
        # self.pages = {page_name: PageClass(master=self, controller=self)}

        self.shared_data = {}
        # self.shared_data = {anything you want, but remember that it's a dict}

        # Sharing stored hashes
        self.stored_hashes = {}

        for PageClass in (LoginPage, CreateAccount, DashboardPage):
            page_name = PageClass.__name__
            frame = PageClass(master=self, controller=self)
            self.pages[page_name] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget()

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        for frame in self.pages.values():
            frame.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)
        if hasattr(frame, "refresh"):
            frame.refresh()
        frame.pack(fill="both", expand=True)

    def show_frame(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        page = self.pages[page_name]
        if hasattr(page, "refresh"):
            page.refresh()  # ← this runs for the page being shown
        page.pack(fill="both", expand=True)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = MainApp()
    app.mainloop()