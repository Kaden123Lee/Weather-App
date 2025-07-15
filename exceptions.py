class WeatherAppException(Exception):
    """Base exception for weather app."""
    pass

class APIKeyError(WeatherAppException):
    """Exception raised when API key is invalid or missing."""
    pass

class CityNotFoundError(WeatherAppException):
    """Exception raised when city is not found."""
    pass

class NetworkError(WeatherAppException):
    """Exception raised when network request fails."""
    pass