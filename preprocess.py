import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load dataset
sdf = pd.read_csv(r"..\sensors\sensor_data.csv")

print("Original Dataset\n")
print(df)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Replace invalid values with NaN
df.loc[(df["temperature"] < -50) | (df["temperature"] > 60), "temperature"] = np.nan

df.loc[(df["humidity"] < 0) | (df["humidity"] > 100), "humidity"] = np.nan

df.loc[(df["pressure"] < 900) | (df["pressure"] > 1100), "pressure"] = np.nan

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Replace missing values with mean
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())

df["humidity"] = df["humidity"].fillna(df["humidity"].mean())

df["pressure"] = df["pressure"].fillna(df["pressure"].mean())

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extract time features
df["hour"] = df["timestamp"].dt.hour
df["minute"] = df["timestamp"].dt.minute
df["second"] = df["timestamp"].dt.second

# Normalize sensor values
scaler = MinMaxScaler()

columns = ["temperature", "humidity", "pressure"]

df[columns] = scaler.fit_transform(df[columns])

# Save processed data
df.to_csv("processed_data.csv", index=False)

print("\nProcessed Dataset\n")
print(df)

print("\nprocessed_data.csv created successfully.")