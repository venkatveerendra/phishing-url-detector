import streamlit as st
import pickle
from feature_extractor import extract_features

# Load model
model = pickle.load(open("phishing_model.pkl", "rb"))

# Sidebar with your info
st.sidebar.title("👨‍💻 Developer Info")
st.sidebar.info(
    """
    **Built by:** Ch Veerendra  
    **Course:** B.Tech CSE (Cybersecurity)  
    [GitHub](https://github.com/venkatveerendra)
    """
)

# Main title
st.title("🔐 Phishing URL Detector")
st.write("This tool detects whether a URL is **Safe** or **Phishing** using Machine Learning.")

url = st.text_input("Enter URL:")

if st.button("Check URL"):
    if url:
        features = [extract_features(url)]
        prediction = model.predict(features)[0]
        if prediction == 0:
            st.success("✅ This URL looks Safe.")
        else:
            st.error("⚠️ Warning! This URL looks Suspicious/Phishing.")
    else:
        st.warning("Please enter a URL.")

# Footer
st.markdown("---")
st.markdown("© 2025 Developed by **Veerendra Veeru** | Cybersecurity Enthusiast 🚀")
