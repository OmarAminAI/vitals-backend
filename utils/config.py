# utils/config.py
import os # This is the only import

class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True

    CLIENT_ID = "23QCSZ"
    CLIENT_SECRET = "4112a6a244bf91db710ff2580f2be515"
    REDIRECT_URI = "https://vitals-backend.vercel.app/api/callback"
    FRONTEND_URL = "https://sekmed-front.vercel.app/"
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"