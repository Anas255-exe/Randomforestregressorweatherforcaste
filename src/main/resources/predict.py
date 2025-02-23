import sys
import joblib
import pandas as pd

# Load the model
model = joblib.load(r"/workspaces/Randomforestregressorweatherforcaste/src/main/resources/weather_model.pkl")

# Function to make predictions
def predict(day_of_year, month):
    input_data = pd.DataFrame({
        'day_of_year': [day_of_year],
        'month': [month]
    })
    predictions = model.predict(input_data)
    return predictions[0]

if __name__ == "__main__":
    day_of_year = int(sys.argv[1])
    month = int(sys.argv[2])

    result = predict(day_of_year, month)
    print(','.join(map(str, result)))