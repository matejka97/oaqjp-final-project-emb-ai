"""Module Server- for server connection and comunication"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """ Connection to emotion detector function"""

    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)
    response_message = str("For the given statement, the system response is " +
     f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " +
     f"'fear': {response['fear']}, 'joy': {response['joy']} and " +
     f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")
    if response['dominant_emotion'] is None:

        return "Invalid invalid text! Please try again!"
    return response_message

@app.route("/")
def render_index_html():
    """ Function for rendering the template"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "localhost", port = 5000)
