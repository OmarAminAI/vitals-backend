from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import Optional
from utils.config import Config   # Note moved config import path
from utils.auth import authorize_user, get_token
from utils.data import fetch_fitbit_data

app = FastAPI(title="Fitbit API Backend")

# CORS for your deployed frontend!
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.FRONTEND_URL],  # Make sure this matches your deployed frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Fitbit API Backend. Use /authorize to begin."}

@app.get("/authorize")
async def authorize():
    auth_url = authorize_user()
    return RedirectResponse(auth_url)

@app.get("/callback")
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

@app.get("/api/data/{data_type}")
async def get_data(
    data_type: str, 
    period: str = "7d",  # (7d, 1d, 30d)
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

@app.get("/api/data/activity_summary")
async def get_activity_summary(authorization: str = Header(None)):  
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    access_token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization

    try:
        data = await fetch_fitbit_data(access_token, "activity_summary", "daily")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Vercel/Mangum handler (needed for serverless deployment)
from mangum import Mangum
handler = Mangum(app)