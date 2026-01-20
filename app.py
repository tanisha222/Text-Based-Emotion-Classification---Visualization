from flask import Flask, request, jsonify, render_template
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK data if not already present
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('wordnet')


app = Flask(__name__)

# Load the trained vectorizer and SVM model
with open('vectorizer.pickle', 'rb') as handle:
    vectorizer = pickle.load(handle)

with open('svm_model.pickle', 'rb') as handle:
    svm_model = pickle.load(handle)

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    tweet_text = data['tweet']

    # Preprocess the text
    cleaned_text = preprocess_text(tweet_text)

    # Vectorize the text using the loaded vectorizer
    vectorized_text = vectorizer.transform([cleaned_text])

    # Make a prediction using the loaded SVM model
    prediction = svm_model.predict(vectorized_text)

    # Return the predicted emotion as a JSON response
    return jsonify({'emotion': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)