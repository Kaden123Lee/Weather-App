class WeatherAppException(Exception):
    pass

class APIKeyError(WeatherAppException):
    pass

class CityNotFoundError(WeatherAppException):
    pass

class NetworkError(WeatherAppException):
    pass
