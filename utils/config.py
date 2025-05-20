import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    DEBUG = os.environ.get("DEBUG", "True") == "True"

    # Fitbit API settings
    CLIENT_ID = os.environ.get("FITBIT_CLIENT_ID", "")
    CLIENT_SECRET = os.environ.get("FITBIT_CLIENT_SECRET", "")

    # Use your Vercel backend deployment for REDIRECT_URI in production!
    REDIRECT_URI = os.environ.get(
        "REDIRECT_URI", "https://vitals-backend.vercel.app/api/callback"
    )
    FRONTEND_URL = os.environ.get(
        "FRONTEND_URL", "https://sekmed-front-579bclytf-omaraminais-projects.vercel.app"
    )

    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"