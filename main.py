import customtkinter as ctk
import tkinter.messagebox as tkmb
from CONST import password_map, permissions, authentication, authorization

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
        new_window = ctk.CTkToplevel(app)

        new_window.title("Brandon's TKinter Login System")

        new_window.geometry("350x150")

        self.controller.username, username = self.username.get()
        
        # Authentication
        self.controller.status = authentication(username) if authentication(username) != None else tkmb.showerror(title="Login Failed", message="Invalid Username")
        if (self.username.get() != password_map[self.username]):
            self.controller.show_frame("DashboardPage")
            tkmb.showwarning(title='Wrong password', message='Please check your password')
        ctk.CTkLabel(new_window,text=f"Welcome, {username}!").pack()


class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Welcome to the Dashboard!")
        label.pack(pady=12)

        # Authorization
        permissions = authorization(self.controller.username, self.controller.status)
        for p in permissions:
            

        back_btn = ctk.CTkButton(self, text="Log Out", command=lambda: controller.show_frame("LoginPage"))
        back_btn.pack(pady=8)


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk Secure Sign-In Simulator")
        self.geometry("400x300")

        # Page container
        self.pages = {}

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
    ctk.set_default_color_theme("blue")
    app = MainApp()
    app.mainloop()