from flask import Flask, send_from_directory, request
import json
import os

app = Flask(__name__, static_folder='dinner/build', static_url_path="/")


# @app.route('/')
# def index():
#     return send_from_directory(app.static_folder, 'index.html')


@app.route('/test', methods=['POST'])
def test():
    j = request.get_json()
    print(j)
    return "Test page"


@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        "last": "Meline"
        }


@app.route('/api', methods=["GET", "POST"])
def api():
    r = request.get_json()
    if r["first"].strip().lower() == "colby":
        return json.dumps({"msg": "Meline"})
    return json.dumps({"msg": "User Not Found"})


if __name__ == "__main__":
    app.run(debug=False, port=5000)
