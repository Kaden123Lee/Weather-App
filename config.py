import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the weather app."""
    
    # OpenWeatherMap API configuration
    API_KEY = os.getenv('OPENWEATHER_API_KEY', '28dc0669191aed1d224f4950b8e35ff4')
    BASE_URL = 'https://api.openweathermap.org/data/2.5'
    
    # Default settings
    DEFAULT_CITY = 'Sacramento'
    DEFAULT_UNITS = 'metric'  # metric, imperial, kelvin
    
    # API endpoints
    CURRENT_WEATHER_URL = f"{BASE_URL}/weather"
    FORECAST_URL = f"{BASE_URL}/forecast"
    
    # Display settings
    TEMPERATURE_UNIT = '°C' if DEFAULT_UNITS == 'metric' else '°F'
    
    @classmethod
    def validate_api_key(cls):
        """Validate that API key is configured."""
        if not cls.API_KEY or cls.API_KEY == '28dc0669191aed1d224f4950b8e35ff4':
            raise ValueError("Please set your OpenWeatherMap API key in the .env file")