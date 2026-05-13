import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# -----------------------------
# LOAD PREPROCESSED DATA
# -----------------------------

data = pd.read_csv(
    r"data/processed/preprocessed_data.csv",
    low_memory=False
)

print("\nDataset Loaded Successfully.")

# -----------------------------
# SELECT FEATURES
# -----------------------------

features = [
    'Impact',
    'Urgency',
    'Priority',
    'No_of_Reassignments',
    'Handle_Time_hrs',
    'Region',
    'Network_Type',
    'CI_Cat',
    'Open_Month',
    'Open_Hour',
    'Resolution_Time_Hours'
]

target = 'Was_Reopened'

# -----------------------------
# KEEP REQUIRED COLUMNS
# -----------------------------

data = data[features + [target]].copy()

# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------

numeric_cols = [
    'Priority',
    'No_of_Reassignments',
    'Handle_Time_hrs',
    'Resolution_Time_Hours'
]

for col in numeric_cols:

    data[col] = pd.to_numeric(
        data[col],
        errors='coerce'
    )

    data[col] = data[col].fillna(
        data[col].median()
    )

# -----------------------------
# HANDLE CATEGORICAL MISSING VALUES
# -----------------------------

categorical_cols = [
    'Impact',
    'Urgency',
    'Region',
    'Network_Type',
    'CI_Cat'
]

for col in categorical_cols:

    data[col] = data[col].fillna(
        data[col].mode()[0]
    )

# -----------------------------
# LABEL ENCODING
# -----------------------------

encoder = LabelEncoder()

for col in categorical_cols:

    data[col] = encoder.fit_transform(
        data[col].astype(str)
    )

# -----------------------------
# FEATURES & TARGET
# -----------------------------

X = data[features]
y = data[target]

# -----------------------------
# TRAIN-TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# RANDOM FOREST MODEL
# -----------------------------

model = RandomForestClassifier(
    n_estimators=200,
    class_weight='balanced',
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# -----------------------------
# PREDICTIONS
# -----------------------------

y_pred = model.predict(X_test)

# Risk probabilities
y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------------
# INCIDENT RISK SCORES
# -----------------------------

risk_results = pd.DataFrame({
    'Actual_Reopened': y_test.values,
    'Predicted_Reopened': y_pred,
    'Reopen_Risk_Score': y_prob
})

print("\nTop High-Risk Incidents:\n")

print(
    risk_results
    .sort_values(
        by='Reopen_Risk_Score',
        ascending=False
    )
    .head(10)
)

# -----------------------------
# EVALUATION
# -----------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)