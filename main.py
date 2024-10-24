from services.weather_api import WeatherAPIWrapper
from cache.redis_cache import RedisCache
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = "LC53YUZQYPQREHWKP89XRZQF4"
redis_cache = RedisCache()
weather_service = WeatherAPIWrapper(api_key, redis_cache)

supported_cities = ["Johannesburg", "New York", "London", "Tokyo", "Sydney"]

@app.route('/weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    
    if not city_name:
        return jsonify({"error": "Please provide a city name."}), 400
    if city_name not in supported_cities:
        return jsonify({"error": f"{city_name} is not supported. Please choose from: {', '.join(supported_cities)}."}), 400

    try:
        # Fetch weather data
        weather_data = weather_service.get_weather_data(city_name)
        
        # Return filtered data as JSON
        return jsonify(weather_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

