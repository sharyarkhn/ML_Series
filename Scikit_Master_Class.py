# ========================================================================================================
                # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            # SCRIPT ROADMAP What Gonna Cover In This Series
                # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#   [PART A: MACHINE LEARNING THEORY FOUNDATIONS]
#   └── Intro: Scikit-Learn Toolkit, Supervised & Unsupervised Learning Definitions
#
#   [PART B: CORE DATA PREPROCESSING PIPELINE]
#   ├── MODULE 1: Data Cleaning (Detecting Nulls & Filling Blanks via Mean Imputation)
#   ├── MODULE 2: Categorical Encoding (Label Encoding vs. One-Hot Encoding Text)
#   └── MODULE 3: Feature Scaling (StandardScaler Z-Score vs. MinMaxScaler 0-1 Bounds)
#
#   [PART C: SUPERVISED MACHINE LEARNING FLOW]
#   ├── MODULE 4: Train-Test Split Architecture (Dividing Textbook/Training vs. Exam/Testing)
#   ├── MODULE 5: Supervised Models Training & Prediction Cycles (.fit() and .predict())
#   │             ├── Sub-Component A: Linear Regression (Continuous Numeric Trends)
#   │             ├── Sub-Component B: Logistic Regression (Binary Group Classification)
#   │             ├── Sub-Component C: K-Nearest Neighbors / KNN (Proximity Classification)
#   │             └── Sub-Component D: Decision Tree Classifier (Rule-Based Tree Choices)
#   ├── MODULE 6: Classification Evaluation Metrics (Accuracy, Precision, Recall, F1 & Confusion Matrix)
#   └── MODULE 7: Regression Performance Evaluation Metrics (Error tracking via MAE, MSE, RMSE)
#
#   [PART D: UNSUPERVISED PREPROCESSING & CLUSTERING PIPELINE]
#   └── MODULE 8: Advanced Customer Analytics Data Pipeline
#                 ├── Step 1: Multi-Dimensional Standard Feature Scaling
#                 ├── Step 2: Principal Component Analysis (Compressing 4D Data down to 2D PCA)
#                 ├── Step 3: K-Means Clustering Segmentation (Grouping Patterns Unsupervised)
#                 └── Step 4: Visual Data Mapping (Plotting Clusters & Centroids using Matplotlib)
#
#   [PART E: PARADIGM COMPARISON SUMMARY TABLE]
#   └── MODULE 9: Supervised vs Unsupervised Structured Matrix (Pandas Console Layout Output)
# ========================================================================================================













            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #                     INTRODUCTION TO MACHINE LEARNING WITH SCIKIT-LEARN
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>


# REQUIRED LIBRARIES:
# - sklearn (Scikit-learn): The core machine learning library used to train models and evaluate performance.
# - pandas: Used to organize data into clean rows and columns.
# - numpy: Used to handle fast mathematical operations and arrays.
# - matplotlib: Used to generate graphs and scatter plots.

# =====================================================================
# PART 1: WHAT IS SCIKIT-LEARN?
# =====================================================================
# DEFINITION: 
# Scikit-learn (imported as sklearn) is an open-source Python library 
# that provides pre-built, optimized algorithms for preprocessing data, 
# training predictive models, tuning parameters, and evaluating accuracy.

# IN SIMPLE WORDS: 
# Think of Scikit-learn as a massive, pre-made toolbox for building AI. 
# Instead of forcing you to write thousands of lines of difficult mathematical 
# formulas from scratch, it gives you ready-to-use commands. With simple tools 
# like .fit() to tell the model to learn and .predict() to make it guess, you 
# can build machine learning programs instantly.


# =====================================================================
# PART 2: SUPERVISED LEARNING
# =====================================================================
# DEFINITION: 
# Supervised learning is a machine learning paradigm where a model is 
# trained on a dataset that contains both the input variables (features) 
# and the correct target answers (labels). It maps inputs to known outputs.

