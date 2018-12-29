from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def entry():
    return jsonify(
        name="Hello World"
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
