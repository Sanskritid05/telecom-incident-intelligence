import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder


class TelecomPreprocessor:

    def __init__(self):

        self.file_path = 'data/preprocessed_data.csv'

        self.data = None

        self.label_encoders = {}

    # ==========================================
    # LOAD DATA
    # ==========================================

    def load_data(self):

        self.data = pd.read_csv(self.file_path)

        print('\nDataset Loaded Successfully')

        print(self.data.head())

        print('\nShape : ', self.data.shape)

        return self.data

    # ==========================================
    # BASIC CLEANING
    # ==========================================

    def basic_cleaning(self):

        self.data = self.data.drop_duplicates()

        self.data.columns = [

            col.strip().replace(' ', '_')

            for col in self.data.columns

        ]

        self.data = self.data.replace(

            [np.inf, -np.inf],

            np.nan

        )

        print('\nBasic Cleaning Completed')

        return self.data

    # ==========================================
    # HANDLE MISSING VALUES
    # ==========================================

    def handle_missing_values(self):

        numeric_columns = self.data.select_dtypes(

            include=['int64', 'float64']

        ).columns

        categorical_columns = self.data.select_dtypes(

            include=['object']

        ).columns

        # NUMERIC

        for col in numeric_columns:

            self.data[col] = self.data[col].fillna(

                self.data[col].median()

            )

        # CATEGORICAL

        for col in categorical_columns:

            self.data[col] = self.data[col].fillna(

                'Unknown'

            )

        print('\nMissing Values Handled')

        return self.data

    # ==========================================
    # FEATURE ENGINEERING
    # ==========================================

    def feature_engineering(self):

        # RESOLUTION CATEGORY

        if 'Resolution_Time_Hours' in self.data.columns:

            self.data['Resolution_Category'] = pd.cut(

                self.data['Resolution_Time_Hours'],

                bins=[0, 4, 12, 24, 9999],

                labels=[

                    'Quick',

                    'Moderate',

                    'Slow',

                    'Critical'

                ]

            )

        # PEAK HOUR INCIDENT

        if 'Open_Hour' in self.data.columns:

            self.data['Peak_Hour_Incident'] = np.where(

                self.data['Open_Hour'].between(9, 18),

                1,

                0

            )

        print('\nFeature Engineering Completed')

        return self.data

    # ==========================================
    # ENCODE CATEGORICAL FEATURES
    # ==========================================

    def encode_features(self):

        categorical_columns = self.data.select_dtypes(

            include=['object', 'category']

        ).columns

        for col in categorical_columns:

            encoder = LabelEncoder()

            self.data[col] = encoder.fit_transform(

                self.data[col].astype(str)

            )

            self.label_encoders[col] = encoder

        print('\nCategorical Encoding Completed')

        return self.data

    # ==========================================
    # EXPORT FINAL DATA
    # ==========================================

    def export_data(self):

        output_path = 'data/processed/processed_ml_data.csv'

        self.data.to_csv(

            output_path,

            index=False

        )

        print(f'\nProcessed ML Dataset Saved → {output_path}')

    # ==========================================
    # COMPLETE PIPELINE
    # ==========================================

    def run_pipeline(self):

        self.load_data()

        self.basic_cleaning()

        self.handle_missing_values()

        self.feature_engineering()

        self.encode_features()

        self.export_data()

        print('\nTelecom AI Preprocessing Pipeline Completed')


if __name__ == '__main__':

    pipeline = TelecomPreprocessor()

    pipeline.run_pipeline()