# IN SIMPLE WORDS: 
# This is like studying for an exam with an answer key at the back of 
# the textbook. You give the computer questions along with the correct 
# answers. The model guesses, checks the answer key to see how wrong it 
# was, fixes its internal settings, and tries again. It repeats this until 
# it learns the underlying patterns so well that it can predict answers 
# for brand-new questions it has never seen before.


# =====================================================================
# PART 3: UNSUPERVISED LEARNING
# =====================================================================
# DEFINITION: 
# Unsupervised learning is a machine learning paradigm where the model 
# analyzes a dataset that contains only input characteristics (features) 
# without any corresponding target answers or human-made labels.

# IN SIMPLE WORDS: 
# This is like giving someone a giant, unorganized pile of random documents 
# and saying, 'I don't know what these are, but group them into piles based 
# on whatever patterns or similarities you can find.' Because there is no 
# answer key, the computer uses geometry and mathematics to check how close 
# data points sit next to each other, finding hidden structures and automatic 
# groupings entirely on its own.












            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #                            Supervised Learning(ML)
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>

import io
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, mean_absolute_error, mean_squared_error
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 1: DATA CLEANING & HANDLING MISSING VALUES (NULL VALUES)
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - pandas: Used to create DataFrames and handle missing data with functions like isnull() and fillna().
# import pandas as pd

# YOUR ORIGINAL DEFINITION: Checking for Null. It tells us about the percentage of missing data.
# 
# HUMAN-WRITTEN EXPLANATION: Out in the real world, datasets are messy and 
# almost always have missing pieces because people forget to fill out forms or 
# sensors glitch out. We represent these empty spaces as 'None' or 'NaN'. 
# Before we pass data to an AI model, we have to deal with these blanks. 
# A common trick is "Imputation"—which just means filling in the blanks with 
# something smart, like the mathematical average (Mean) of that column.

print("="*70)
print("MODULE 1: CLEANING DATA")
print("="*70)

raw_data = {
    "Name" : ["sherry", "Wasio", "Nisar", "hasaan", "Narejo"],
    "Age" : [25, None, 43, None, 99],
    "Salary" : [5000, 40322, None, 34565, None]
}

df_missing = pd.DataFrame(raw_data)
print("Initial Dataset with missing values:\n", df_missing)

# Checking the missing data patterns
print("\nTotal Null Count per column:\n", df_missing.isnull().sum())
print("\nPercentage of missing data:\n", df_missing.isnull().mean() * 100)

# Filling missing values with the column averages
df_missing['Age'].fillna(df_missing['Age'].mean(), inplace=True)
df_missing['Salary'].fillna(df_missing['Salary'].mean(), inplace=True)
print("\nDataset after Mean Imputation:\n", df_missing)
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 2: ENCODING CATEGORICAL VALUES (TEXT TO NUMBERS)
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - pandas: Used to read text data and generate One-Hot encoded tables via get_dummies().
# - io: Provides StringIO to read raw text strings directly into data tables.
# - sklearn.preprocessing.LabelEncoder: Converts categorical text strings into single numbers.

# import io
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder


# YOUR ORIGINAL DEFINITION: Since we know ML doesn't understand text like 
# "Audi inhales petrol". ML can't understand text, so encoding is used. 
# We tell ML: if you see Audi, it means 123; if petrol, it means 234.
# Label Encoding: Used when we have two possibilities (Male-Female, Yes-No). 
# It sets text categories with a number like male->0 or female->1.
# One-Hot Encoding: Used when we have more than two possibilities like a city 
# with 4 unique colonies, using formats like [0,0,0,1], [1,0,0,0].
#
# HUMAN-WRITTEN EXPLANATION: Machine learning models are essentially massive 
# calculators; they only understand numbers. If you feed them text words like 
# "Mumbai" or "Female", they crash. Encoding is the translation process.
# 1. Label Encoding works perfectly for binary choices (Yes/No, True/False). 
#    It assigns a simple 0 or 1.
# 2. One-Hot Encoding is used for columns with multiple options that don't 
#    have a natural order (like Cities). If you labeled cities 0, 1, 2, 3, the 
#    computer might think city 3 is "greater than" city 0. One-Hot encoding 
#    creates a new column for every city and flags it with 1s and 0s.

