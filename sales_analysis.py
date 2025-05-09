import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('sales_data.csv')

# Display the first few rows of the DataFrame
print("Sales Data Analysis Info")
print("===================================")
print(df.info())


#
print("\nMising Values")
print(df.isnull().sum())

#remove quotes from column names
df.columns = df.columns.str.replace('"', '')
#clean Column names (remove spaces and lower case)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.rename(columns={
    'height(inches)': 'height_inches',
    'weight(pounds)': 'weight_pounds'
}, inplace=True)

# Optional: Print to verify
print("\nCleaned Column Names:", df.columns.tolist())


#drop empty rows 
df.dropna(inplace=True)


#summary statistics
print("\nSummary Statistics")
print("===================================")
print(df.describe())


#saved cleaned data to a new csv file
df.to_csv('cleaned_sales_data.csv', index=False)



# Show average height and weight
avg_height = df['height_inches'].mean()
avg_weight = df['weight_pounds'].mean()

print(f"\nAverage Height: {avg_height:.2f} inches")
print(f"Average Weight: {avg_weight:.2f} pounds")

# Tallest person
tallest = df[df['height_inches'] == df['height_inches'].max()]
print("\nTallest Person Data:")
print(tallest)

# Shortest person
shortest = df[df['height_inches'] == df['height_inches'].min()]
print("\nShortest Person Data:")
print(shortest)

# set the style of seaborn
sns.set(style="whitegrid")

#1 histogram of height distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['height_inches'], bins=15, kde=True, color='blue')
plt.title('Height Distribution')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('height_distribution.png')
plt.close()

#histogram of weight distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['weight_pounds'], bins=15, kde=True, color='green')
plt.title('Weight Distribution')
plt.xlabel('Weight (pounds)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('weight_distribution.png')
plt.close()

#scatter plot of height vs weight
plt.figure(figsize=(8, 5))
sns.scatterplot(x='height_inches', y='weight_pounds', data=df, color='coral')
plt.title('Height vs Weight')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.tight_layout()
plt.savefig('height_vs_weight.png')
plt.close()


print("\nGrapth saved as PNG files: height_distribution.png, weight_distribution.png, height_vs_weight.png")


