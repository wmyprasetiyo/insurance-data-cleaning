#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries for data manipulation and visualization if necessary
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


#Load the dataset into a Pnadas dataFrame
df = pd.read_csv(r"C:\Users\wmypr\insurance.csv")


# In[5]:


#Display the first 5 rows to get an overview of the data
df.head()


# In[7]:


#Get the dimensions of the DataFrame (rows, columns)
df.shape


# In[9]:


#Generate summary statistics for numerical columns in the DataFrame
df.describe()


# In[11]:


#Show basic info about the DataFrame (column types, non-null counts, and memory usage)
df.info()


# In[13]:


#Count the number of missing values in each column
df.isnull().sum()


# In[15]:


#Count the remaining duplicate rows in the DataFrame
df.duplicated().sum()


# In[17]:


# Remove duplicate rows from the DataFrame
df = df.drop_duplicates()


# In[19]:


# Remove dollar signs from the 'charges' column
df["charges"] = df["charges"].replace(r"[\$]", "", regex=True)

# Convert the 'charges' column to numeric values, as its dtype is still 'object'; invalid values become NaN
df["charges"] = pd.to_numeric(df["charges"], errors="coerce")


# In[27]:


#Check the first few rows to ensure the 'charges' column has been cleaned '$' and converted
df.info()


# In[29]:


df.head()


# In[31]:


# Convert any negative values in the 'age' column to positive, as age cannot be negative
df["age"] = df["age"].abs()


# In[33]:


# Convert any negative values in the 'children' column to positive, as the number of children cannot be negative
df["children"] = df["children"].abs()


# In[35]:


# Generate summary statistics to confirm no negative values in 'age' and 'children' columns
df.describe()


# In[37]:


# Replace missing values with mean or median, depending on the column distribution
df["age"] = df["age"].fillna(df["age"].mean())
df["bmi"] = df["bmi"].fillna(df["bmi"].median())
df["children"] = df["children"].fillna(df["children"].median())
df["charges"] = df["charges"].fillna(df["charges"].median())


# In[39]:


# Replace missing values in the 'sex' column with the most common value (mode)
df["sex"] = df["sex"].fillna(df["sex"].mode()[0])

# Replace missing values in the 'smoker' column with the most common value (mode)
df["smoker"] = df["smoker"].fillna(df["smoker"].mode()[0])

# Replace missing values in the 'region' column with the most common value (mode)
df["region"] = df["region"].fillna(df["region"].mode()[0])


# In[43]:


# Check if there are any remaining null values in the dataset after imputation
df.isnull().sum()


# In[45]:


# Display the unique values in the 'sex' column to check the distinct categories (e.g., 'male', 'female')
df["sex"].unique()


# In[47]:


# Display the count of each unique value in the 'sex' column to see the distribution of categories (e.g., 'male', 'female')
df["sex"].value_counts()


# In[49]:


# Standardize the values in the 'sex' column by replacing variations like 'M' and 'man' with 'male', 
# and 'F' and 'woman' with 'female' to ensure consistent representation of gender categories
df["sex"] = df["sex"].replace({"M" : "male", "man" : "male", "F" : "female", "woman" : "female"})


# In[51]:


# Display the updated count of each unique value in the 'sex' column after standardizing the categories (e.g., 'male', 'female')
df["sex"].value_counts()


# In[53]:


# Display the unique values in the 'region' column to check the distinct categories
df["region"].unique()


# In[55]:


# Convert all region names to lowercase for consistent representation
df["region"] = df["region"].str.lower()


# In[57]:


# Display the unique values in the 'region' column to check the distinct regions after standardization (e.g., 'southeast', 'southwest')
df["region"].unique()


# In[61]:


# Display the unique values in the 'smoker' column to identify any unexpected values beyond 'yes' and 'no'
df["smoker"].unique()


# In[63]:


# Round the values in the 'age' and 'children' columns to the nearest integer and convert them to integer type
# This ensures that both columns have integer values, as age and number of children should be whole numbers
df[["age", "children"]] = df[["age", "children"]].round(0).astype(int)


# In[65]:


# Round the values in the 'bmi' and 'charges' columns to 2 decimal places for consistency and better readability
df[["bmi", "charges"]] = df[["bmi", "charges"]].round(2)


# In[67]:


# Replace the 'yes' and 'no' values in the 'smoker' column with Boolean values True and False for easier analysis
df["smoker"] = df["smoker"].replace({"yes" : True, "no" : False}).astype(bool)


# In[69]:


#Display the first 5 rows of the dataset to check the updated values and overall structure of the DataFrame
df.head()


# In[71]:


# Display a summary of the DataFrame after data cleaning and preprocessing 
# to verify data types, confirm there are no missing values, and check the final structure
df.info()


# In[73]:


# Generate descriptive statistics for the numeric columns after preprocessing 
# to confirm that values are within expected ranges and outliers or anomalies have been handled
df.describe()


# In[75]:


# Save the cleaned DataFrame to a CSV file
df.to_csv("insurance_data_cleaned.csv", index=False)