print("="*70)
print("MODULE 2: CATEGORICAL ENCODING")
print("="*70)

datastr = """Name,Gender,City,Passed
Aman,Male,Delhi,Yes
Priya,Female,Mumbai,Yes
Rahul,Male,Bangalore,No
Anjali,Female,Mumbai,Yes
Ravi,Male,Delhi,Yes
Meera,Female,Chennai,No
Arjun,Male,Bangalore,Yes
Neha,Female,Delhi,Yes
Imran,Male,Chennai,No
Sneha,Female,Mumbai,Yes
Raj,Male,Chennai,Yes
Divya,Female,Delhi,No
Kabir,Male,Mumbai,Yes
Simran,Female,Bangalore,Yes
Karan,Male,Delhi,No
Pooja,Female,Mumbai,Yes
Rakesh,Male,Chennai,Yes
Isha,Female,Delhi,No
Rohit,Male,Delhi,Yes
Deepa,Female,Bangalore,Yes"""

df_categorical = pd.read_csv(io.StringIO(datastr))

# --- Approach A: Label Encoding ---
df_label = df_categorical.copy()
le = LabelEncoder()
df_label["Gender_Encoded"] = le.fit_transform(df_label['Gender'])
df_label["Passed_Encoded"] = le.fit_transform(df_label['Passed'])

print("Label Encoded Output (Binary columns transformed to 0 and 1):")
print(df_label[['Name', 'Gender', 'Gender_Encoded', 'Passed', 'Passed_Encoded']].head(6))

# --- Approach B: One-Hot Encoding ---
# pd.get_dummies converts categorical text into separate binary columns
df_onehot = pd.get_dummies(df_categorical, columns=['City'], dtype=int)
print("\nOne-Hot Encoded Output (City transformed into distinct tracking columns):")
print(df_onehot.head(4))
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 3: FEATURE SCALING (STANDARD SCALER VS MINMAX SCALER)
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - pandas: Used to wrap scaled data back into clean tables with labels.
# - sklearn.preprocessing.StandardScaler: Normalizes features to have Mean=0 and Variance=1.
# - sklearn.preprocessing.MinMaxScaler: Compresses features into a strict 0 to 1 range.
# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler

# YOUR ORIGINAL DEFINITION: It converts all the numbers into the same range 
# so that the learning model will not get confused. 
# StandardScaler: It brings the mean to 0 and standard deviation to 1. 
# Formula: Scaled = (Actual_Value - Mean) / standard_deviation.
# MinMaxScaler: It will transform numbers between 0 and 1 if you don't want 
# any negative values. Formula: Scaled = (Actual - Min) / (Max - Min).
#
# HUMAN-WRITTEN EXPLANATION: Imagine a dataset tracking people's ages (18-60) 
# and annual salaries ($20,000-$150,000). The numerical scale of salary is 
# huge compared to age. When models check distances between points, the salary 
# column completely drowns out the age column. Feature scaling fixes this bias.
# - StandardScaler squishes data so it centers tightly at 0. It is great for 
#   normally distributed patterns and naturally handles extreme numbers well.
# - MinMaxScaler forces every single value into a strict box between 0.0 and 1.0. 
#   It works beautifully when you need non-negative numbers, but it can struggle 
#   if you have a few massive, wild outliers.

print("="*70)
print("MODULE 3: FEATURE SCALING")
print("="*70)

scale_data = {
    "StudyHours" : [1, 2, 3, 4, 5],
    "TestScore" : [40, 50, 60, 70, 80]
}
df_scale = pd.DataFrame(scale_data)

