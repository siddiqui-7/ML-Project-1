import flask
from flask import request, jsonify
from functions import *
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = flask.Flask(__name__)

@app.route("/", methods=["POST"])
def print_piped():
    if 'mes' in request.form:
        msg = request.form['mes']
        x_input = str(msg)
        print(x_input)
        x_input, pred_class, pred_proba = make_prediction(x_input)
        return flask.render_template('predictor.html',
                                     chat_in=x_input,
                                     prediction=pred_class,
                                     probability=pred_proba)
    return "No input provided", 400

@app.route("/", methods=["GET"])
def predict():
    print(request.args)
    if 'chat_in' in request.args:
        x_input, pred_class, pred_proba = make_prediction(request.args['chat_in'])
        print(x_input)
        return flask.render_template('predictor.html',
                                     chat_in=x_input,
                                     prediction_class=pred_class,
                                     prediction_prob=pred_proba)
    else: 
        return flask.render_template('predictor.html',
                                     chat_in=" ",
                                     prediction_class=" ",
                                     prediction_prob=" ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
