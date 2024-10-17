  Weather Cache API
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

Technologies Used

Flask: Python-based web framework for API development
Redis: In-memory key-value store for caching
Visual Crossing Weather API: External API used for fetching weather data
Docker: Containerization platform for running the application
Python 3.7: Programming language used for the backend
Requests Library: For handling API requests
json: For handling data serialization and deserialization
Features
Get Weather Data: Fetch current weather information for a specified city.
Redis Caching: Caches weather data to improve performance and reduce load on the external API.
Error Handling: Gracefully handles invalid inputs and API errors.
Modular Architecture: Each component of the project (API communication, caching, and Flask routing) is modular and easy to maintain.
Setup and Installation
Prerequisites
Docker installed on your machine.
Redis installed locally or running in a container.
Steps to Run the Project
Clone the repository:

bash

Copy code
git clone https://github.com/KeitumetseK/weather_cache_api.git
cd weather_cache_api
Build and run the Docker container:

bash
Copy code
docker-compose up --build
Set environment variables:

You'll need to provide your Visual Crossing Weather API key in the environment:
makefile

Copy code
WEATHER_API_KEY=your_api_key_here
Run the Flask server: The Flask server will be running at http://localhost:5000.

Redis Setup
The project includes a docker-compose.yml file, which will automatically set up Redis within a container. If you're using a local Redis instance, ensure it is running before starting the project.

Usage
Endpoints
Get Weather Data for a City

Endpoint: /weather?city=<city_name>
Method: GET
Description: Retrieves the current weather for the specified city.

Example:
bash

Copy code
curl "http://localhost:5000/weather?city=Johannesburg"

Response Example:

json
Copy code
{
  "city": "Johannesburg",
  "temperature": "24.5°C",
  "conditions": "Partly Cloudy",
  "wind_speed": "20.0 km/h",
  "humidity": "43.4%"
}
Project Architecture
The project consists of the following key components:

Flask API: Manages the HTTP requests and handles routing.
Redis Client: Handles caching for frequently requested data.
Weather Service: Communicates with the Visual Crossing Weather API to fetch weather data.
Docker: Ensures the application and Redis run in isolated environments.
Data Flow
A user sends a request to the Flask API to retrieve weather data for a specific city.
The API checks if the weather data is available in Redis.
If cached data is found, it returns the data from Redis.
If not, it fetches the data from the Visual Crossing Weather API, stores it in Redis, and returns the data to the user.
Challenges and Solutions
Handling Large API Responses: The Visual Crossing API returns a lot of data, most of which was unnecessary for our use case. To handle this, we filtered the response to only return relevant fields like temperature, conditions, wind speed, and humidity.
Redis Setup in Docker: Redis in Docker posed issues due to systemd. We handled this by manually configuring Redis to run properly without systemd.
Invalid Inputs and Error Handling: We implemented robust error handling to manage invalid city names and API request failures, ensuring user-friendly error messages.
Future Improvements
Extended Caching: Implementing cache expiration policies to ensure data doesn't become outdated.
More Weather Metrics: Expanding the API to provide additional weather metrics such as forecasts and historical weather data.
Scalability: Implementing load balancing and scaling Redis to handle higher traffic efficiently.

Contributors
Keitumetse Kgatlhanye - https://github.com/KeitumetseK
