from colorama import init, Fore, Style
import sys  # For input handling and potential system operations
from models import WeatherData
from typing import List
from models import WeatherData, ForecastItem

init()  # Initialize colorama

class WeatherUI:
    """User interface for the weather app."""
    
    def __init__(self):
        self.unit_symbol = '°C'  # Default
    
    def set_unit_symbol(self, units: str):
        """Set temperature unit symbol."""
        self.unit_symbol = '°C' if units == 'metric' else '°F'
    
    def display_welcome(self):
        """Display welcome message."""
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}           🌤️  WEATHER APP  🌤️")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")
    
    def get_city_input(self, default_city: str) -> str:
        """Get city name from user."""
        city = input(f"{Fore.YELLOW}Enter city name (default: {default_city}): {Style.RESET_ALL}").strip()
        return city if city else default_city
    
    def display_current_weather(self, weather: WeatherData):
        """Display current weather information."""
        print(f"\n{Fore.GREEN}{'='*50}")
        print(f"{Fore.GREEN}  CURRENT WEATHER")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        
        print(f"\n📍 {Fore.WHITE}{weather.city}, {weather.country}{Style.RESET_ALL}")
        print(f"🌡️  Temperature: {Fore.CYAN}{weather.temperature}{self.unit_symbol}{Style.RESET_ALL}")
        print(f"🤔 Feels like: {Fore.CYAN}{weather.feels_like}{self.unit_symbol}{Style.RESET_ALL}")
        print(f"☁️  Condition: {Fore.YELLOW}{weather.description}{Style.RESET_ALL}")
        print(f"💧 Humidity: {weather.humidity}%")
        print(f"📊 Pressure: {weather.pressure} hPa")
        print(f"💨 Wind: {weather.wind_speed} m/s")
        
        if weather.visibility:
            print(f"👁️  Visibility: {weather.visibility/1000:.1f} km")
        
        print(f"⏰ Updated: {weather.timestamp.strftime('%H:%M, %B %d')}")
    
    def display_forecast(self, forecast: List[ForecastItem]):
        """Display forecast information."""
        print(f"\n{Fore.BLUE}{'='*50}")
        print(f"{Fore.BLUE}  24-HOUR FORECAST")
        print(f"{Fore.BLUE}{'='*50}{Style.RESET_ALL}")
        
        for item in forecast:
            time_str = item.datetime.strftime('%H:%M')
            temp_color = Fore.RED if item.temperature > 25 else Fore.CYAN
            print(f"{time_str} | {temp_color}{item.temperature:5.1f}{self.unit_symbol}{Style.RESET_ALL} | {item.description}")
    
    def display_error(self, message: str):
        """Display error message."""
        print(f"\n{Fore.RED}❌ Error: {message}{Style.RESET_ALL}")
    
    def display_loading(self, message: str):
        """Display loading message."""
        print(f"\n{Fore.YELLOW}⏳ {message}...{Style.RESET_ALL}")
    
    def ask_for_forecast(self) -> bool:
        """Ask user if they want to see forecast."""
        response = input(f"\n{Fore.MAGENTA}Would you like to see the 24-hour forecast? (y/n): {Style.RESET_ALL}").lower()
        return response in ['y', 'yes']
    
    def ask_continue(self) -> bool:
        """Ask user if they want to check another city."""
        response = input(f"\n{Fore.MAGENTA}Check weather for another city? (y/n): {Style.RESET_ALL}").lower()
        return response in ['y', 'yes']