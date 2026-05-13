import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report
)
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import SMOTE


# ==========================================
# LOAD DATA
# ==========================================

data = pd.read_csv(
    'data/processed/processed_ml_data.csv'
)

print('\nDataset Loaded')

print(data.head())


# ==========================================
# TARGET VARIABLE
# ==========================================

TARGET_COLUMN = 'Was_Reopened'


# ==========================================
# REMOVE NON-ML COLUMNS
# ==========================================

drop_columns = [

    # IDENTIFIERS

    'Incident_ID',

    # DESCRIPTION 
    'Incident_Description',

    # TEMPORAL LEAKAGE

    'Reopen_Time',
    'Resolved_Time',
    'Close_Time',

    # POST-RESOLUTION SIGNALS

    'Handle_Time_hrs',

    # STRONG OPERATIONAL SHORTCUTS

    # 'No_of_Reassignments',

    'No_of_Related_Interactions',

    'No_of_Related_Incidents',

    'No_of_Related_Changes',


]

for col in [

    'Incident_ID',
    'Ticket_ID',
    'Description',
    'Cleaned_Description'

]:

    if col in data.columns:

        drop_columns.append(col)

data = data.drop(columns=drop_columns)


# ==========================================
# FEATURES & TARGET
# ==========================================

print('\nALL COLUMNS:\n')
print(data.columns.tolist())
X = data.drop(columns=[TARGET_COLUMN])

y = data[TARGET_COLUMN]


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(


    X,
    y,

    test_size=0.2,

    random_state=42
)

# ==========================================
# APPLY SMOTE
# ==========================================

smote = SMOTE(

    sampling_strategy=0.50,

    random_state=42
)

print('\nSMOTE Applied Successfully')

print('\nBalanced Training Distribution:\n')

print(y_train.value_counts())

# ==========================================
# MODEL
# ==========================================

model = RandomForestClassifier(

    n_estimators=80,

    max_depth=8,

    min_samples_split=20,

    min_samples_leaf=10,

    max_features='sqrt',

    class_weight={0:1, 1:2},

    random_state=42
)

print('\nFINAL TRAINING FEATURES:\n')

print(X.columns.tolist())

# ==========================================
# TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)

print('\nModel Training Completed')


# ==========================================
# PREDICTIONS
# ==========================================

y_probs = model.predict_proba(X_test)[:, 1]

threshold = 0.40

# ==========================================
# PREDICT PROBABILITIES
# ==========================================

probabilities = model.predict_proba(

    X_test

)[:, 1]


# ==========================================
# CUSTOM THRESHOLD
# ==========================================

threshold = 0.40

predictions = np.where(

    probabilities >= threshold,

    1,

    0
)

# ==========================================
# EVALUATION
# ==========================================

accuracy = accuracy_score(

    y_test,
    predictions
)

print(f'\nModel Accuracy : {accuracy:.4f}')

print('\nClassification Report:\n')

print(

    classification_report(
        y_test,
        predictions
    )
)

print('\nConfusion Matrix:\n')

print(

    confusion_matrix(
        y_test,
        predictions
    )
)

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(

    model,

    'models/reopen_prediction_model.pkl'
)

print(

    '\nModel Saved → models/reopen_prediction_model.pkl'
)