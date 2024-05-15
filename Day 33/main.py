import requests
from datetime import datetime

MY_LAT = 56.07428613231186  # Your latitude
MY_LONG = 12.71759061741751  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])
#iss_latitude = float(53)
#iss_longitude = float(10)


def iss_position():

    if iss_latitude < (MY_LAT + 5.0) and iss_latitude > (MY_LAT - 5.0):
        if iss_longitude < (MY_LONG + 5.0) and iss_longitude > (MY_LONG - 5.0):
            return True
        else:
            return False
    else:
        return False

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
result = data["results"]
sunrise = result["sunrise"]
sunset = result["sunset"]
print(f"sunrise: {sunrise} and sunset: {sunset}")
print(iss_position())
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
