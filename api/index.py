# api/index.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

fastapi_application = FastAPI(title="Bare Minimum Test API")

fastapi_application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_application.get("/")
async def root_route():
    print("--- ROOT ROUTE REACHED ---")
    return {"message": "Bare minimum API is ALIVE!"}

@fastapi_application.get("/api/test")
async def test_api_route():
    print("--- /api/test ROUTE REACHED ---")
    return {"message": "Bare minimum /api/test is ALIVE!"}

app = Mangum(fastapi_application)