import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate date range from January 2013 to December 2020 with monthly frequency
date_range = pd.date_range(start='2013-01-01', end='2020-12-31', freq='M')

# Generate random temperatures between -5 and +35 degrees Celsius
temperatures = np.random.uniform(low=-5, high=35, size=len(date_range))

# Generate random pH values between 4 and 17
ph_values = np.random.uniform(low=4, high=7, size=len(date_range))
cod = np.random.uniform(low=0, high=4, size=len(date_range))

# Create a DataFrame
time_series_data = pd.DataFrame({
    'Date': date_range,
    'Temperature': temperatures,
    'pH': ph_values,
    'cod': cod,
})

# Display the first few rows of the dataset
print(time_series_data.head())

# Save the dataset to a CSV file
time_series_data.to_csv('time_series_dataset.csv', index=False)

# Plot Temperature and pH vs Time
plt.figure(figsize=(14, 7))

# Plot Temperature
plt.subplot(2, 1, 1)
plt.plot(time_series_data['Date'], time_series_data['Temperature'], label='Temperature', color='r')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature vs Time')
plt.legend()

# Plot pH
plt.subplot(2, 1, 2)
plt.plot(time_series_data['Date'], time_series_data['pH'], label='pH', color='b')
plt.xlabel('Date')
plt.ylabel('pH')
plt.title('pH vs Time')
plt.legend()

# Plot cod
plt.subplot(2, 1, 2)
plt.plot(time_series_data['Date'], time_series_data['cod'], label='cod', color='g')
plt.xlabel('Date')
plt.ylabel('cod')
plt.title('cod vs Time')
plt.legend()

# Plot Temperature
plt.subplot(2, 1, 1)
plt.plot(time_series_data['Date'], time_series_data['Temperature'], label='Temperature', color='r')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature vs Time')
plt.legend()
# Adjust layout and show plot
plt.tight_layout()
plt.show()