import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("data/spam.csv", encoding="latin-1")

# Keep only the useful columns
if "v1" in df.columns and "v2" in df.columns:
    df = df[["v1", "v2"]]
    df.columns = ["label", "text"]
elif "label" in df.columns and "message" in df.columns:
    df = df[["label", "message"]]
    df.columns = ["label", "text"]
else:
    print("Columns found:", df.columns)
    raise ValueError("Dataset format not recognized. Check column names.")

# Convert labels
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Drop missing rows
df = df.dropna()

X = df["text"]
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/spam_model.pkl")
print("Model saved successfully.")