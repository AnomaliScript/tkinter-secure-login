import customtkinter as ctk
import tkinter.messagebox as tkmb
from CONST import password_map, authentication, authorization

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x500")
app.title("Brandon's Login System")

# ChatGPT Code Example

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

    def login(self):

        username = self.username.get()
        password = self.password.get()

        # Check if username exists
        if username not in password_map:
            tkmb.showerror("Login Failed", "Invalid Username")
            return

        # Check password
        if password != password_map[username]:
            tkmb.showwarning("Wrong Password", "Please check your password")
            return

        # Call authentication logic
        power = authentication(username)

        if power is None:
            tkmb.showerror("Login Failed", "Authentication failed.")
            return

        # Store shared data in the controller
        self.controller.shared_data["username"] = username
        self.controller.shared_data["power"] = power

        # Welcome window (optional)
        new_window = ctk.CTkToplevel(self)
        new_window.title("Brandon's TKinter Login System")
        new_window.geometry("350x150")
        ctk.CTkLabel(new_window, text=f"Welcome, {username}!").pack(pady=20)

        # Move to dashboard
        self.controller.show_frame("DashboardPage")


class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        username = self.controller.shared_data.get("username")
        power = self.controller.shared_data.get("power")

        label = ctk.CTkLabel(self, text="Welcome to the Dashboard!")
        label.pack(pady=12)

        # Authorization
        permissions, personals = authorization(username, power)

        back_btn = ctk.CTkButton(self, text="Log Out", command=lambda: controller.show_frame("LoginPage"))
        back_btn.pack(pady=8)

    def refresh(self):
        username = self.controller.shared_data.get("username", "Unknown")
        status = self.controller.shared_data.get("status", "No Status")
        self.welcome_label.configure(text=f"Welcome, {username}")
        self.status_label.configure(text=f"Status: {status}")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk Secure Sign-In Simulator")
        self.geometry("400x300")

        # Page container
        self.pages = {}
        # self.pages = {page_name: PageClass(master=self, controller=self)}

        self.shared_data = {}
        # self.shared_data = {anything you want, but remember that it's a dict}

        for PageClass in (LoginPage, DashboardPage):
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


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = MainApp()
    app.mainloop()