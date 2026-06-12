# AI Weather Agent

An AI agent built with LangChain and Google's Gemini model that can retrieve real-time weather information using OpenWeatherMap API. The agent uses tool calling to determine when to fetch weather data and can automatically detect the user's location when no city is specified.

## Features

- Real-time weather retrieval using OpenWeatherMap API
- Automatic location detection using IP geolocation
- LangChain agent with multiple tools
- Gemini 2.5 Flash integration
- Dynamic tool selection through AI reasoning
- Support for both Celsius and Fahrenheit temperatures

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

## Tech Stack

- Python
- LangChain
- Gemini 2.5 Flash
- OpenWeatherMap API
- Requests
- Python Dotenv

## Project Structure

```text
ai-weather-agent/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repo-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
OPEN_WEATHER_API_KEY=your_openweather_api_key
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
The weather in New York is sunny with a temperature of 25°C.
```

## Concepts Learned

This project was built while learning AI Engineering and demonstrates:

- AI Agents
- Tool Calling
- Prompt Engineering
- Environment Variables
- API Integration
- LangChain Workflows
- Multi-step Agent Reasoning

## Future Improvements

- Streamlit web interface
- Chat memory
- Weather forecasts
- Error handling for invalid cities
- Database-backed conversation history