# ===== Standard Scaler Implementation =====
std_scaler = StandardScaler()
standard_scaled_array = std_scaler.fit_transform(df_scale)
# Rebuilding DataFrame since fit_transform drops headers and outputs a raw matrix
df_standard = pd.DataFrame(standard_scaled_array, columns=["StudyHours", "TestScore"])
print("Standard Scaler Results (Mean focused around 0):")
print(df_standard)

# ===== MinMaxScaler Implementation =====
minmax_scaler = MinMaxScaler()
minmax_scaled_array = minmax_scaler.fit_transform(df_scale)
df_minmax = pd.DataFrame(minmax_scaled_array, columns=["StudyHours", "TestScore"])
print("\nMinMax Scaler Results (Strictly contained between 0 and 1):")
print(df_minmax)
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 4: TRAIN-TEST SPLIT ARCHITECTURE
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - pandas: Used to isolate input and output feature matrices.
# - sklearn.model_selection.train_test_split: Randomly divides datasets into training and testing portions.
# import pandas as pd
# from sklearn.model_selection import train_test_split

# YOUR ORIGINAL DEFINITION: First part will teach the model, second will 
# test the model. Why we use it: To train the model on unseen data. If we 
# give some input X and output Y, we then test it to see what if this X, 
# then what will be the Y. random_state keeps results consistent.
#
# HUMAN-WRITTEN EXPLANATION: If you give a student the exact exam questions 
# while they are studying, they will get a 100% score by simply memorizing them. 
# But you won't know if they actually learned anything. To fix this, we split 
# our dataset into two pieces before training:
# - Training Set (usually 80%): The textbook the AI model reads to learn patterns.
# - Testing Set (usually 20%): The unseen final exam we use to verify if the 
#   model can think for itself.

print("="*70)
print("MODULE 4: TRAIN-TEST SPLIT")
print("="*70)

X = df_scale[["StudyHours"]]  # Independent variables / Input Features
Y = df_scale[["TestScore"]]   # Dependent variables / Target Answers

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("X_train (Study hours model reviews during class):\n", X_train)
print("Y_train (True scores model reviews during class):\n", Y_train)
print("\nX_test (Exam question held back):\n", X_test)
print("Y_test (Exam answer key hidden away):\n", Y_test)
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 5: SUPERVISED LEARNING (REGRESSION VS CLASSIFICATION)
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - sklearn.linear_model.LinearRegression: Predicts continuous numeric outputs.
# - sklearn.linear_model.LogisticRegression: Predicts binary category groups (0 or 1).
# - sklearn.neighbors.KNeighborsClassifier: Classifies data based on the labels of closest neighbors.
# - sklearn.tree.DecisionTreeClassifier: Classifies data using a branching tree of yes/no feature questions.
# from sklearn.linear_model import LinearRegression, LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier


# YOUR ORIGINAL DEFINITION: Supervised means we teach the computer using 
# examples. Regression is used when we want to predict a continuous number. 
# Classification is used to predict fixed categories like True, False, 
# Spam, or Not Spam.
#
# HUMAN-WRITTEN EXPLANATION: Supervised learning means the computer learns by 
# looking at examples that already contain the correct answer key. It comes in 
# two main flavors depending on what you want to predict:
# 1. Regression: You want to guess a continuous numeric value (like stock prices, 
#    temperatures, or an exact exam score).
# 2. Classification: You want to guess a distinct label or category (like distinguishing 
#    an Apple from an Orange, or checking if an email is Spam or Clean).

print("="*70)
print("MODULE 5: SUPERVISED MACHINE LEARNING MODELS")
print("="*70)

# =====================================================================================
# Sub-component A: Linear Regression (Predicting a Continuous Number)
# =====================================================================================
# YOUR ORIGINAL NOTE: model.fit(X,y) handles the whole internal cycle: 
# residual error, cost function, and gradient descent. model.predict([[value]]) 
# checks using a 2D array because rows represent examples and columns represent features.

