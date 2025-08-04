# Customer-Personality-Analysis-Data-Cleaning-and-Preprocessing
Cleaned and preprocessed the Customer Personality Analysis dataset by handling nulls, removing duplicates, standardizing text (gender, country, marital status), fixing data types, converting dates, and deriving age column for better customer insights and future analysis.
 Objective:

To clean and preprocess raw marketing data by handling missing values, fixing inconsistencies, standardizing formats, and preparing it for further analysis or modeling.
 
 Tools Used:

Python 3
Pandas
NumPy
CSV dataset from Kaggle

 Dataset:
 
Customer Personality Analysis dataset from Kaggle
Contains customer demographics, campaign responses, purchase behaviors, etc.

 Key Cleaning Steps (Summary of Your Code):

1. Load Dataset
The CSV file marketing_campaign.csv is loaded using pandas.read_csv() with ; as separator.

2. Initial Inspection
Display original shape and check for missing values.

3. Handle Missing Values
Fill missing values in the Income column with its mean.

Drop any remaining rows that still contain null values.

4. Remove Duplicates
Drop duplicate records to ensure data integrity.

5. Standardize Text Columns
Convert all values in Education and Marital_Status to lowercase and strip whitespace.
Group similar marital statuses (e.g., divorced, widow, etc.) under "single".

6. Standardize Gender
Convert variations of gender (e.g., F, female, m, Male) into consistent terms: "male" and "female".

7. Standardize Country Names
If a country column exists, unify common abbreviations (e.g., USA, UK, UAE) to full names.

8. Format Date
Convert Dt_Customer (customer joining date) into datetime format (dd-mm-yyyy).
Any formatting errors are coerced to NaT.

9. Rename Columns
All column names are converted to lowercase and spaces are replaced with underscores for consistency.

10. Create Derived Column
Age is calculated from Year_Birth.
Unrealistic ages (e.g., over 100) are removed from the dataset.

11. Fix Data Types
Ensure numeric columns like income, kidhome, and teenhome are of integer type.

12. Export Cleaned Data
Save the cleaned dataset as cleaned_customer_data.csv.
