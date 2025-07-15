from typing import List, Optional, Dict, Any
from datetime import datetime
import requests.exceptions  # For exception handling
from api_client import WeatherAPIClient
from models import WeatherData, ForecastItem
from exceptions import CityNotFoundError, NetworkError

class WeatherService:
    """Service layer for weather operations."""
    
    def __init__(self, api_client: WeatherAPIClient):
        self.api_client = api_client
    
    def get_current_weather(self, city: str, units: str = 'metric') -> WeatherData:
        """Get current weather and convert to WeatherData model."""
        try:
            data = self.api_client.get_current_weather(city, units)
            return self._parse_current_weather(data)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"City '{city}' not found")
            raise
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to fetch weather data: {e}")
    
    def get_forecast(self, city: str, units: str = 'metric') -> List[ForecastItem]:
        """Get forecast and convert to ForecastItem models."""
        try:
            data = self.api_client.get_forecast(city, units)
            return self._parse_forecast(data)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"City '{city}' not found")
            raise
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to fetch forecast data: {e}")
    
    def _parse_current_weather(self, data: Dict[str, Any]) -> WeatherData:
        """Parse API response into WeatherData model."""
        return WeatherData(
            city=data['name'],
            country=data['sys']['country'],
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            description=data['weather'][0]['description'].title(),
            wind_speed=data['wind']['speed'],
            wind_direction=data['wind'].get('deg'),
            visibility=data.get('visibility'),
            timestamp=datetime.fromtimestamp(data['dt'])
        )
    
    def _parse_forecast(self, data: Dict[str, Any]) -> List[ForecastItem]:
        """Parse forecast API response into ForecastItem models."""
        items = []
        for item in data['list'][:8]:  # Next 24 hours (8 x 3-hour intervals)
            items.append(ForecastItem(
                datetime=datetime.fromtimestamp(item['dt']),
                temperature=item['main']['temp'],
                description=item['weather'][0]['description'].title(),
                humidity=item['main']['humidity']
            ))
        return items