import json
import requests
from cache.redis_cache import RedisCache
from datetime import datetime


class WeatherAPIWrapper:
    def __init__(self, api_key, cache):
        self.api_key = api_key
        self.cache = cache
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    def get_weather_data(self, city):

        cached_data = self.cache.get(city)
        if cached_data:
            try:
                # Decode the cached data from bytes to string if necessary
                if isinstance(cached_data, bytes):
                    cached_data = cached_data.decode('utf-8')

                # If the cached data is still a string, deserialize it
                if isinstance(cached_data, str):
                    cached_data = json.loads(cached_data)

                # Validate cached data: Check if it contains today's weather
                today_date = datetime.now().strftime("%Y-%m-%d")
                if cached_data['current_conditions']['datetime'] == today_date:
                    print(f"Cache hit for {city}")
                    return cached_data
                else:
                    # Invalidate old cache
                    print(f"Cache data for {city} is outdated. Deleting old cache.")
                    self.cache.delete(city)

            except (ValueError, KeyError) as e:
                print(f"Error processing cached data for {city}: {e}")
                # If there's an error with cache, invalidate it
                self.cache.delete(city)

        # Cache miss, fetch from API
        print("Cache miss for {}, fetching from API".format(city))
        url = "{}{}?unitGroup=metric&key={}&contentType=json".format(self.base_url, city, self.api_key)
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "Failed to fetch data for {}, status code: {}".format(city, response.status_code)}

        
        weather_data = response.json()

        
        if 'days' not in weather_data or not weather_data['days']:
            raise Exception("Unexpected API structure: {}".format(weather_data))

        filtered_data = []


        current_conditions = {
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

        self.cache.set(city, json.dumps(current_conditions))

        return current_conditions 

