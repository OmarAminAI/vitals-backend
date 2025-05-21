from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import Optional
# from utils.config import Config # Keep this commented if it's causing silent crashes
from utils.auth import authorize_user, get_token # Keep commented if not essential for current test
from utils.data import fetch_fitbit_data # Keep commented if not essential for current test
from mangum import Mangum

# 1. Define your FastAPI application
fastapi_application = FastAPI(title="Fitbit API Backend")

# Configure CORS to allow all origins
# WARNING: This is insecure for production.
# Only use for debugging or if your API is truly public.
fastapi_application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True, # Or False, depending if you need cookies/auth headers from different origins
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

@fastapi_application.get("/")
async def home_route():
    print("DEBUG: Home route / accessed") # Add a print statement
    return {"message": "Fitbit API Backend. Use /authorize to begin."}

# Keep /api/authorize simplified for now if utils.auth or utils.config is problematic
@fastapi_application.get("/api/authorize")
async def authorize():
    print("DEBUG: /api/authorize accessed") # Add a print statement
    # Temporarily return a simple response or a hardcoded redirect
    # if authorize_user() or Config depends on the problematic module
    # auth_url = authorize_user()
    # return RedirectResponse(auth_url)
    return {"message": "Authorize endpoint placeholder"} # Placeholder

# Comment out other routes if they depend on problematic utils
# @fastapi_application.get("/api/callback")
# ...

# @fastapi_application.get("/api/data/{data_type}")
# ...

# @fastapi_application.get("/api/data/activity_summary")
# ...

# 2. Vercel/Mangum handler
app = Mangum(fastapi_application)