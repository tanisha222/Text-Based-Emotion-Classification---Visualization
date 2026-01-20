document.addEventListener('DOMContentLoaded', () => {
    const predictBtn = document.getElementById('predict-btn');
    const reviewInput = document.getElementById('review-input');
    const resultDiv = document.getElementById('result-div');

    predictBtn.addEventListener('click', () => {
        const tweetText = reviewInput.value;

        if (!tweetText) {
            resultDiv.innerHTML = "Please enter some text.";
            return;
        }

        resultDiv.innerHTML = "Analyzing...";

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ tweet: tweetText }),
        })
        .then(response => response.json())
        .then(data => {
            const emotion = data.emotion;
            resultDiv.innerHTML = `Predicted Emotion: ${emotion}`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = "An error occurred. Please try again.";
        });
    });
});