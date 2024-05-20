# dq_report.py

import pandas as pd
import numpy as np

def data_quality_report(df):
    """
    Generate a comprehensive data quality report for a DataFrame.
    The report includes statistical metrics and analysis on distribution skewness and outliers.
    """
    report = pd.DataFrame()
    for column in df.columns:
        report.at[column, 'Columns'] = column
        report.at[column, 'Missing Values'] = df[column].isna().sum()
        report.at[column, '% Missing Values'] = (df[column].isna().mean() * 100).round(2)
        report.at[column, 'Unique Values'] = df[column].nunique()
        report.at[column, 'Data Type'] = df[column].dtype

    # Compute statistics for numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        report.at[col, 'Mean'] = df[col].mean()
        report.at[col, 'Median'] = df[col].median()
        report.at[col, 'Std Deviation'] = df[col].std()
        report.at[col, 'Min'] = df[col].min()
        report.at[col, 'Max'] = df[col].max()
        report.at[col, 'q1 Outliers'] = ((df[col] < (q1 - 1.5 * iqr)).sum())
        report.at[col, 'q3 Outliers'] = ((df[col] > (q3 + 1.5 * iqr)).sum())
        skewness = df[col].skew()
        if skewness > 1:
            report.at[col, 'Distribution'] = 'Right skewed'
        elif skewness < -1:
            report.at[col, 'Distribution'] = 'Left skewed'
        else:
            report.at[col, 'Distribution'] = 'Normal'

    return report

def export_report_to_excel(report, filename="data_quality_report.xlsx"):
    """
    Export the data quality report to an Excel file, applying column width adjustments for readability.
    """
    # Define the path to the Google Drive folder
    drive_path = '/content/drive/MyDrive/Lending_Club_Analysis/Output_files/'

    with pd.ExcelWriter(drive_path + filename, engine='xlsxwriter') as writer:
        report.to_excel(writer, sheet_name='Data Quality Report', index=False)
        worksheet = writer.sheets['Data Quality Report']
        for column in report:
            col_idx = report.columns.get_loc(column)
            col_width = max(report[column].astype(str).map(len).max(), len(column)) + 1
            worksheet.set_column(col_idx, col_idx, col_width)

    print(f"Data quality report exported successfully to {filename}")

def main():
    """
    Load the dataset, generate a data quality report with advanced metrics, and export it to Excel.
    """
    # df = pd.read_csv("your_dataset.csv")  # Ensure this is correctly set to your dataset path
    report = data_quality_report(df)
    export_report_to_excel(report)

if __name__ == "__main__":
    main()