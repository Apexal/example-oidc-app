from flask import Flask, escape, request
from flask_oidc_ext import OpenIDConnect

app = Flask(__name__)
app.secret_key = 'secret'
app.config['OIDC_CLIENT_SECRETS'] = './client_secrets.json'
app.config['OIDC_SCOPES'] = ['openid', 'email', 'profile', 'cohort']
oidc = OpenIDConnect(app)

@app.route('/')
def index():
    if oidc.user_loggedin:
        return f'Hello, {oidc.user_getfield("given_name")}!'
    else:
        return 'Please login'

@app.route('/login')
@oidc.require_login
def login():
    info = oidc.user_getinfo(fields=['email', 'given_name', 'cohort'])
    return f'Welcome {info}'

@app.route('/logout')
def logout():
    oidc.logout()
    return 'Logged out'