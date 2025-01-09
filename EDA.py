import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the cleaned dataset from crime data cleaning project
data = pd.read_csv("C:/Users/Kezia Helena/Desktop/Crime Project/processed_crime_data.csv")


#  plot of crimes distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Crime', palette='Set2')
plt.title('Distribution of Crimes')
plt.xticks(rotation=90)


# Crime plotted by neighborhood
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='Neighborhood', palette='Set3', order=data['Neighborhood'].value_counts().index)
plt.title('Distribution of Crimes by Neighborhood')
plt.xticks(rotation=90)



# plotting a heatmap of crime frequency by neighborhood and crime type 
crime_pivot = data.pivot_table(index='Neighborhood', columns='Crime', aggfunc='size', fill_value=0)

plt.figure(figsize=(14, 8))
sns.heatmap(crime_pivot, annot=False, fmt='d', cmap='Blues', linewidths=0.5)
plt.title('Heatmap of Crime Frequency by Neighborhood and Crime Type')


