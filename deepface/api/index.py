from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/api/deepface/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}

    @app.route('/api/deepface/hello')
    def hello():
        return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
