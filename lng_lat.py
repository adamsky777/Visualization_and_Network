import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
# Load CSV file into pandas dataframe
df = pd.read_csv("NAME.csv")
print(df)

# Initialize geolocator
geolocator = Nominatim(user_agent="my_app")

# Define a function to get the latitude and longitude of a city
def get_coordinates(city):
    location = geolocator.geocode(city)
    if location:
        fetch_val = "Fetched: " + city
        prGreen(str(fetch_val))
        return location.latitude, location.longitude
    else:
        return None, None

# Add columns for latitude and longitude to dataframe
df['latitude'], df['longitude'] = zip(*df['City'].apply(get_coordinates))

# Save dataframe to CSV file
df.to_csv('UPDATED.sv', index=False)

prGreen(str("Done! csv saved"))