X_reg = [[1], [2], [3], [4], [5]]
y_reg = [50, 60, 70, 80, 90]

lin_model = LinearRegression()
lin_model.fit(X_reg, y_reg)  # Tuning internal weights using gradient descent

prediction_input = 6
reg_pred = lin_model.predict([[prediction_input]])
print(f"Linear Regression Prediction: If you study {prediction_input} hours, predicted score is: {reg_pred[0]}")

# =====================================================================================
# Sub-component B: Logistic Regression (Binary Classification)
# =====================================================================================
# YOUR ORIGINAL NOTE: It is also regression but used for classification to 
# group things. It gives binary output as 0 and 1. 0 means No, 1 means Yes.

X_cls = [[1], [2], [3], [4], [5]]
y_cls = [0, 1, 0, 1, 1]  # Binary targets (e.g., 0 = Fail, 1 = Pass)

log_model = LogisticRegression()
log_model.fit(X_cls, y_cls)

test_val = [[3]]
cls_pred = log_model.predict(test_val)[0]
print(f"Logistic Regression Group Prediction for input {test_val[0]}: Group {cls_pred}")

# =====================================================================================
# Sub-component C: K-Nearest Neighbors / KNN (Proximity Classification)
# =====================================================================================
# YOUR ORIGINAL NOTE: It takes decisions seeing the nearest points. If 2 out 
# of 3 people agree to go to the gym, the third person will agree as well.

X_knn = [
    [180, 7.0],
    [200, 7.5],
    [250, 8.0],
    [300, 8.5],
    [330, 9.0],
    [360, 9.5]
]
y_knn = [0, 0, 0, 1, 1, 1]  # 0 = Apple, 1 = Orange

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_knn, y_knn)

query_fruit = [[360, 9.1]]
knn_pred = knn_model.predict(query_fruit)[0]
fruit_label = "Apple" if knn_pred == 0 else "Orange"
print(f"KNN Classifier Prediction for {query_fruit[0]}: {fruit_label}")

# =====================================================================================
# Sub-component D: Decision Tree Classifier (Rule-Based Classification)
# =====================================================================================
# YOUR ORIGINAL NOTE: It is a model which takes decisions asking a series 
# of YES/NO questions based on data features.

X_tree = [
    [7, 2],  # Features for Apple
    [8, 3],  # Features for Apple
    [9, 8],  # Features for Orange
    [10, 9], # Features for Orange
]
y_tree = [0, 0, 1, 1]  # 0 = Apple, 1 = Orange

tree_model = DecisionTreeClassifier()
tree_model.fit(X_tree, y_tree)

tree_pred = tree_model.predict([[8.5, 5]])[0]
tree_label = "Apple" if tree_pred == 0 else "Orange"
print(f"Decision Tree Prediction for input [8.5, 5]: {tree_label}")
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 6: MASTERING MODEL EVALUATION METRICS
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - pandas: Used to create a clean, row-and-column table for the confusion matrix.
# - sklearn.metrics: Imports accuracy_score, precision_score, recall_score, f1_score, and confusion_matrix.
# import pandas as pd
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# YOUR ORIGINAL DEFINITIONS:
# Accuracy: What percentage of the actual numbers I guessed true. It doesn't matter what group it is.
# Precision: What percentage of the positive guesses are actually correct. Avoids false alarms.
# Recall: Out of all the real positives, what percentage did you guess perfectly? It's a search-and-rescue metric.
# F1-Score: Calculates a special average (Harmonic Mean) so you can optimize both at the same time.
#
# HUMAN-WRITTEN EXPLANATION: You can't just build a model and blindly trust it. 
# You need performance scorecards.
# - Accuracy is great if your dataset has an even mix of categories, but it lies 
#   if your dataset is highly unbalanced.
# - Precision focuses on your model's predictions. When your model rings the alarm 
#   and says "Fire!", how often is there actually a real fire? High precision 
#   means very low false alarms.
# - Recall focuses on reality. If there are 10 real fires in the city, how many 
#   of them did your model manage to spot? High recall means zero dangerous misses.
# - F1-Score balances both metrics using a Harmonic Mean. It prevents you from 
#   cheating by making a model that guesses everything is positive just to get a 
#   perfect recall score.

