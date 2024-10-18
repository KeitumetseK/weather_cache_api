from services.weather_api import WeatherAPIWrapper
from cache.redis_cache import RedisCache
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Redis Cache and Weather API Wrapper
api_key = "LC53YUZQYPQREHWKP89XRZQF4"
redis_cache = RedisCache()
weather_service = WeatherAPIWrapper(api_key, redis_cache)

# Define Flask route for weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        # Fetch weather data
        weather_data = weather_service.get_weather_data(city)
        
        # Return filtered data as JSON
        return jsonify(weather_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

