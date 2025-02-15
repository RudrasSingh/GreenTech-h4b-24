# # Import Kivy modules
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.popup import Popup
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.config import Config
# import os
# import dotenv
# import webbrowser
# import pyrebase

# dotenv.load_dotenv()

# # Configure Kivy
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '300')

# # Firebase configuration (replace with your Firebase project credentials)
# config = {
#     'apiKey': os.getenv('APIKEY'),
#     'authDomain': os.getenv('AUTHDOMAIN'),
#     'projectId': os.getenv('PROJECTID'),
#     'storageBucket': os.getenv('STORAGEBUCKET'),
#     'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
#     'appId': os.getenv('APPID'),
#     'measurementId': os.getenv('MEASUREMENTID'),
#     'databaseURL': ""
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# db = firebase.database()

# # Screen Manager to manage different screens
# sm = ScreenManager()

# class LoginScreen(Screen):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
        
#         # Layout
#         layout = GridLayout(cols=1, padding=10)
        
#         # Title Label
#         title_label = Label(text='GreenAge Phone Client', font_size=24, color=(0, 1, 0, 1))  # Green color
#         layout.add_widget(title_label)
        
#         # Email Input
#         self.email_input = TextInput(hint_text='Email', multiline=False)
#         layout.add_widget(self.email_input)
        
#         # Password Input
#         self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
#         layout.add_widget(self.password_input)
        
#         # Login Button
#         login_button = Button(text='Login', size_hint=(1, 0.5))
#         login_button.bind(on_press=self.login)
#         layout.add_widget(login_button)
        
#         # Register Button
#         register_button = Button(text='Register', size_hint=(1, 0.5))
#         register_button.bind(on_press=self.register)
#         layout.add_widget(register_button)
        
#         self.add_widget(layout)
    
#     def login(self, instance):
#         email = self.email_input.text
#         password = self.password_input.text
        
#         try:
#             user = auth.sign_in_with_email_and_password(email, password)
#             self.parent.current = 'MainScreen'
#             self.show_success_popup("Login successful")
#         except Exception as e:
#             self.show_error_popup(f"Login failed:")
#             self.email_input.text = ""
#             self.password_input.text = ""
    
#     def register(self, instance):
#         email = self.email_input.text
#         password = self.password_input.text
        
#         try:
#             auth.create_user_with_email_and_password(email, password)
#             self.show_success_popup("Registration successful")
#         except Exception as e:
#             self.show_error_popup(f"Registration failed: {e}")
    
#     def show_success_popup(self, message):
#         popup = Popup(title='Success', content=Label(text=message), size_hint=(None, None), size=(300, 200))
#         popup.open()
    
#     def show_error_popup(self, message):
#         popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
#         popup.open()

# class MainScreen(Screen):
#     def __init__(self, **kwargs):
#         super(MainScreen, self).__init__(**kwargs)
        
#         # Layout
#         layout = GridLayout(cols=1, padding=10)
        
#         # Title Label
#         title_label = Label(text='Welcome to GreenAge', font_size=32, color=(0, 1, 0, 1))  # Green color
#         layout.add_widget(title_label)
#         title_label = Label(text='Think Green', font_size=24, color=(0, 1, 0, 1))  # Green color
#         layout.add_widget(title_label)
        
#         # Report Waste Button
#         report_button = Button(text='Report Waste', size_hint=(1, 0.5))
#         report_button.bind(on_press=self.report_waste)
#         layout.add_widget(report_button)
        
#         # Open Webpage Button
#         webpage_button = Button(text='Open Webpage', size_hint=(1, 0.5))
#         webpage_button.bind(on_press=self.open_webpage)
#         layout.add_widget(webpage_button)
        
#         # Logout Button
#         logout_button = Button(text='Logout', size_hint=(1, 0.5))
#         logout_button.bind(on_press=self.logout)
#         layout.add_widget(logout_button)
        
#         self.add_widget(layout)
    
#     def report_waste(self, instance):
#         # Implement your functionality for reporting waste
#         self.show_success_popup("Waste reported successfully") 
    
#     def open_webpage(self, instance):
#         # Open a webpage (example URL)
#         webbrowser.open('http://127.0.0.1:5000')
    
#     def logout(self, instance):
#         auth.current_user = None
#         self.parent.current = 'LoginScreen'
#         self.show_success_popup("Logged out successfully")
    
#     def show_success_popup(self, message):
#         popup = Popup(title='Success', content=Label(text=message), size_hint=(None, None), size=(300, 200))
#         popup.open()

# # Add screens to the screen manager
# sm.add_widget(LoginScreen(name='LoginScreen'))
# sm.add_widget(MainScreen(name='MainScreen'))

# class GreenAgePhoneClient(App):
#     def build(self):
#         return sm

# # Run the app
# if __name__ == '__main__':
#     GreenAgePhoneClient().run()
