import requests
from requests.utils import get_environ_proxies
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("api_key")
ACCOUNT_SID = os.getenv("account_sid")
AUTH_TOKEN = os.getenv("auth_token")
MB_TWILIO = os.getenv("mb_twilio")
MB_PERSONAL = os.getenv("mb_personal")


weather_params ={
    "lat":29.852970,
    "lon":77.875450,
    "appid":API_KEY,
    "cnt":4,
}
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data =response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today.Remember to bring an Umbrella☂️.",
        from_=MB_TWILIO,
        to=MB_PERSONAL,
    )

    print(message.status)




