from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    emotions = emotion_detector(text_to_analyze)

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return jsonify({
        "formatted_response": response_str,
        "emotions": emotions
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
