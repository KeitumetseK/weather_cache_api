import requests

class WeatherAPIWrapper:
    def __init__(self, api_key, cache):
        self.api_key = api_key
        self.cache = cache
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    def get_weather_data(self, city):
        # Check cache first
        cached_data = self.cache.get(city)
        if cached_data:
            print(f"Cache hit for {city}")
            return cached_data

        # Cache miss, fetch from API
        print(f"Cache miss for {city}, fetching from API")
        url = f"{self.base_url}{city}?unitGroup=metric&key={self.api_key}&contentType=json"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} Client Error: {response.reason} for url: {url}")

        # Parse the full response
        weather_data = response.json()

        # Filter to show only the necessary fields (for example, current temperature and conditions)
        filtered_data = {
            "city": city,
            "temperature": weather_data['days'][0]['temp'],
            "humidity": weather_data['days'][0]['humidity'],
            "wind_speed": weather_data['days'][0]['windspeed'],
            "conditions": weather_data['days'][0]['conditions'],
            "precipitation": weather_data['days'][0]['precip'],
            "uv_index": weather_data['days'][0]['uvindex']
        }

        # Cache the filtered data and return it
        self.cache.set(city, filtered_data, ex=43200)  # Cache for 12 hours (43,200 seconds)
        return filtered_data

