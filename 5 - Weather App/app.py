import requests

def get_weather(api_key, zip_code, country_code='us'):
    """
    Fetches weather information for a given ZIP code using the OpenWeatherMap API.

    Parameters:
        api_key (str): Your OpenWeatherMap API key.
        zip_code (str): The ZIP code for which to fetch the weather.
        country_code (str): The country code (default is 'us' for the United States).

    Returns:
        None
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=imperial"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°F")
    else:
        print("Failed to retrieve weather data. Please check your API key and ZIP code.")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    zip_code = input("Enter the ZIP code: ")
    get_weather(api_key, zip_code)
