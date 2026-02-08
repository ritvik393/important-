from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
    "hqadmin": "hq123",
    "commander": "cmd123"
}

complaints = []

@app.route("/")
def home():
    return "HCC Backend Running"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if users.get(data.get("username")) == data.get("password"):
        return jsonify({"msg": "Login Success"})
    return jsonify({"msg": "Invalid Login"})

@app.route("/complaint", methods=["POST"])
def complaint():
    complaints.append(request.json)
    return jsonify({"msg": "Complaint Sent to HQ"})

if __name__ == "__main__":
    app.run(debug=True)