print("="*70)
print("MODULE 6: CLASSIFICATION METRICS & PERFORMANCE EVALUATION")
print("="*70)

y_true = [1, 0, 1, 1, 0, 1, 0]  # Ground truth answers
y_pred = [1, 0, 1, 0, 0, 1, 1]  # Predictions made by the AI

print("Evaluation Metrics Summary Scorecard:")
print("Accuracy Score : ", accuracy_score(y_true, y_pred))
print("Precision Score: ", precision_score(y_true, y_pred))
print("Recall Score   : ", recall_score(y_true, y_pred))
print("F1 Score       : ", f1_score(y_true, y_pred))

# =======Confusion Matrix Segment========
# YOUR ORIGINAL NOTE: A 2x2 report card grid. The true diagonal values (TP and TN) 
# are your correct hits. The off-diagonal values are mistakes (FP and FN). Exposes lazy models.
y_actual_cm = [1, 1, 0, 1, 0]
y_pred_cm   = [1, 1, 1, 0, 0] 

cm = confusion_matrix(y_actual_cm, y_pred_cm, labels=[1, 0])
cm_df = pd.DataFrame(cm, 
                     index=['Pred Pass (1)', 'Pred Fail (0)'], 
                     columns=['Actual Pass (1)', 'Actual Fail (0)'])
print("\nConfusion Matrix Report Card Grid:\n", cm_df)
print("\n" + "-"*50 + "\n")


# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# MODULE 7: REGRESSION ERROR METRICS (MAE, MSE, RMSE)
# <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# REQUIRED LIBRARIES:
# - numpy: Provides math tools like sqrt() to calculate square roots.
# - sklearn.metrics: Imports mean_absolute_error and mean_squared_error.
# import numpy as np
# from sklearn.metrics import mean_absolute_error, mean_squared_error

# YOUR ORIGINAL DEFINITION: Used to see how far off predictions are.
# MAE: Take the mistake difference, remove minus signs (absolute value), add them up, and divide.
# MSE: Square the mistakes first to make them big, add them all up, and divide by N. Punishes big mistakes.
# RMSE: Take the square root of the MSE. Tracks mistake size while highlighting large, dangerous misses.
#
# HUMAN-WRITTEN EXPLANATION: You can't use accuracy scores on continuous numbers 
# because being off by $1 is different from being off by $5,000. Instead, we track 
# the scale of our errors.
# - MAE (Mean Absolute Error) is simple and straightforward. It tells you that on 
#   average, your predictions are off by a steady amount (e.g., off by 5 degrees).
# - MSE (Mean Squared Error) squares the errors. If you are off by 2, the penalty 
#   is 4. If you are off by 10, the penalty jumps to 100! It severely punishes 
#   outliers.
# - RMSE (Root Mean Squared Error) brings the squared units back down to earth 
#   so it matches the original metric's units, making it easy to read while 
#   still keeping a strong penalty for massive errors.

print("="*70)
print("MODULE 7: REGRESSION PERFORMANCE METRICS")
print("="*70)

real_scores = [90, 60, 80, 100]
predict_scores = [85, 70, 70, 95]

mae_val = mean_absolute_error(real_scores, predict_scores)
mse_val = mean_squared_error(real_scores, predict_scores)
rmse_val = np.sqrt(mse_val)

