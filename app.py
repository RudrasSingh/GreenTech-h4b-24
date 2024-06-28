from flask import *
from pyrebase import *
from dotenv import load_dotenv
import os
from authlib.integrations.flask_client import OAuth
#-----------------setting up the app------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.secret_key = 'SECRET_KEY' #generate a secret key and use it here in this virtual env
load_dotenv()

#------------------------Database setup-----------------------------
# @app.before_request
# def before_request():
#     # Open database connection before each request
#     db.connect_to_database()

# @app.after_request
# def after_request(response):
#     # Close database connection after each request
#     db.close_connection()
#     return response

#--------------Authlib---------------
oauth = OAuth(app)
oauth.register(
    "club",
    client_id=os.getenv("OAUTH2_CLIENT_ID"),
    client_secret=os.getenv("OAUTH2_CLIENT_SECRET"),
    client_kwargs={"scope": "openid profile email",},
    server_metadata_url=f'{os.getenv("OAUTH2_META_URL")}',
)
#------------------------firebase setting---------------------------

firebase_config = {
  'apiKey': os.getenv('APIKEY'),
  'authDomain': os.getenv('AUTHDOMAIN'),
  'projectId': os.getenv('PROJECTID'),
  'storageBucket': os.getenv('STORAGEBUCKET'),
  'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
  'appId': os.getenv('APPID'),
  'measurementId': os.getenv('MEASUREMENTID'),
  'databaseURL': ""
}

firebase = initialize_app(firebase_config)
auth = firebase.auth() #auth for the user_token 

#------------------- Routing ------------------------

@app.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'POST':

        email = request.form.get('newemail')
        password = request.form.get('newpassword')
        name = request.form.get('name')
        user_type = request.form.get('radio')

        try:
            user = auth.create_user_with_email_and_password(email, password)
            
            if user_type.lower() == 'club':
                session["userType"] = user_type.lower()
                flash(f"Account Created Successfully for {user_type}!",'message')
                #redirects to complete profile page for club with updated session info
            else:
                session["userType"] = user_type.lower()
                flash(f"Account Created Successfully for {user_type}!",'message')

            return redirect('/complete-profile')
        except Exception as e:
            print("Error During Signup:", e)
            flash("Something went wrong!",'error')
            return redirect('/sign-up')
            # Print error for debugging


    else:

        return render_template('signup.html')


@app.route("/signin-google")
def googleCallback():
    
    try:
        # fetch access token and id token using authorization code
        token = oauth.clubsync.authorize_access_token()
        # print(token,"\n\n",type(token))

        token = dict(token)
        # print(json.dumps(token, indent = 4))
        # Extract necessary user data from the ID token
        personal = token.get('userinfo')
        user_info = {"name" : personal.get('name'),
                    "email" : personal.get('email'),
                    "idToken" : token.get('id_token')}
        # Set complete user information in the session
        session["user"] = user_info
        return redirect('/choose-user') 
    except Exception as e:
        print("Error during google callback:", e)
        return redirect('/sign-up')


@app.route("/google-login")
def googleLogin():
    try:
        if "user" in session:
            abort(404)
        return oauth.clubsync.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))
    except Exception as e:
        flash("Error during google login:", "Failure")
        print(e)
        return redirect('/signup')

    

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')

            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect('/')
        
        except Exception as e:
                    print("Error during login:", e)  # Print error for debugging
                    login_error = "Invalid email or password. Please try again."
                    flash(login_error)
                    return render_template('login.html')
        
    else:
        return render_template('login.html')
    

@app.route('/logout')
def logout():

    session.pop('user', None)
    session.clear() 
    flash("Logged out successfully!","Success")
    return redirect('/')


@app.route('/forgot-password', methods=['GET','POST'])
def forgotPassword():
    if request.method == 'POST':
        try:
            email = request.form.get('user_email')
            try:
                auth.send_password_reset_email(email)
                flash("Password reset link sent to your email!","Success")
                return redirect('/login')
            except Exception as e:
                print("Error during password reset:", e)
                flash("Something went wrong!","Error")
                return redirect('/login')
            
        except Exception as e:

            print("Error during password reset:", e)
            flash("Something went wrong!","Error")
            return redirect('/login')
        
    return render_template('forgotPassword.html')


@app.route('/')
def homepage():
    """
    
    """   
    if 'user' in session:

        #signed user
        
        user_id_token = session['user']
        try:
            
            email = session["user"]
            return render_template('home.html')
        

        except KeyError as e:
            flash(e,"Something went wrong!")
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)