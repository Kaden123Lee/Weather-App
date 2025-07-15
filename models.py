from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class WeatherData:
    """Data model for current weather information."""
    
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    description: str
    wind_speed: float
    wind_direction: Optional[int]
    visibility: Optional[int]
    timestamp: datetime
    
    def __str__(self):
        return f"Weather in {self.city}, {self.country}: {self.temperature}°C, {self.description}"

@dataclass
class ForecastItem:
    """Data model for forecast item."""
    
    datetime: datetime
    temperature: float
    description: str
    humidity: int
    
    def __str__(self):
        return f"{self.datetime.strftime('%H:%M')}: {self.temperature}°C, {self.description}"