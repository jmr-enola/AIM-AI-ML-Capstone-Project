 # Student Dropout and Academic Success Prediction

## **Project Overview**
This project focuses on identifying students at risk of leaving higher education by predicting three potential outcomes: **Dropout, Enrolled, or Graduate**. By leveraging machine learning, the goal is to provide educational institutions with the tools needed for **early intervention**, allowing them to prioritise support for students most likely to struggle.

## **Data Dictionary**
The model utilizes a dataset of **37 features** derived from demographic data, socioeconomic factors, academic performance, and macroeconomic indicators.

| Category | Key Features |
| :--- | :--- |
| **Demographic** | Marital status, Nationality, Gender, Age at enrollment |
| **Socioeconomic** | Parents' qualification/occupation, Scholarship status, Debtor |
| **Academic** | Course, Admission grade, Curricular units (1st & 2nd semester) |
| **Macroeconomic** | Unemployment rate, Inflation rate, GDP |

## **Methodology**

### **1. Preprocessing & Pipeline**
To ensure robustness and prevent **data leakage**, all transformations are handled within a scikit-learn **Pipeline**. The preprocessing steps include:
*   **StandardScaler:** Normalises features to a unit variance.
*  **RFE:** Recursively removes less important features based on the model’s performance until the desired number of features is selected.
*   **PCA:** Reduces dimensionality to its primary principal components.
*   **SMOTE:** Applied to the training set only to balance the target classes (Dropout and Graduate).

### **2. Model Selection**
The project evaluates several algorithms using cross-validation scores for accuracy, precision, and F1-score:
*   Logistic Regression
*   Decision Tree
*   Random Forest
*   XGBoost
*   **SVM** (Identified as a top-performing model).

## **Fairness and Interpretability**
A core component of this notebook is the commitment to **Responsible AI**:
*   **Interpretability:** Global and local explanations are provided using **SHAP** and **LIME** to clarify how specific features (like tuition fees or age) impact a student's predicted outcome.
*   **Fairness Audit:** The model is audited for bias across sensitive attributes, specifically **Gender, Nationality, and Scholarship status**, using metrics like **Demographic Parity** and **Equalised Odds**.

***