# config.py
class Config:
    SECRET_KEY = 'your_secret_key'  # Replace with a secure secret key in production
    DEBUG = True  
    
    # Fitbit API settings
    CLIENT_ID = "23QCSZ"
    CLIENT_SECRET = "4112a6a244bf91db710ff2580f2be515"
    REDIRECT_URI = "http://localhost:5000/callback"
    
    # Add this line
    FRONTEND_URL = "http://localhost:3000"
    
    # Fitbit API endpoints
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"