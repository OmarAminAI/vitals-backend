from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import Optional
from utils.config import Config
from utils.auth import authorize_user, get_token
from utils.data import fetch_fitbit_data
from mangum import Mangum # Make sure Mangum is imported

# 1. Define your FastAPI application with a different variable name
fastapi_application = FastAPI(title="Fitbit API Backend")

fastapi_application.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_application.get("/")
async def home_route(): # Renamed from 'home' to avoid conflict if 'home' is a common name
    return {"message": "Fitbit API Backend. Use /authorize to begin."}

@fastapi_application.get("/api/authorize")
async def authorize():
    auth_url = authorize_user()
    return RedirectResponse(auth_url)

@fastapi_application.get("/api/callback")
async def callback(code: Optional[str] = None, error: Optional[str] = None):
    frontend_url = Config.FRONTEND_URL

    if error:
        return RedirectResponse(f"{frontend_url}/home?error={error}")
    if not code:
        return RedirectResponse(f"{frontend_url}/home?error=no_code")

    try:
        tokens = await get_token(code)
        access_token = tokens['access_token']
        return RedirectResponse(f"{frontend_url}/home?token={access_token}&view=vital")
    except Exception as e:
        return RedirectResponse(f"{frontend_url}/home?error={str(e)}")

@fastapi_application.get("/api/data/{data_type}")
async def get_data(
    data_type: str,
    period: str = "7d",
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    access_token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization

    try:
        period_mapping = {"1d": "daily", "7d": "weekly", "30d": "monthly"}
        backend_period = period_mapping.get(period, "weekly")
        type_mapping = {
            "heart": "heart_rate",
            "distance": "distance",
            "steps": "steps",
            "calories": "calories",
            "activity_summary": "activity_summary"
        }
        backend_data_type = type_mapping.get(data_type, data_type)
        data = await fetch_fitbit_data(access_token, backend_data_type, backend_period)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@fastapi_application.get("/api/data/activity_summary")
async def get_activity_summary(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    access_token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization

    try:
        data = await fetch_fitbit_data(access_token, "activity_summary", "daily")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Vercel/Mangum handler: Export the Mangum instance AS 'app'
app = Mangum(fastapi_application)

# If you previously had 'handler = Mangum(app)', remove or comment it out.
# Make sure only ONE final 'app' (the Mangum instance) or 'handler' is effectively exported.