import re

def extract_features(url):
    features = []
    # Length of URL
    features.append(len(url))

    # Count of dots
    features.append(url.count('.'))

    # Presence of @
    features.append(1 if '@' in url else 0)

    # Presence of https
    features.append(1 if url.startswith("https") else 0)

    # Presence of IP address
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    features.append(1 if ip_pattern.search(url) else 0)

    # Number of slashes
    features.append(url.count('/'))

    return features
