# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = pd.read_csv("/content/Titanic-Dataset.csv")

# Basic cleanup 
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)
df.dropna(subset=['Survived'], inplace=True)

# 1. Summary statistics
print("Summary Statistics:\n", df.describe())

# 2. Histograms for numeric features
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
df[numeric_cols].hist(bins=20, figsize=(12, 8), color='skyblue')
plt.suptitle("Histograms of Numeric Features")
plt.show()

# 3. Boxplots to understand spread and outliers
plt.figure(figsize=(12, 6))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(1, 4, i)
    sns.boxplot(y=df[col], color='lightcoral')
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

# 4. Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 5. Pairplot to see relationships
sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch', 'Survived']], hue='Survived')
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.show()

# 6. Example Plotly chart (interactive)
fig = px.histogram(df, x='Age', color='Survived', nbins=30,
                   title="Age Distribution by Survival", barmode='overlay')
fig.show()
