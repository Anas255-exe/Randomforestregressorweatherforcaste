import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_weather_data(start_date, num_days):
    # Define weather conditions
    conditions = ["Sunny", "Rainy", "Cloudy", "Snowy", "Foggy"]

    # Generate date range
    dates = [start_date + timedelta(days=i) for i in range(num_days)]

    # Generate random data
    data = {
        "date": dates,
        "day_of_year": [date.timetuple().tm_yday for date in dates],
        "month": [date.month for date in dates],
        "temperature": np.random.uniform(low=-10, high=35, size=num_days).round(1),  # Temperature in Celsius
        "humidity": np.random.uniform(low=20, high=100, size=num_days).round(1),     # Humidity in percentage
        "wind_speed": np.random.uniform(low=0, high=50, size=num_days).round(1),     # Wind speed in km/h
        "pressure": np.random.uniform(low=950, high=1050, size=num_days).round(1),   # Pressure in hPa
        "weather_condition": np.random.choice(conditions, size=num_days)            # Weather condition
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    return df

# Parameters
start_date = datetime(2023, 1, 1)  # Start date
num_days = 365 * 5                 # Generate data for 5 years

# Generate the dataset
weather_df = generate_weather_data(start_date, num_days)

# Save the dataset to a CSV file
weather_df.to_csv("weather_dataset.csv", index=False)

print("Synthetic dataset generated and saved as 'weather_dataset.csv'.")
print(weather_df.head())