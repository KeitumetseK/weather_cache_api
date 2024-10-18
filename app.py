from flask import Flask, jsonify, request
from services.weather_api import WeatherAPIWrapper
from cache.redis_cache import RedisCache

app = Flask(__name__)

# Initialize Redis cache and Weather API Wrapper
redis_cache = RedisCache()
api_key = "LC53YUZQYPQREHWKP89XRZQF4"
weather_service = WeatherAPIWrapper(api_key, redis_cache)

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get the city from the query parameters
    city_name = request.args.get('city')
    
    if not city_name:
        return jsonify({"error": "Please provide a city name."}), 400
    
    try:
        # Fetch weather data
        weather_data = weather_service.get_weather_data(city_name)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

