 # Student Dropout and Academic Success Prediction

## **Project Overview**
This project focuses on identifying students at risk of leaving higher education by predicting three potential outcomes: **Dropout, Enrolled, or Graduate** [1]. By leveraging machine learning, the goal is to provide educational institutions with the tools needed for **early intervention**, allowing them to prioritise support for students most likely to struggle [2], [3].

## **Data Dictionary**
The model utilizes a dataset of **37 features** derived from demographic data, socioeconomic factors, academic performance, and macroeconomic indicators [4], [5].

| Category | Key Features |
| :--- | :--- |
| **Demographic** | Marital status, Nationality, Gender, Age at enrollment [4] |
| **Socioeconomic** | Parents' qualification/occupation, Scholarship status, Debtor [6], [7] |
| **Academic** | Course, Admission grade, Curricular units (1st & 2nd semester) [8], [9] |
| **Macroeconomic** | Unemployment rate, Inflation rate, GDP [1] |

## **Methodology**

### **1. Preprocessing & Pipeline**
To ensure robustness and prevent **data leakage**, all transformations are handled within a scikit-learn **Pipeline** [10]. The preprocessing steps include:
*   **StandardScaler:** Normalises features to a unit variance [11].
*   **SelectKBest:** Selects the top features based on mutual information [11].
*   **PCA:** Reduces dimensionality to its primary principal components [11].
*   **SMOTE:** Applied to the training set only to balance the target classes (Dropout and Graduate) [12].

### **2. Model Selection**
The project evaluates several algorithms using cross-validation scores for accuracy, precision, and F1-score [13], [14]:
*   Logistic Regression
*   Decision Tree
*   Random Forest
*   XGBoost
*   **SVM** (Identified as a top-performing model) [13].

## **Fairness and Interpretability**
A core component of this notebook is the commitment to **Responsible AI**:
*   **Interpretability:** Global and local explanations are provided using **SHAP** and **LIME** to clarify how specific features (like tuition fees or age) impact a student's predicted outcome [15], [16].
*   **Fairness Audit:** The model is audited for bias across sensitive attributes, specifically **Gender, Nationality, and Scholarship status**, using metrics like **Demographic Parity** and **Equalised Odds** [17], [18], [19].

***