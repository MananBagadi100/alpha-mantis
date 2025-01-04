from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/v3/status')
def status():
    return jsonify({"health": "All systems operational"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
