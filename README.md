## Weather Cache API##
	Table of Contents
	Project Overview
	Technologies Used
	Features
	Setup and Installation
	Usage
	Project Architecture
	Challenges and Solutions
	Future Improvements
	Contributors
	License
	Project Overview


This project is a weather data API that integrates with the Visual Crossing Weather API to provide real-time weather information for cities. The system utilizes Redis caching to store frequently requested weather data, reducing the need for repetitive API calls and improving performance.

The project is built using Flask and Redis, with Docker used for containerization. The system is designed to be modular and scalable, ensuring ease of maintenance and future expansion.

#Technologies Used
	~Flask: Python-based web framework for API development
	~Redis: In-memory key-value store for caching
	~Visual Crossing Weather API: External API used for fetching weather data
	~Python 3.7: Programming language used for the backend
	~Requests Library: For handling API requests
	~json: For handling data serialization and deserialization

#Features
	~Fetches current weather conditions and a 5-day forecast for supported cities.
	~Caches weather data using Redis to minimize external API requests and reduce latency.
	~Allows cache clearing for specified cities.
	~Supports multiple cities through dynamic city selection in query parameters.

#Prerequisites
	~Python (version 3.7 or above)
	~Redis installed locally or running in a container.
	~API Key: Obtain an API key from Visual Crossing Weather.
#Steps to Run the Project
	~Clone the repository:

	**Copy code:**
	1. git clone https://github.com/KeitumetseK/weather_cache_api.git
 	cd weather_cache_api

	2. Install dependencies:
	**Copy code**
	pip install -r requirements.txt
	
	3. Run the Redis server:
	**copy code**
	redis-server

	4. Start the Flask server:
	**Copy code**
	python main.py
	
	You'll need to provide your Visual Crossing Weather API key in the environment:
	**Copy code:**
	WEATHER_API_KEY=your_api_key_here
	Run the Flask server: The Flask server will be running at http://localhost:5000.

#Redis Setup
	~The project includes a docker-compose.yml file, which will automatically set up Redis within a container. If you're using a local Redis instance, ensure it is running before starting the project.


#Endpoints
	Get Weather Data for a City

	~Endpoint: /weather?city=<city_name>
	~Method: GET
	~Description: Retrieves current weather conditions and a 5-day forecast for a specified city. Checks cache first; if cache is stale or missing, fetches fresh data.
	~Query Parameters:
	-city (required): The name of the city to fetch weather data for.


#Example:
	**Copy code**
	curl "http://localhost:5000/weather?city=Johannesburg"

#Response Example:
		{
  		"city": "Johannesburg",
  		"temperature": "24.5°C",
  		"conditions": "Partly Cloudy",
  		"wind_speed": "20.0 km/h",
  		"humidity": "43.4%"
		}

#Clear Cache for a City
	~Endpoint: /weather/clear_cache
	~Method: POST
	~Description: Clears the cached weather data for a specified city.
	~Request Body:
		-city (required): Name of the city to clear from cache.
#Example Request:
	**Copy code**
	curl -X POST "http://localhost:5000/weather/clear_cache" -H "Content-Type: application/json" -d '{"city": "New York"}'


#Error Handling
	~Missing city parameter returns 400 status with an error message.
	~External API failure or unrecognized response structure returns 500 status with an error message.

#Redis Caching
	~Weather data for each city is cached with a 1-hour expiration policy. This allows frequently requested cities to retrieve data quickly without excessive API calls.

#Project Architecture
	The project consists of the following key components:

	~Flask API: Manages the HTTP requests and handles routing.
	~Redis Client: Handles caching for frequently requested data.
	~Weather Service: Communicates with the Visual Crossing Weather API to fetch weather data.

#Data Flow
	~A user sends a request to the Flask API to retrieve weather data for a specific city.
	~The API checks if the weather data is available in Redis.
	~If cached data is found, it returns the data from Redis.
	~If not, it fetches the data from the Visual Crossing Weather API, stores it in Redis, and returns the data to the user.

#Additional Information
	~Flask Debugging: Set debug=True in main.py when running locally.
	~Environment Variables: Configure your API key securely for production use.
	~Dependencies:
		-Flask
		-Redis
		-Requests

#Contributors
Keitumetse Kgatlhanye - https://github.com/KeitumetseK
