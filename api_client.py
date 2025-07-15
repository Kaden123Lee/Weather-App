import requests
from typing import Dict, Any, List
from datetime import datetime

class WeatherAPIClient:
    """Client for OpenWeatherMap API."""
    
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
    
    def get_current_weather(self, city: str, units: str = 'metric') -> Dict[str, Any]:
        """Fetch current weather data for a city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units
        }
        
        url = f"{self.base_url}/weather"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_forecast(self, city: str, units: str = 'metric') -> Dict[str, Any]:
        """Fetch 5-day forecast data for a city."""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units
        }
        
        url = f"{self.base_url}/forecast"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        
        return response.json()
