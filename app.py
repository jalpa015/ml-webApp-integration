from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import recommendation
import sys

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movie", methods=["POST"])
def recommend_movies():
    features = [str(x) for x in request.form.values()]
    movie_name = str(features[0])
    print(request, file=sys.stdout)
    res = recommendation.results(movie_name)
    print(jsonify(res))
    return render_template("index.html", recommended_movie=res)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
