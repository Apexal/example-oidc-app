from flask import Flask, escape, request, render_template
from flask_oidc_ext import OpenIDConnect

scopes = ['openid', 'email', 'profile', 'cohort']
claims = [
    'username',
    'password',
    'email',
    'email_verified',
    'role',
    'phone',
    'phone_verified',
    'cohort',
    'majors',
    'minors',
    'gender',
    'given_name',
    'middle_name',
    'family_name'
]

app = Flask(__name__)
app.secret_key = 'secret'
app.config['OIDC_CLIENT_SECRETS'] = './client_secrets.json'
app.config['OIDC_SCOPES'] = scopes
oidc = OpenIDConnect(app)

@app.route('/')
def index():
    if oidc.user_loggedin:
        return render_template('index.html', logged_in=True, scopes=scopes, user=oidc.user_getinfo(fields=claims))
    else:
        return render_template('index.html', logged_in=False)
        

@app.route('/login')
@oidc.require_login
def login():
    info = oidc.user_getinfo(fields=['email', 'given_name', 'cohort'])
    return f'Welcome {info}'

@app.route('/logout')
def logout():
    oidc.logout()
    return 'Logged out'