# AI Weather Agent

An AI agent built with LangChain and Google's Gemini model that can retrieve real-time weather information using OpenWeatherMap API. The agent uses tool calling to determine when to fetch weather data and can automatically detect the user's location when no city is specified.

## Features

- Real-time weather retrieval using OpenWeatherMap API
- Automatic location detection using IP geolocation
- LangChain agent with multiple tools
- Gemini 2.5 Flash integration
- Dynamic tool selection through AI reasoning
- Support for both Celsius and Fahrenheit temperatures
- PostgreSQL database storage using Supabase

## How It Works

The application uses two tools:

### get_weather(city)

Retrieves live weather data for a specified city using the OpenWeatherMap API.

### get_location()

Determines the user's current location through IP-based geolocation.

The AI agent decides which tool(s) to use based on the user's query.

Examples:

- "What's the weather in Charlotte?"
  - Calls `get_weather("Charlotte")`

- "What's the weather today?"
  - Calls `get_location()`
  - Calls `get_weather(location)`
    
## Architecture

```text
User Query
    │
    ▼
Gemini 2.5 Flash
    │
    ▼
LangChain Agent
    │
    ├── get_weather()
    │       └── OpenWeatherMap API
    │
    └── get_location()
            └── IP Geolocation API
    │
    ▼
Agent Response
    │
    ▼
Supabase PostgreSQL
(Persistent Conversation Memory)
```

## Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini 2.5 Flash
- OpenWeatherMap API
- IPAPI Geolocation API
- PostgreSQL
- Supabase
- Requests
- Python Dotenv

## Project Structure

```text
ai-weather-agent/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/dhvani-vora/ai-weather-agent
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
OPEN_WEATHER_API_KEY=your_openweather_api_key
SUPABASE_DB_URI=your_supabase_connection_string
```

4. Run the application

```bash
python main.py
```

## Example Usage

```text
Enter your query here:
What is the weather in New York?
```

Output:

```text
The weather in New York is sunny with a temperature of 25°C. The wind speed is 3.5 m/s and the humidity is 60%.
```

## Conversation Memory

The agent uses LangGraph's PostgresSaver with a PostgreSQL database hosted on Supabase.

Conversation history is stored persistently, allowing the agent to remember previous messages even after the application is restarted.

Example:

```text
User: Where am I?
Agent: You are in Rome, Italy.

[Application closes]

User: What is the weather there?
Agent: The weather in Rome is sunny with a temperature of 25°C.
```

## Learning Outcomes

Through this project, I learned:

- Building AI agents with LangChain
- Tool calling and function execution
- Managing conversation memory
- Using LangGraph checkpointers
- Working with PostgreSQL databases
- Integrating Supabase with Python
- Designing multi-step AI workflows

## Future Improvements

- Web interface
- User authentication
- Weather forecasts
- GPS-based location retrieval
- Multiple user sessions
- Deployment to cloud hosting

## Version History

### v1.0
- Gemini-powered weather agent
- Tool calling with OpenWeatherMap API
- Automatic location detection

### v1.1
- Persistent conversation memory
- PostgreSQL database integration
- Supabase cloud storage
- Conversation history across sessions
