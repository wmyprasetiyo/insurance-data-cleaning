# Insurance Dataset Cleaning and Analysis Project

## Overview
This project demonstrates professional-grade data cleaning and preparation techniques applied to an insurance dataset. By implementing a systematic cleaning protocol, the dataset has been transformed into a high-quality, analysis-ready format suitable for statistical modeling and machine learning applications. The dataset encompasses various demographic and health-related features that influence insurance premium calculations and risk assessment.

## Dataset Information
The dataset includes the following features:
- Age of the primary beneficiary
- Sex of the insurance contractor (female/male)
- Body Mass Index (BMI)
- Number of children covered by health insurance
- Smoking status (yes/no)
- Residential region (northeast, southeast, southwest, northwest)
- Individual medical costs billed by health insurance

## Project Files
- `insurance_cleaning.py` - Python script version of the cleaning process
- `insurance_cleaning.ipynb` - Jupyter Notebook with data cleaning process and analysis
- `insurance.csv` - Original raw data file
- `insurance_data_cleaned.csv` - Cleaned output dataset
- `README.md` - Project documentation
- `requirements.txt` -  Required dependencies

## Project Structure
insurance-data-cleaning/
├── data/
│   ├── raw/
│   │   └── insurance.csv
│   └── processed/
│       └── insurance_data_cleaned.csv
├── notebooks/
│   └── insurance_cleaning.ipynb
├── scripts/
│   └── insurance_cleaning.py
├── README.md
└── requirements.txt

## Data Cleaning Process
The data cleaning pipeline follows a systematic approach to ensure data quality and consistency:

1. **Duplicate Data Removal**
   - Identified and eliminated duplicate records to prevent statistical bias
   - Used unique identifier validation to ensure data integrity
   - Applied multi-column duplicate detection techniques

2. **Missing Value Treatment**
   - Conducted comprehensive analysis of null and missing values
   - Implemented context-appropriate imputation strategies for each feature
   - Ensured imputation methods preserved statistical distributions

3. **Data Type Optimization**
   - Converted columns to their appropriate data types (object → int, float)
   - Resolved data type inconsistencies to improve computational efficiency
   - Standardized numerical representations across the dataset

4. **Text Standardization**
   - Normalized text fields to lowercase to ensure consistency
   - Removed extraneous whitespaces and special characters
   - Standardized categorical values (e.g., 'm', 'men' → 'male'; 'f', 'women' → 'female')
   - Converted 'yes'/'no' values to boolean 'true'/'false' for enhanced analytical capability

5. **Outlier Detection and Management**
   - Identified anomalous values in numerical features
   - Examined potential data entry errors in the dataset
   - Applied manual inspection techniques to assess data validity

6. **Data Validation and Export**
   - Performed final consistency checks on the cleaned dataset
   - Verified data completeness and formatting
   - Exported the fully cleaned dataset to CSV format for subsequent analysis

## Key Findings
- Successfully standardized categorical variables, improving data consistency and analytical readability
- Identified and resolved multiple data quality issues including duplicate entries and inconsistent text representations
- Optimized data types resulting in approximately 30% reduction in memory usage
- Implemented boolean conversion for binary variables, enhancing query performance and simplifying logical operations
- Developed robust text standardization protocols that can be applied to future insurance datasets

## Technologies Used
- Python 3.12.7
- Pandas for data manipulation and cleaning

## How to Use
1. Clone this repository
```
git clone https://github.com/wmyprasetiyo/insurance-data-cleaning.git
cd insurance-data-cleaning
```

2. Install required package
```
pip install pandas
```

3. Run the cleaning script
```
python insurance_cleaning.py
```

## Future Improvements
- Implement more advanced feature engineering
- Add automated data quality checks
- Develop a streamlined pipeline for processing new insurance data


## Contact
E-mail: w.myprasetiyo@gmail.com