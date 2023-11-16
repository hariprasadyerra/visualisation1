# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\SourceCode\\Downloads\\abc\\data.csv')
print(data.head())

# Load the data
data = pd.read_csv('C:\\Users\\SourceCode\\Downloads\\abc\\data.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index of the dataframe
data.set_index('Date', inplace=True)

# Plotting the line chart using pyplot
plt.figure(figsize=(14,7))  # Set the figure size for better readability

# Plot a line for each country
for column in data.columns:
    plt.plot(data.index, data[column], label=column)

# Add title and labels
plt.title('Monthly Data Trends for Pacific Countries')
plt.xlabel('Date')
plt.ylabel('Values')

# Show legend
plt.legend()

# Display the plot
plt.show()

# Calculate the total visits for each country by summing over the rows
total_visits = data.sum(numeric_only=True)  # This will exclude the Date column

# Plot the bar chart
plt.figure(figsize=(14,7))  # Set the figure size for better visibility
total_visits.plot(kind='bar', color='skyblue')  # Plot a bar chart

# Add title and labels
plt.title('Total Visits per Country')
plt.xlabel('Country')
plt.ylabel('Total Visits')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Ensure the plot is displayed properly with labels not cut off
plt.tight_layout()

# Show the plot
plt.show()
# Calculate the total flights for each country by summing over the rows
total_flights = data.sum(numeric_only=True)  # This excludes non-numeric columns such as 'Date'

# Create a pie chart
plt.figure(figsize=(10,10))  # Set the figure size for a clear, visible pie chart
plt.pie(total_flights, labels=total_flights.index, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Total Flights as Percentage of Total')

# Show the pie chart
plt.show()