from operator import length_hint
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import recommendation
import sys
from werkzeug.middleware.proxy_fix import ProxyFix
# from werkzeug.contrib.atom import AtomFeed
# from urllib.parse import urljoin

app = Flask(__name__)
CORS(app)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movie", methods=["POST", "GET"])
def recommend_movies():
    features = [str(x) for x in request.form.values()]
    movie_name = str(features[0])
    print(request, file=sys.stdout)
    res = recommendation.results(movie_name)
    print(jsonify(res), file=sys.stdout)
    if res is None:
        return render_template("index.html", error_message=jsonify("Movie not in database"))
    else:
        return render_template("index.html", recommended_movie=res)
    


if __name__ == "__main__":
    app.run(port=5000, debug=True)
