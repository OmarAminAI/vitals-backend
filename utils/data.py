import httpx
from datetime import datetime, timedelta
from .config import Config

def get_date_range(period):
    today = datetime.now().strftime("%Y-%m-%d")
    if period == 'daily':
        start_date = today
    elif period == 'weekly':
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    elif period == 'monthly':
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    else:
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    return start_date, today

async def fetch_fitbit_data(access_token, data_type, period='weekly'):
    headers = {"Authorization": f"Bearer {access_token}"}
    start_date, end_date = get_date_range(period)

    if data_type == 'heart_rate':
        url = f"{Config.API_BASE_URL}activities/heart/date/{start_date}/{end_date}.json"
    elif data_type == 'calories':
        url = f"{Config.API_BASE_URL}activities/calories/date/{start_date}/{end_date}.json"
    elif data_type == 'steps':
        url = f"{Config.API_BASE_URL}activities/steps/date/{start_date}/{end_date}.json"
    elif data_type == 'distance':
        url = f"{Config.API_BASE_URL}activities/distance/date/{start_date}/{end_date}.json"
    elif data_type == 'activity_summary':
        url = f"{Config.API_BASE_URL}activities/date/{end_date}.json"
    elif data_type == 'sleep':
        url = f"{Config.API_BASE_URL}sleep/date/{start_date}/{end_date}.json"
    else:
        return {"error": "Invalid data type"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()