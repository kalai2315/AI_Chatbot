from requests_html import HTMLSession

def weather():
    # Create an HTML session
    session = HTMLSession()
    
    # Define the query and URL for weather search
    query = "bangalore"
    url = f"https://www.google.com/search?q=weather+{query}"
    
    # Send a GET request with a custom user-agent
    response = session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"})
    
    # Extract weather data using CSS selectors
    temp = response.html.find('span#wob_tm', first=True).text
    unit = response.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = response.html.find('span#wob_dc', first=True).text
    
    # Return the weather information
    return f"{temp} {unit} {desc}"

# Example usage
weather_info = weather()
print(weather_info)
