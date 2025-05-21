# api/index.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # We'll keep CORS for now
from mangum import Mangum

# 1. Define your FastAPI application
fastapi_application = FastAPI(title="Bare Minimum Test API")

# Configure CORS to allow all origins for this test
fastapi_application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_application.get("/")
async def root_route():
    print("--- ROOT ROUTE REACHED ---") # Add very distinct print
    return {"message": "Bare minimum API is ALIVE!"}

@fastapi_application.get("/api/test") # Add another distinct test endpoint
async def test_api_route():
    print("--- /api/test ROUTE REACHED ---") # Add very distinct print
    return {"message": "Bare minimum /api/test is ALIVE!"}

# 2. Vercel/Mangum handler
app = Mangum(fastapi_application)

# NO OTHER IMPORTS. NO utils.config, utils.auth, utils.data.
# NO OTHER ROUTES.