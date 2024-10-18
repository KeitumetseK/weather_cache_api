import requests
from cache.redis_cache import RedisCache



class WeatherAPIWrapper:
    def __init__(self, api_key, cache):
        self.api_key = api_key
        self.cache = cache
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    def get_weather_data(self, city):
        # Check cache first
        cached_data = self.cache.get(city)
        if cached_data:
            print("Cache hit for {}".format(city))
            return cached_data

        # Cache miss, fetch from API
        print("Cache miss for {}, fetching from API".format(city))
        url = "{}{}?unitGroup=metric&key={}&contentType=json".format(self.base_url, city, self.api_key)
        response = requests.get(url)

        
        print("Full API Response for {}: {}".format(city, response.json()))

        if response.status_code != 200:
            return {"error": "Failed to fetch data for {}, status code: {}".format(city, response.status_code)}

        
        weather_data = response.json()

        
        if 'days' not in weather_data or not weather_data['days']:
            raise Exception("Unexpected API structure: {}".format(weather_data))

        filtered_data = {
            "city": city,
            "current_conditions": {
                "datetime": weather_data['days'][0]['datetime'],
                "temp": weather_data['days'][0]['temp'],
                "humidity": weather_data['days'][0]['humidity'],
                "conditions": weather_data['days'][0]['conditions'],
            },
            "forecast": [
                {
                    "date": day['datetime'],
                    "temp": day['temp'],
                    "humidity": day['humidity'],
                    "conditions": day['conditions']
                }
                for day in weather_data['days'][:5]  
            ]
        }

        self.cache.set(city, filtered_data)

        return filtered_data


