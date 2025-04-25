
# 🚀 Task 2: Exploratory Data Analysis (EDA)

## 🎯 Objective

The objective of this task was to perform **Exploratory Data Analysis (EDA)** to understand the dataset through descriptive statistics and data visualizations. This step is essential in any data science pipeline to detect patterns, trends, relationships, and anomalies that inform further modeling and analysis.

---

## 📁 Dataset

I used the **Titanic Dataset**, a classic dataset used for machine learning and analytics practice. It contains data about the passengers who were aboard the Titanic, including features like age, gender, ticket class, fare, and survival status.


---

## 🛠️ Tools and Libraries Used

- **Python** – Programming Language  
- **Pandas** – For data manipulation and analysis  
- **Matplotlib** – For basic plotting  
- **Seaborn** – For advanced statistical visualizations  
- **Plotly** – For interactive visualizations  

---

## 🧪 Step-by-Step EDA Process

### 1. 📥 Data Loading and Cleaning

```python
import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()
```

- Checked for missing values using `df.isnull().sum()`
- Filled or dropped missing values depending on the column (e.g., imputed age, dropped cabin column if too sparse)

---

### 2. 📊 Summary Statistics

Used `.describe()` and `.info()` to understand the structure and central tendencies of numeric columns:

```python
df.describe()
df.info()
```

- Identified distributions for `Age`, `Fare`, etc.
- Noted outliers and skewness

---

### 3. 🖼️ Data Visualization

#### 📌 a. Histograms for Distribution

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Age'].dropna(), kde=True)
plt.title('Age Distribution')
plt.show()
```

- Helped visualize the spread and skewness of numerical features

#### 📌 b. Boxplots for Outliers and Group Comparison

```python
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Fare Distribution by Class')
plt.show()
```

- Detected outliers in `Fare`
- Found median fare was highest in 1st class

#### 📌 c. Count Plots for Categorical Features

```python
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.show()
```

- Women had a significantly higher survival rate

#### 📌 d. Correlation Heatmap

```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```

- Found strong correlations between some variables like `Fare` and `Pclass`

#### 📌 e. Pairplot to Explore Feature Interactions

```python
sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']])
```

- Useful for visualizing how features like Age and Fare relate to survival

#### 📌 f. Plotly Interactive Visuals (Optional Enhancement)

```python
import plotly.express as px

fig = px.histogram(df, x='Age', color='Survived', barmode='overlay')
fig.show()
```

- Made visualizations more interactive and engaging

---

### 4. 🔎 Insights and Inferences

- **Gender**: Females had higher survival rates than males.
- **Class**: First-class passengers had better survival chances.
- **Age**: Children were more likely to survive than adults.
- **Fare**: Higher fare tended to correlate with higher class and better survival rates.

---

## 📚 What I Learned

- How to use **Pandas** for data exploration and cleaning
- How to create and interpret **visualizations** with Seaborn and Matplotlib
- The significance of **statistical summaries** like mean, median, and standard deviation
- How to uncover **patterns and anomalies**
- The importance of storytelling through **data visualization**

---

## ❓ Interview Preparation Topics Covered

- Exploratory Data Analysis process
- Data cleaning techniques
- Visualization best practices
- Statistical interpretation
- Feature relationships and correlation

---

## ✅ Conclusion

This task helped build a strong foundation in data exploration. By combining statistics with visualization, I was able to draw meaningful insights from raw data, a skill that is crucial in any data science or analytics role.

