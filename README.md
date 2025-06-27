🌦️ Python Weather App
This Python-based weather app is a beginner-friendly project that helps users get real-time weather updates for any location in the world. It's built using the requests library and uses the WeatherAPI to fetch current weather details.

When you run the program, it first welcomes you with the message “Welcome to Sabah Codes”. Then, it asks you to type in a location (like Delhi, New York, or Tokyo). Once you enter a location, the app connects to the WeatherAPI using an API key and sends a request to get live weather information.

If the location is valid and everything works correctly, the app displays:

The name of the city and country

The current temperature in Celsius

The weather condition (like sunny, cloudy, or rainy)

For example, if you type “Delhi”, it might show:

Location: Delhi, India  
Temperature: 34.2°C  
Condition: Partly cloudy
The app also includes basic error handling. This means if there’s a mistake—like if you enter a wrong location, the internet is not working, or the API key is invalid—the app will not crash. Instead, it will show a friendly error message so you know what went wrong.

This project is great for learning how to:

Work with external APIs

Use the requests library to make HTTP calls

Handle JSON data

Add error handling in Python programs

It’s a simple yet useful tool that shows how Python can be used to build real-world applications by connecting to online services.

🔧 Tools Used:
Python – for writing the program

WeatherAPI – to get weather data

Requests library – to make API requests

This app is a good project for students or beginners who are learning Python and want to build something practical and easy to understand.
