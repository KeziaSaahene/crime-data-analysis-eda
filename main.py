print("Hello, VS Code!")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Crime_Reports_20240701.csv')

#Exploring the data
print(data.head())
print(data.describe())


#Cleaning the data
#Checking dor missing values
print(data.isna().sum())

# Drop rows with missing 'Crime Date Time'
data = data.dropna(subset=['Crime Date Time'])
print("After dropping rows with missing 'Crime Date Time':")

# Fill missing 'Reporting Area' with the median
data['Reporting Area'] = data['Reporting Area'].fillna(data['Reporting Area'].median())
print("After filling missing 'Reporting Area':")

# Fill missing 'Neighborhood' with "Unknown"
data['Neighborhood'] = data['Neighborhood'].fillna('Unknown')
print("After filling missing 'Neighborhood':")

# Fill missing 'Location' with "Unknown Location"
data['Location'] = data['Location'].fillna('Unknown Location')
print("After filling missing 'Location':")

print(data.isna().sum())

#Correctring the data types
print(data.dtypes)

# Addressing Crime Date Time 
# Convert Crime Date Time to datetime
# Extract start times
data['Start Time'] = data['Crime Date Time'].str.extract(r'(.+?) -')[0]

# Convert to datetime
data['Start Time'] = pd.to_datetime(data['Start Time'], format="%m/%d/%Y %H:%M", errors='coerce')


# Addressing Date of Report 
# Convert Date of Report to datetime
data['Date of Report'] = pd.to_datetime(data['Date of Report'],  format="%m/%d/%Y %I:%M:%S %p",  # Format for "02/25/2009 07:16:00 AM"errors='coerce'
)

# Addressing crime
# # Convert Crime to 'category' dtype
data['Crime'] = data['Crime'].astype('category')  
print(data['Reporting Area'].head(199))

# Addressing Reporting Area
# Convert 'Reporting Area' to category type
data['Reporting Area'] = data['Reporting Area'].astype('category')
print(data['Reporting Area'].unique())

# Addressing Neighborhood
# Convert Neighborhood to category type
data['Neighborhood'] = data['Neighborhood'].astype('category')
print(data.dtypes)


# Checking for duplicates
print(f"Duplicate rows: {data.duplicated().sum()}")


# Save the cleaned and processed data to a CSV file
data.to_csv('processed_crime_data.csv', index=False)
print("Processed data has been saved to 'processed_crime_data.csv'.")
