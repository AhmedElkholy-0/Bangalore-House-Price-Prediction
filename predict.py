import joblib
import json
import numpy as np

# Load model and column metadata
model = joblib.load('bangalore_house_price_model.pkl')
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

def predict_price(location, sqft, bath, balcony, bhk):
    # Find location index or default to 'other'
    loc_index = -1
    full_loc_name = 'location_' + location.lower()
    
    if full_loc_name in data_columns:
        loc_index = data_columns.index(full_loc_name)
    else:
        loc_index = data_columns.index('location_other')

    # Prepare feature array
    x = np.zeros(len(data_columns))
    x[0] = bhk        # size
    x[1] = sqft       # total_sqft
    x[2] = bath       # bath
    x[3] = balcony    # balcony
    
    if loc_index >= 0:
        x[loc_index] = 1

    # Return prediction
    return model.predict([x])[0]

# --- Interactive Mode ---
if __name__ == "__main__":
    print("--- Bangalore House Price Predictor ---")
    loc = input("Enter Location: ")
    sqft = float(input("Enter Total Sqft: "))
    bath = int(input("Enter Number of Bathrooms: "))
    balcony = int(input("Enter Number of Balconies: "))
    bhk = int(input("Enter BHK: "))
    
    price = predict_price(loc, sqft, bath, balcony, bhk)
    print(f"\nEstimated Price: {price:.2f} Lakhs")