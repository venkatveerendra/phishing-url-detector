import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import extract_features

# Simple dataset (you can expand this later with a bigger phishing dataset)
data = {
    'url': [
        "https://google.com", 
        "http://192.168.1.1/login",
        "http://phishing.com@fake.com",
        "https://secure-paypal.com.fake.xyz",
        "https://openai.com"
    ],
    'label': [0, 1, 1, 1, 0]   # 0 = Safe, 1 = Phishing
}

df = pd.DataFrame(data)

X = [extract_features(u) for u in df['url']]
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained & saved as phishing_model.pkl")
