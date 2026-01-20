**Text-Based Emotion Classifier Web App**

This project is an end-to-end Natural Language Processing (NLP) application that classifies the emotion of a given text. It uses a trained Support Vector Machine (SVM) model and provides a simple web interface built with Flask to interact with the model in real-time.



**Features**

-   **Multi-Class Emotion Classification**: Classifies text into one of several emotions (e.g., happiness, sadness, worry, love).
-   **Machine Learning Backend**: Built with a robust `LinearSVC` model and `TF-IDF` for efficient text feature extraction.
-   **Interactive Web Interface**: A clean and simple UI to input text and receive an instant emotion prediction.
-   **End-to-End Pipeline**: Covers the full process from data cleaning and preprocessing to model training and deployment via a Flask API.

---

**How to Run This Project**

To get this project running on your local machine, follow these simple steps.

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tanisha222/Text-Based-Emotion-Classification---Visualization]
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Text-based-emotion-classifier-
    ```

3.  **Install the required packages:**
    All the necessary libraries are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    This will start the development server.
    ```bash
    python app.py
    ```

5.  **Open the web interface:**
    Open your web browser and go to the following address:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

You should now see the web application and can start testing it with your own sentences!

---
**Technologies Used**

This project was built using the following technologies:

-   **Backend**: Python, Flask
-   **Machine Learning**: Scikit-learn, Pandas, NLTK
-   **Frontend**: HTML, CSS, JavaScript

---

