import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
import joblib
import os

# Step 1: Load the dataset
df = pd.read_csv(r"C:\Users\Admin\Desktop\ecommerce_datasets\customer_messages.csv")

# Step 2: Convert text to TF-IDF features
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['message_text'])
y = df['sentiment_label']

# Step 3: Check class distribution before balancing
print("Before balancing:")
print(y.value_counts())

# Step 4: Balance the dataset using oversampling
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)

print("\nAfter balancing:")
print(pd.Series(y_resampled).value_counts())

# Step 5: Train the model
model = MultinomialNB()
model.fit(X_resampled, y_resampled)

# Step 6: Evaluate the model on the original data (optional)
y_pred = model.predict(X)
print("\nClassification Report on Original Data:")
print(classification_report(y, y_pred))

# Step 7: Save the model and vectorizer
os.makedirs("ml_models", exist_ok=True)
joblib.dump(tfidf, 'ml_models/tfidf_vectorizer.pkl')
joblib.dump(model, 'ml_models/sentiment_model.pkl')

print("\nModel and vectorizer saved successfully.")
