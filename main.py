from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = "segredo-teste"

@app.route('/decode', methods=['POST'])
def decode_jwt():
    token = request.json.get('token')
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify(decoded), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
