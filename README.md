# OpenID Connect Client

A barebones Flask app to test with the RCOS Identity Platform (RIP) in development.

To use you must create `client_secrets.json`:

```json
{
    "web": {
        "client_id": "<client id here>",
        "client_secret": "<secret here>",
        "auth_uri": "http://localhost:3000/auth",
        "token_uri": "http://localhost:3000/token",
        "userinfo_uri": "http://localhost:3000/me",
        "redirect_uris": [
            "http://localhost:5000/oidc_callback"
        ],
        "issuer": "http://localhost:3000"
    }
}
```

and run with

`$ FLASK_APP=app.py flask run`