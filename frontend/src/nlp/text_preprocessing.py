import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Load dataset
data = pd.read_csv(
    r"data/processed/final_istm_data.csv",
    low_memory=False
)

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Text cleaning function
def clean_text(text):

    # Convert to lowercase
    text = str(text).lower()

    # Remove special characters but KEEP numbers
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Tokenization
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

# Apply preprocessing
data['Cleaned_Description'] = data['Incident Description'].apply(clean_text)

# Check duplicate Incident IDs
print("\nDuplicate Incident IDs:")
print(data['Incident_ID'].duplicated().sum())

# Display original vs cleaned text
print("\nSample Cleaned Output:\n")
print(
    data[
        ['Incident Description', 'Cleaned_Description']
    ].head()
)

# Display unique cleaned descriptions
print("\nUnique Cleaned Descriptions:\n")

unique_descriptions = data['Cleaned_Description'].unique()

for desc in unique_descriptions[:20]:
    print(desc)

# Save processed dataset
data.to_csv(
    r"data/processed/nlp_processed_data.csv",
    index=False
)

print("\nProcessed dataset saved successfully.")