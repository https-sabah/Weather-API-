import requests
print("Welcome to Sabah Codes")
def get_weather(location):
    api_key = "[ Enter api ]"
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "yes"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        print(f"Location: {data['location']['name']}, {data['location']['country']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    location = input("Enter your location: ")
    if location.strip():
        get_weather(location)
    else:
        print("Please enter a valid location.")
