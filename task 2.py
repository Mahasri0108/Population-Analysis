# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:12:22 2025

@author: Lenovo
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df = pd.read_csv(r"C:\Users\Lenovo\Downloads\titanic\train.csv")
print(titanic_df.head())
# Set the plot style
sns.set_style("whitegrid")

# Survival rate by gender
plt.figure(figsize=(6,4))
sns.barplot(x="Sex", y="Survived", data=titanic_df, palette="coolwarm")
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

# Survival rate by passenger class
plt.figure(figsize=(6,4))
sns.barplot(x="Pclass", y="Survived", data=titanic_df, palette="viridis")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

# Age distribution of survivors vs non-survivors
plt.figure(figsize=(8,5))
sns.histplot(titanic_df, x="Age", hue="Survived", kde=True, bins=30, palette="coolwarm", element="step")
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()