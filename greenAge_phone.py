# Import Kivy modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.config import Config
import os,dotenv
import pyrebase

dotenv.load_dotenv()


# Configure Kivy
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '300')

# Firebase configuration (replace with your Firebase project credentials)
config = {
    'apiKey': os.getenv('APIKEY'),
  'authDomain': os.getenv('AUTHDOMAIN'),
  'projectId': os.getenv('PROJECTID'),
  'storageBucket': os.getenv('STORAGEBUCKET'),
  'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
  'appId': os.getenv('APPID'),
  'measurementId': os.getenv('MEASUREMENTID'),
  'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

class GreenAgePhoneClient(App):

    def build(self):
        # Layout
        layout = GridLayout(cols=1, padding=10)
        
        # Title Label
        title_label = Label(text='GreenAge Phone Client', font_size=24, color=(0, 1, 0, 1))  # Green color
        layout.add_widget(title_label)
        
        # Email Input
        self.email_input = TextInput(hint_text='Email', multiline=False)
        layout.add_widget(self.email_input)
        
        # Password Input
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        layout.add_widget(self.password_input)
        
        # Login Button
        login_button = Button(text='Login', size_hint=(1, 0.5))
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        
        # Register Button
        register_button = Button(text='Register', size_hint=(1, 0.5))
        register_button.bind(on_press=self.register)
        layout.add_widget(register_button)
        
        return layout
    
    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.show_success_popup("Login successful")
        except Exception as e:
            self.show_error_popup(f"Login failed:")
            self.email_input.text = ""
            self.password_input.text = ""
    
    def register(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        
        try:
            auth.create_user_with_email_and_password(email, password)
            self.show_success_popup("Registration successful")
        except Exception as e:
            self.show_error_popup(f"Registration failed: {e}")
    
    def show_success_popup(self, message):
        popup = Popup(title='Success', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()
    
    def show_error_popup(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

# Run the app
if __name__ == '__main__':
    GreenAgePhoneClient().run()
