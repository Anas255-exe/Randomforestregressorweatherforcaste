import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load the dataset
df = pd.read_csv(r"C:\Users\mdana\Downloads\development\demo\demo\src\main\resources\dataset.csv")

# Define features (X) and target variables (y)
X = df[['day_of_year', 'month']]
y = df[['temperature', 'humidity', 'wind_speed', 'pressure']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae_temperature = mean_absolute_error(y_test['temperature'], y_pred[:, 0])
mae_humidity = mean_absolute_error(y_test['humidity'], y_pred[:, 1])
mae_wind_speed = mean_absolute_error(y_test['wind_speed'], y_pred[:, 2])
mae_pressure = mean_absolute_error(y_test['pressure'], y_pred[:, 3])

print(f"Temperature - MAE: {mae_temperature:.2f}")
print(f"Humidity - MAE: {mae_humidity:.2f}")
print(f"Wind Speed - MAE: {mae_wind_speed:.2f}")
print(f"Pressure - MAE: {mae_pressure:.2f}")

# Save the model to a file
joblib.dump(model, "weather_model.pkl")
print("Model saved as 'weather_model.pkl'")