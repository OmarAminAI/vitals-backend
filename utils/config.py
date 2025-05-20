import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use env var or fallback
    DEBUG = os.environ.get("DEBUG", "True") == "True"

    # Fitbit API settings
    CLIENT_ID = os.environ.get("FITBIT_CLIENT_ID", "")
    CLIENT_SECRET = os.environ.get("FITBIT_CLIENT_SECRET", "")
    # These should MATCH your actual deployed backend location!
    REDIRECT_URI = os.environ.get(
        "REDIRECT_URI", "https://your-vercel-backend-url.vercel.app/api/callback"
    )
    FRONTEND_URL = os.environ.get(
        "FRONTEND_URL", "https://sekmed-front-579bclytf-omaraminais-projects.vercel.app"
    )

    # Fitbit API endpoints
    AUTH_URL = "https://www.fitbit.com/oauth2/authorize"
    TOKEN_URL = "https://api.fitbit.com/oauth2/token"
    API_BASE_URL = "https://api.fitbit.com/1/user/-/"