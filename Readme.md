<div align="center">

# [Predictive Model to Classify Profitable Borrowers](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/FAB%20Predictive%20model%20to%20classify%20profitable%20borrowers.pptx)

</div>

---

*Note*: If GitHub gives an error while opening Jupyter notebooks, click on this [link](https://nbviewer.org/) and paste the notebook link.

---

## Project Objective
The bank is facing significant financial losses due to loan defaults, which directly impacts profitability and risk management. To address this issue, the bank aims to develop a predictive model that can accurately identify borrowers who are likely to fully repay their loans versus those who are at risk of defaulting (Charged Off). By leveraging comprehensive data on loan applications, borrower demographics, and historical payment behavior, this project seeks to enhance the bank's loan approval process, minimize default rates, and optimize lending decisions.

## Project Goal
To improve the bank's overall financial health and customer satisfaction through data-driven insights and predictive analytics.

---

**Build a robust model that will predict whether the borrower will be profitable for the bank.** We have a dataset that consists of:
- Borrower’s identification data
- Borrower’s loan data
- Borrower’s demographic data
- Borrower’s verification data
- Date/ time data
- Borrower’s transaction data
- Borrower’s hardship data
- Borrower’s debt settlement data
- Borrower’s application data

---

## Key Steps to Achieve the Objective:

### 1. Data Quality Analysis and Data Quality Report
The first step is to assess the data quality and generate a comprehensive Data Quality report. This report includes:
- Missing value %
- Number of Unique values
- Data Types
- Descriptive statistical measures
- Type of distribution

Data Quality report and Data Cleaning and feature engineering report are generated. The script to generate this report is [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/1_DQ_checks_and_Descriptive_Statisticalal_reports.ipynb). The `data_quality_report.xlsx` can be downloaded from [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/tree/main/Data%20Quality%20Report), and the raw descriptive statistical file can be downloaded from [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/tree/main/Output%20Files).

### 2. Exploratory Data Analysis and Feature Engineering
Exploratory Data Analysis (EDA) focuses on handling missing values and outliers to prepare the dataset for modeling. The script to perform EDA is [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/2_Exploratory_Data_Analysis.ipynb). Based on the raw descriptive statistical files generated in the previous step and EDA using Python, the Data Cleaning and feature engineering reports are generated. You can download those reports from [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/tree/main/Data%20Cleaning%20and%20feature%20engineering%20report).

#### Feature Engineering: 
You can find the Data Preprocessing script [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/3_Data_preprocessing.ipynb). Based on the Data Cleaning and feature engineering reports, data preprocessing is performed to:
- Drop irrelevant columns
- Impute missing values
- Transform feature distribution
- Convert numerical variables to categorical variables using percentile distribution, binning, etc.
- Derive new features from existing features

### 3. Segmentation
Segmentation involves dividing the borrowers based on various characteristics to identify patterns and group-specific behaviors. The entire script can be found [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/4_Borrower_Segmentation.ipynb).

#### Steps for Segmentation:
1. **Data preparation for clustering**:
   - Create Dummy Variables
   - Scale the numerical variables
   - Feature elimination using variance threshold method and using correlation matrix

2. **Validate if dataset is relevant for clustering using Hopkin's test**

3. **Export prepared data** so that it can be used for classification model as well: `processed_data_for_models.csv`

4. **KMeans++ iteration for 3 different kinds of data**:
   - `processed_data_for_models`
   - Only numerical variables from `processed_data_for_models`, dropping categorical and dummy variables
   - Reduced dimensions: Dimensions of the `processed_data_for_models` are reduced using Principal Component Analysis

5. **For each of the 3 datasets**:
   - Determine optimum number of clusters using the elbow method
   - Generate silhouette scores for `optimum_k-1`, `optimum_k`, and `optimum_k+1` number of clusters

6. **Export segmented data**:
   - `segmented_processed_data.csv`: Based on the optimum cluster number for our problem statement and best silhouette score, the final KMeans++ model is created. Segments are assigned to each data point and the final dataset is exported to drive.

### Next Steps:
1. Classification based on selected features
2. Model Monitoring framework

---

## Skills Demonstrated
- **Technical Skills**: Data Preprocessing, Feature Engineering, Clustering (KMeans++, PCA), Classification Modeling, Model Evaluation, Model Monitoring, Python, Jupyter Notebooks, Data Visualization.
- **Non-Technical Skills**: Analytical Thinking, Problem Solving, Communication, Project Management.

## Important Python Packages Used
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **scikit-learn**: Machine learning algorithms and tools
- **Seaborn & Matplotlib**: Data visualization
- **Joblib**: Parallel processing
- **Scipy**: Scientific computing

---

## Author

<div align="center">
  <img src="https://user-images.githubusercontent.com/54990079/125200983-9e8a4a00-e28b-11eb-9f6d-9ec4d4b8e43a.png" alt="Souvik Ganguly" width="150" height="150">
  <h2>Souvik Ganguly</h2>
  <a href="https://www.linkedin.com/in/souvik-ganguly-ds/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</div>

---

**Connect with me**: If you would like to connect with me, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/souvik-ganguly-ds/) or email me at [souvik.ganguly.ds@gmail.com](mailto:souvik.ganguly.ds@gmail.com).

---

For more details, refer to the project presentation [here](https://github.com/ds-souvik/Predictive-model-to-classify-profitable-borrowers/blob/main/FAB%20Predictive%20model%20to%20classify%20profitable%20borrowers.pptx).