print(f"Mean Absolute Error (MAE)        : {mae_val} (Straightforward average error)")
print(f"Mean Squared Error (MSE)         : {mse_val} (Penalizes larger misses exponentially)")
print(f"Root Mean Squared Error (RMSE)   : {round(rmse_val, 2)} (Brings error metrics back to original scale)")
print("\n" + "-"*50 + "\n")


















            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #                            Unsupervised Learning 
            #                 <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<
            #       <<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
            # <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>

# REQUIRED LIBRARIES:
# - numpy: Used to format numeric output displays with functions like around().
# - pandas: Organizes raw columns and components into clean tracking DataFrames.
# - sklearn.preprocessing.StandardScaler: Symmetrically normalizes feature variances.
# - sklearn.decomposition.PCA: Reduces dimensionality while preserving structural patterns.
# - sklearn.cluster.KMeans: Partitions unlabelled data based on proximity vectors.
# - matplotlib.pyplot: Handles plot generation, labeling, grids, and rendering.
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# =====================================================================================
#        ADVANCED PREPROCESSING PIPELINE (SCALING -> PCA -> CLUSTERING)
# =====================================================================================
#       <<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#                           MODULE 1: DATA INGESTION & SETUP
#       <<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DEFINITION: A data matrix is basically just a structured table where 
# you keep your raw, unorganized information. Think of it like an Excel 
# sheet where every row is a person and every column is a different detail 
# or feature about them. 
#
# WHY WE USE IT: Computers cannot look at a person and just understand 
# who they are; we have to break their characteristics down into pure 
# numbers so a machine learning algorithm can process them. Here, we track 
# 4 different numbers for each person, which means our data lives in a 
# "4-Dimensional" space that our human eyes cannot visualize on a flat screen.

data = {
    "Customer" : ['haider', 'nisar', 'hasaan', 'wasio', 'honnybun', 'sherry'],
    "Income"   : [30000, 40000, 50000, 60000, 70000, 80000],
    "Age"      : [20, 30, 40, 22, 38, 35],
    "Spending" : [100, 90, 80, 70, 60, 50],
    "Saving"   : [1000, 5000, 8000, 10000, 15000, 20000] 
}

df = pd.DataFrame(data)
X = df[['Income', 'Age', 'Spending', 'Saving']]

print("--- ORIGINAL UNPROCESSED DATAFRAME ---")
print(df)
print("\n" + "="*60 + "\n")


# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#               MODULE 2: STANDARD SCALING (Z-SCORE NORMALIZATION)
# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DEFINITION: Standard scaling is a cleaning step that takes columns 
# with completely different numerical ranges and forces them all onto 
# the same playground. It recalculates every single number so that the 
# average of the whole column becomes 0, and the numbers spread out 
# naturally by a standard deviation of 1.
#
# WHY WE USE IT: Algorithms calculate the physical distance between data 
# points to figure out how similar they are. If you leave the data alone, 
# a massive column like Income (ranging in the tens of thousands) will completely 
# swallow up a tiny column like Age (ranging from 20 to 40). The computer 
# would assume a tiny $10 change in income is way more important than a 
# 15-year gap in age. Scaling fixes this so every feature gets an equal say.

scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(X)

print("--- RESCALED DATA MATRIX (MEAN = 0, STD DEV = 1) ---")
print(np.around(scaled_matrix, 2))
print("\n" + "="*60 + "\n")


# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#               MODULE 3: PRINCIPAL COMPONENT ANALYSIS (PCA)
# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DEFINITION: PCA is a clever mathematical technique used for "dimensionality 
# reduction." Instead of just throwing away columns to simplify your dataset 
# (which deletes valuable information), PCA squashes and rotates the data, 
# blending the old columns into brand-new, imaginary columns called 
# "Principal Components."
#
# WHY WE USE IT: Since we cannot look at a 4-Dimensional graph, we use PCA 
# to flatten our 4 columns down into 2 main columns (PCA1 and PCA2). 
# - PCA1 acts like a wide-angle camera lens, capturing the biggest, most obvious 
#   pattern in the financial data.
# - PCA2 captures the next biggest remaining pattern. This allows us to plot 
#   the data on a standard 2D flat screen while keeping almost all of the 
#   original informational patterns intact.

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_matrix)

