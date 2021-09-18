from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hello"

@app.route("/<classone>/<classtwo>")
def classes(classone, classtwo):
    return {
        "classone": classone,
        "classtwo": classtwo
    }


if __name__ == "__main__":
    app.run(port=8081)