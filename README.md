Overview

This project performs data cleaning and exploratory data analysis (EDA) on the Titanic dataset from Kaggle. The analysis explores relationships between variables such as survival rate, passenger class, gender, and age. The goal is to uncover patterns and trends in the data that provide insights into the factors influencing survival on the Titanic.

Dataset

The dataset used is the Titanic training dataset from Kaggle. It contains information about passengers, including their age, gender, ticket class, fare, and survival status.

Dependencies

Ensure you have the following Python libraries installed before running the notebook:

pip install pandas seaborn matplotlib

Project Structure

├── titanic_eda.py      # Python script performing EDA
├── README.md           # Project documentation
├── train.csv           # Titanic dataset (not included in repo, download from Kaggle)
└── images/             # Folder for saving generated plots

Data Cleaning

Before performing EDA, we clean the dataset by handling missing values and checking for inconsistencies.

Steps:

Check for missing values and handle them accordingly.

Convert categorical variables into appropriate formats.

Drop irrelevant columns if necessary.

Exploratory Data Analysis (EDA)

The analysis includes various visualizations using seaborn and matplotlib:

1. Survival Rate by Gender

This visualization explores the relationship between gender and survival rate.

sns.barplot(x="Sex", y="Survived", data=titanic_df, palette="coolwarm")

Insight: Female passengers had a significantly higher survival rate than males.

2. Survival Rate by Passenger Class

This visualization examines the survival rate across different ticket classes.

sns.barplot(x="Pclass", y="Survived", data=titanic_df, palette="viridis")

Insight: Passengers in first class had a much higher survival rate than those in third class.

3. Age Distribution of Survivors vs. Non-Survivors

This histogram displays the age distribution of survivors and non-survivors.

sns.histplot(titanic_df, x="Age", hue="Survived", kde=True, bins=30, palette="coolwarm", element="step")

Insight: Younger passengers had higher survival rates, possibly due to prioritization.

How to Run the Analysis

Clone the repository:

git clone https://github.com/yourusername/titanic-eda.git

Navigate to the project directory:

cd titanic-eda

Run the Python script:

python titanic_eda.py

Conclusion

This project provides insights into the Titanic dataset through data visualization and analysis. Key findings include:

Women had a higher survival rate than men.

First-class passengers had better survival chances than lower classes.

Younger passengers had higher survival rates.

Further analysis can include feature engineering and predictive modeling.# Population-Analysis
