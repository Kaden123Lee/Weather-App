from ui import WeatherUI
from config import Config
import sys
from api_client import WeatherAPIClient
from weather_service import WeatherService
from colorama import Fore
from colorama import Style


def main():
    """Main application entry point."""
    ui = WeatherUI()
    ui.display_welcome()
    
    try:
        # Validate configuration
        Config.validate_api_key()
        
        # Initialize services
        api_client = WeatherAPIClient(Config.API_KEY, Config.BASE_URL)
        weather_service = WeatherService(api_client)
        ui.set_unit_symbol(Config.DEFAULT_UNITS)
        
        while True:
            try:
                # Get city from user
                city = ui.get_city_input(Config.DEFAULT_CITY)
                
                # Fetch and display current weather
                ui.display_loading("Fetching current weather")
                weather_data = weather_service.get_current_weather(city, Config.DEFAULT_UNITS)
                ui.display_current_weather(weather_data)
                
                # Ask for forecast
                if ui.ask_for_forecast():
                    ui.display_loading("Fetching forecast")
                    forecast_data = weather_service.get_forecast(city, Config.DEFAULT_UNITS)
                    ui.display_forecast(forecast_data)
                
                # Ask to continue
                if not ui.ask_continue():
                    break
                    
            except ValueError as e:
                ui.display_error(str(e))
            except ConnectionError as e:
                ui.display_error(f"Connection problem: {e}")
            except Exception as e:
                ui.display_error(f"Unexpected error: {e}")
    
    except ValueError as e:
        ui.display_error(str(e))
        print(f"\n{Fore.YELLOW}To get started:")
        print(f"1. Sign up at https://openweathermap.org/api")
        print(f"2. Create a .env file with: OPENWEATHER_API_KEY=28dc0669191aed1d224f4950b8e35ff4")
        print(f"3. Run the app again{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}Thank you for using Weather App! 🌟{Style.RESET_ALL}")

if __name__ == "__main__":
    main()