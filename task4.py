import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/Rahul/Documents/New folder (3)/US_Accidents_50000_sample.csv")

# Convert Start_Time to datetime format
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract Hour and Weekday for time-based analysis
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()

# Count of accidents by hour
accidents_by_hour = df['Hour'].value_counts().sort_index()

# Count of accidents by weekday (ordered)
accidents_by_weekday = df['Weekday'].value_counts().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Top 10 weather conditions
accidents_by_weather = df['Weather_Condition'].value_counts().head(10)

# Count of accidents by severity
accidents_by_severity = df['Severity'].value_counts().sort_index()

# Create plots
fig, axs = plt.subplots(2, 2, figsize=(18, 12))

# Plot: Accidents by Hour
sns.barplot(x=accidents_by_hour.index, y=accidents_by_hour.values, ax=axs[0, 0])
axs[0, 0].set_title("Accidents by Hour of Day")
axs[0, 0].set_xlabel("Hour")
axs[0, 0].set_ylabel("Number of Accidents")

# Plot: Accidents by Weekday
sns.barplot(x=accidents_by_weekday.index, y=accidents_by_weekday.values, ax=axs[0, 1])
axs[0, 1].set_title("Accidents by Weekday")
axs[0, 1].set_xlabel("Day of Week")
axs[0, 1].set_ylabel("Number of Accidents")
axs[0, 1].tick_params(axis='x', rotation=45)

# Plot: Top Weather Conditions
sns.barplot(y=accidents_by_weather.index, x=accidents_by_weather.values, ax=axs[1, 0])
axs[1, 0].set_title("Top 10 Weather Conditions during Accidents")
axs[1, 0].set_xlabel("Number of Accidents")
axs[1, 0].set_ylabel("Weather Condition")

# Plot: Accidents by Severity
sns.barplot(x=accidents_by_severity.index, y=accidents_by_severity.values, ax=axs[1, 1])
axs[1, 1].set_title("Accidents by Severity Level")
axs[1, 1].set_xlabel("Severity (1=Low, 4=High)")
axs[1, 1].set_ylabel("Count")

# Final layout and save
plt.tight_layout()
plt.savefig("Accident_Analysis_Plots.png")
plt.show()
