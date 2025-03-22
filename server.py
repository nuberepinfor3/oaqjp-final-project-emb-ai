from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Verificar si la emoción dominante es None
    if response['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"

    # Extraer las emociones y la emoción dominante de la respuesta
    emocion_dominante = response['dominant_emotion']
    scores = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }

    # Formatear la respuesta como una cadena de texto
    formatted_response = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {scores['anger']}, "
        f"'disgust': {scores['disgust']}, "
        f"'fear': {scores['fear']}, "
        f"'joy': {scores['joy']}, "
        f"'sadness': {scores['sadness']}. "
        f"La emoción dominante es {emocion_dominante}."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)