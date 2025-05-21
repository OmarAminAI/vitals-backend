# utils/config.py
import os

class Config:
    SECRET_KEY = 'your_secret_key' # You can keep this or replace if needed
    DEBUG = True # Or False, depending on your needs

    # Fitbit API settings - HARDCODED VALUES
    # WARNING: THIS IS INSECURE FOR PRODUCTION. USE ENVIRONMENT VARIABLES.
    CLIENT_ID = "23QCSZ"
    CLIENT_SECRET = "4112a6a244bf91db710ff2580f2be515"

    # Your Vercel backend deployment for REDIRECT_URI
    REDIRECT_URI = "https://vitals-backend.vercel.app/api/callback"

    # Your frontend URL
    FRONTEND_URL = "https://sekmed-front.vercel.app/"

    # Fitbit URLs - these are typically fine to keep as they are
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"

    # Remove or comment out the os.environ.get() calls for the hardcoded values:
    # CLIENT_ID = os.environ.get("FITBIT_CLIENT_ID", "") # No longer needed
    # CLIENT_SECRET = os.environ.get("FITBIT_CLIENT_SECRET", "") # No longer needed
    # REDIRECT_URI = os.environ.get(
    #     "REDIRECT_URI", "https://vitals-backend.vercel.app/api/callback"
    # ) # No longer needed if the default is what you want
    # FRONTEND_URL = os.environ.get(
    #     "FRONTEND_URL", "https://sekmed-front-579bclytf-omaraminais-projects.vercel.app"
    # ) # No longer needed if the default is what you want