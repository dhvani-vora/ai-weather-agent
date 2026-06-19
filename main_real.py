from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver

import os

import requests

load_dotenv()

DB_URI = os.getenv("SUPABASE_DB_URI")

def get_weather(city: str):
    """Get weather for a given city.
    Return temperature in Celsius for most locations, but return in Fahrenheit for US, Liberia, Burma"""
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    if response.status_code != 200:
        return {
            "error": data.get("message", "Unknown error")
        }

    temperature_celsius = data['main']['temp']
    
    temperature_fahrenheit = temperature_celsius * 9/5 + 32
    
    weather_data = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "condition": data["weather"][0]["description"],
        "temperature_celsius": round(temperature_celsius, 1),
        "temperature_fahrenheit": round(temperature_fahrenheit, 1),
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return weather_data

def get_location():
    """Get user's current location. Use this when the user asks about the weather without specifying a city."""
    response = requests.get("https://ipapi.co/json/", headers={"User-Agent": "yourbot/0.1"})
    if response.status_code != 200:
        return {"error": "City not found"}
    data = response.json()
    city = data['city']
    country = data['country_name']
    return f"{city}, {country}"


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
system_prompt = """
You are a helpful weather assistant.

Workflow:
1. If the user asks about weather without specifying a city,
   first call get_location().
2. Then call get_weather() using that location.
3. If the user specifies a city directly,
   call get_weather() immediately.
4. Use your knowledge to determine which temperature unit to use (Celsius or Fahrenheit) based on the user's location or query.
5. Present the weather information including temperature in the appropriate unit, condition, wind speed, humidity, and any other relevant details from the get_weather() response.
"""
connection =  PostgresSaver.from_conn_string(DB_URI)
checkpointer = connection.__enter__()
agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=system_prompt,
    checkpointer = checkpointer
)

