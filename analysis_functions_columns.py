import pandas as pd
import numpy as np

def analyze_columns_with_missing_values_by_loan_status(df):
    """
    Analyzes columns grouped by 'loan_status' based on their null value percentage between 0% and 40%.
    Returns a dictionary where each key is a column name, and the value is a DataFrame containing
    descriptive statistics for that column grouped by 'loan_status'.
    """
    results = {}
    # Calculate missing values percentage and filter columns
    missing_percentage = df.isnull().mean() * 100
    filtered_columns = df.loc[:, (missing_percentage > 0) & (missing_percentage <= 40)].columns

    # Define which percentiles to include in the description
    percentiles = [0.0, 0.25, 0.5, 0.75, 1.0]

    for col in filtered_columns:
        # Group the data by 'loan_status'
        grouped = df.groupby('loan_status')[col]

        # Check the data type and calculate statistics accordingly
        if df[col].dtype in ['float64', 'int64']:
            description = grouped.describe(percentiles=percentiles).unstack()
            description.columns = ['count', 'mean', 'std', 'min', '0%', '25%', '50%', '75%', '100%']
            description.drop(columns=['std'], inplace=True)  # Optionally drop std if not required
            description['median'] = grouped.median()
            description['missing %'] = grouped.apply(lambda x: x.isnull().mean() * 100)
            results[col] = description.reset_index()
        else:
            # Calculate stats for non-numeric columns
            mode = grouped.apply(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
            top_freq = grouped.apply(lambda x: x.value_counts().iloc[0] if not x.value_counts().empty else np.nan)
            unique = grouped.nunique()
            count = grouped.count()
            missing_percentage = grouped.apply(lambda x: x.isnull().mean() * 100)

            # Combine all non-numeric stats into a DataFrame
            stats = pd.DataFrame({
                'count': count,
                'unique': unique,
                'top': mode,
                'freq': top_freq,
                'missing %': missing_percentage
            })
            results[col] = stats

    return results

def analyze_columns_by_loan_status(df):
    """
    Analyzes columns grouped by 'loan_status' based on their null value percentage of 0%.
    Returns a dictionary where each key is a column name, and the value is a DataFrame containing
    descriptive statistics for that column grouped by 'loan_status'.
    """
    results = {}
    # Calculate missing values percentage and filter columns
    missing_percentage = df.isnull().mean() * 100
    filtered_columns = df.loc[:, (missing_percentage == 0)].columns

    # Define which percentiles to include in the description
    percentiles = [0.0, 0.25, 0.5, 0.75, 1.0]

    for col in filtered_columns:
        # Group the data by 'loan_status'
        grouped = df.groupby('loan_status')[col]

        # Check the data type and calculate statistics accordingly
        if df[col].dtype in ['float64', 'int64']:
            description = grouped.describe(percentiles=percentiles).unstack()
            description.columns = ['count', 'mean', 'std', 'min', '0%', '25%', '50%', '75%', '100%']
            description.drop(columns=['std'], inplace=True)  # Optionally drop std if not required
            description['median'] = grouped.median()
            description['missing %'] = grouped.apply(lambda x: x.isnull().mean() * 100)
            results[col] = description.reset_index()
        else:
            # Calculate stats for non-numeric columns
            mode = grouped.apply(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
            top_freq = grouped.apply(lambda x: x.value_counts().iloc[0] if not x.value_counts().empty else np.nan)
            unique = grouped.nunique()
            count = grouped.count()
            missing_percentage = grouped.apply(lambda x: x.isnull().mean() * 100)

            # Combine all non-numeric stats into a DataFrame
            stats = pd.DataFrame({
                'count': count,
                'unique': unique,
                'top': mode,
                'freq': top_freq,
                'missing %': missing_percentage
            })
            results[col] = stats

    return results

def export_report_to_excel(report_dict, filename):
    """
    Export the report dictionary to an Excel file, each dictionary key as a separate sheet.
    """
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        for col, data in report_dict.items():
            sheet_name = col[:31]  # Sheet names are limited to 31 characters
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"Report exported successfully to {filename}")

def main():
    # df = pd.read_csv("your_dataset.csv")  # Adjust the file path as needed

    # Analyze the dataset for columns with missing values
    results_missing_values = analyze_columns_with_missing_values_by_loan_status(df)

    # Export the report to an Excel file
    export_report_to_excel(results_missing_values, 'statistics_columns_with_missing_values.xlsx')

    # Analyze the dataset for columns with no missing values
    results_no_missing_values = analyze_columns_by_loan_status(df)

    # Export the report to an Excel file
    export_report_to_excel(results_no_missing_values, 'complete_columns_statistics.xlsx')

if __name__ == "__main__":
    main()
