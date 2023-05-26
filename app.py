import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import json

def FindKeyDifference(product_links):
    results = []
    # Fetch the product data and preprocess it
    product_data = fetch_product_data(product_links)
    preprocessed_data = preprocess_data(product_data)
    # Extract features using TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(preprocessed_data['product_title'])
    # Train the classifier
    classifier = LinearSVC()
    classifier.fit(features, preprocessed_data['key_difference'])
    # Predict key differences for new product data
    new_product_data = fetch_product_data(product_links)
    new_preprocessed_data = preprocess_data(new_product_data)
    new_features = vectorizer.transform(new_preprocessed_data['product_title'])
    predictions = classifier.predict(new_features)
    # Prepare the results
    for i, link in enumerate(product_links):
        product_info = {
            'product_link': link,
            'product_title': new_preprocessed_data['product_title'][i],
            'key_difference': predictions[i]
        }
        results.append(product_info)

    return json.dumps(results, indent=2)

def fetch_product_data(product_links):
    product_data = []
    for link in product_links:
        # Fetch the product page
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the necessary information
        product_title = soup.find('h1').text.strip()
        product_data.append(product_title)
    return product_data

def preprocess_data(product_data):
    preprocessed_data = {
        'product_title': [],
        'key_difference': []
    }

    # Preprocess the product titles and key differences
    for i, title in enumerate(product_data):
        key_difference = extract_key_difference(title)
        preprocessed_data['product_title'].append(title)
        preprocessed_data['key_difference'].append(key_difference)

    return preprocessed_data

def extract_key_difference(title):
    words = title.split()
    key_difference = words[-1]
    return key_difference

def main():
    link=input("Enter the link 1: ")
    link2=input("Enter the link 2: ")
    link3=input("Enter the link 3: ")
    product_links = [link,link2,link3]

    result = FindKeyDifference(product_links)
    print(result)
    with open("results.json", "w") as f:
        json.dump(result, f)

if __name__ == '__main__':
    main()
