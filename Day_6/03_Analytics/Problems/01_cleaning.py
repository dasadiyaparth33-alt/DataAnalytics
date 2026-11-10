from typing import Dict, List, Optional
import numpy as np
import pandas as pd

'''
- Object-oriented pipeline Design
- Schema Standardization(snake_case)
- String Normalization & Structural Mapping
- Remove duplicate values
- Categorical Mapping means : Like kahi pe BNG likha hai kahi pe bengaluru to unko thik karna
- Change thew Data type
- Automated Missing Value Imputation (Meadian / Mode)
- IQR - based Outlier Detection & Capping
- Logging & Type Annotations
'''

class TransactionDataCleaner:
    def __init__(self):
        pass

    def standardize_schema(self, df:pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
        print("1. Schema Standardized")
        return df

    def sanitize_text(self, df:pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        string_cols = df.select_dtypes(include=['object','string']).columns
        df[string_cols] = df[string_cols].apply(lambda col:col.str.strip())
        if "full_name" in df.columns:
            df["full_name"] = df["full_name"].str.title()
        print("2. Text Sanitization")
        return df

    def deduplicate(self, df: pd.DataFrame) -> pd.DataFrame:
            df = df.copy()
            df = df.drop_duplicates().reset_index(drop=True)
            return df


    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df_clean = (
            df.pipe(self.standardize_schema)
            .pipe(self.sanitize_text)
        )
        return df_clean

    



if __name__ == "__main__":
     # Sample dirty transaction payload
    raw_data = {
        " Customer_ID ": ["CUST_001", "CUST_002", "CUST_001", "CUST_004", "CUST_005", "CUST_006", "CUST_007"],
        " Full Name ": ["  aarav sharma ", "BHAVNA PATEL", "  aarav sharma ", "chirag gupta", "divya REDDY ", " eshan verma", "Fiona Gallagher"],
        " Purchase_Amount ": [" $1,200.50 ", " $450.00 ", " $1,200.50 ", " $89.99 ", " $15,000.00 ", " $150.25 ", np.nan],
        " Join Date ": ["2024-01-15", "2023-11-20", "2024-01-15", "2022-05-10", "2024-03-01", "2023-08-19", "2024-02-12"],
        " Region ": ["BLR", " Bengaluru ", "BLR", "MUM", " Mumbai ", "DEL", np.nan],
        " Age ": [28, 34, 28, np.nan, 42, 29, 31],
    }


    df_raw = pd.DataFrame(raw_data) 
    cleaner = TransactionDataCleaner()
    df_cleaned = cleaner.fit_transform(df_raw)
    print("=" * 100)
    print("_" * 100)
    print(df_cleaned)
    print("=" * 100)