# Format the output into a new coordinate DataFrame
pca_df = pd.DataFrame(pca_result, columns=['PCA1_Main_Pattern', 'PCA2_Minor_Pattern'])

explained_variance = pca.explained_variance_ratio_
print("--- PCA MATHEMATICAL INSIGHTS ---")
print(f"PCA1 captures: {round(explained_variance[0]*100, 2)}% variance.")
print(f"PCA2 captures: {round(explained_variance[1]*100, 2)}% variance.")
print(f"Total variance retained in 2D: {round(sum(explained_variance)*100, 2)}%")
print("\nCompressed 2D Coordinates:")
print(pca_df)
print("\n" + "="*60 + "\n")


# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#                           MODULE 4: K-MEANS CLUSTERING
# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DEFINITION: K-Means is an "unsupervised" machine learning algorithm, 
# which means it groups data points together without you giving it any pre-made 
# answers or labels. The "K" is simply the number of groups you want to find. 
# It works by dropping imaginary group captains (centroids) into the data, 
# matching every point to the nearest captain, moving the captain to the center 
# of that crowd, and repeating until nobody switches teams.
#
# WHY WE USE IT: We use it to automatically find natural target audiences or 
# behaviors hidden inside the data. Instead of a human guessing who is similar 
# to whom, K-Means uses pure geometry to separate your customers into distinct, 
# organized groups based on how close they sit to each other in the data space.

kmeans_model = KMeans(n_clusters=2, random_state=42, n_init=10)
cluster_labels = kmeans_model.fit_predict(pca_df)

# Assign discovered labels back to datasets
df['Assigned_Group'] = cluster_labels
pca_df['Assigned_Group'] = cluster_labels

print("--- FINAL SEGMENTATION RESULTS ---")
print(df)
print("\n" + "="*60 + "\n")


# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
#                       MODULE 5: CLUSTER VISUALIZATION
# <<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# DEFINITION: Cluster visualization is the final step where you take the 
# abstract math groups the computer created and turn them into a real, 
# colored picture. It paints each discovered group with a unique color and 
# marks the exact spots where the group centers (centroids) landed.
#
# WHY WE USE IT: It's one thing for a computer to give you a column of 0s 
# and 1s, but seeing the data visually as separate, colored clouds makes it 
# instantly obvious if the algorithm did a good job. It allows analysts to 
# easily spot patterns, see where the boundaries lie, and present the 
# findings to others in a way that anyone can understand at a glance.

plt.figure(figsize=(9, 7))

# Loop and plot clusters with custom identifiers
for group_id in pca_df['Assigned_Group'].unique():
    group_mask = pca_df['Assigned_Group'] == group_id
    current_cluster_data = pca_df[group_mask]
    
    plt.scatter(
        current_cluster_data['PCA1_Main_Pattern'], 
        current_cluster_data['PCA2_Minor_Pattern'], 
        label=f'Customer Segment {group_id}', 
        s=150, edgecolor='k', alpha=0.85
    )

# Extract and plot the group centers (centroids)
centroids = kmeans_model.cluster_centers_
plt.scatter(
    centroids[:, 0], centroids[:, 1], 
    color='red', marker='X', s=300, 
    label='Cluster Centroids', edgecolor='black'
)

plt.xlabel('PCA1 (Financial Dynamics Axis)', fontsize=11, fontweight='bold')
plt.ylabel('PCA2 (Demographic Dynamics Axis)', fontsize=11, fontweight='bold')
plt.title('Analytics Pipeline (Scaling -> PCA -> K-Means)', fontsize=13, fontweight='bold', pad=15)
plt.legend(loc='best', frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()