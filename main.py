import pandas as pd
import numpy as np

#Load Dataset
df = pd.read_csv("marketing_campaign.csv", sep=";")


#Initial Inspection
print("Original Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

#Handle Missing Values
df['Income'] = df['Income'].fillna(df['Income'].mean())  # Fill missing income with mean
df.dropna(inplace=True)  # Drop any remaining rows with nulls

#Remove Duplicate Rows
df.drop_duplicates(inplace=True)

#Standardize Text Columns
df['Education'] = df['Education'].str.lower().str.strip()
df['Marital_Status'] = df['Marital_Status'].str.lower().str.strip()

#Fix inconsistent marital statuses
df['Marital_Status'] = df['Marital_Status'].replace({
    'together': 'married',
    'divorced': 'single',
    'widow': 'single',
    'alone': 'single',
    'absurd': 'single',
    'yo-lo': 'single'
})

#Standardize Gender
if 'Gender' in df.columns or 'gender' in df.columns:
    gender_col = 'Gender' if 'Gender' in df.columns else 'gender'
    df[gender_col] = df[gender_col].str.lower().str.strip()
    df[gender_col] = df[gender_col].replace({
        'f': 'female',
        'm': 'male',
        'male': 'male',
        'female': 'female'
    })

# Standardize Country Names (if exists)
if 'Country' in df.columns or 'country' in df.columns:
    country_col = 'Country' if 'Country' in df.columns else 'country'
    df[country_col] = df[country_col].str.lower().str.strip()
    df[country_col] = df[country_col].replace({
        'us': 'united states',
        'usa': 'united states',
        'uk': 'united kingdom',
        'u.k.': 'united kingdom',
        'uae': 'united arab emirates'
    })

# Convert Dt_Customer to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format="%d-%m-%Y", errors='coerce')

# Rename Columns (lowercase, underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Create Age Column
df['age'] = 2025 - df['year_birth']
df = df[df['age'] < 100]  # Remove unrealistic ages

# Fix Data Types
int_columns = ['income', 'kidhome', 'teenhome']
for col in int_columns:
    df[col] = df[col].astype(int)

# Save Cleaned Dataset
df.to_csv("cleaned_customer_data.csv", index=False)

# Summary Output
print(df.columns.tolist())
print("\n Cleaning Complete")
print("Cleaned Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nPreview:\n", df.head())
