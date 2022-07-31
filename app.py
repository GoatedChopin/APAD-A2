from flask import Flask, send_from_directory, request
import json
import os

app = Flask(__name__, static_folder='dinner/build', static_url_path="/")


# @app.route('/')
# def index():
#     return send_from_directory(app.static_folder, 'index.html')


@app.route('/test')
def test():
    j = request.get_json()
    print(j)
    return "Test page"


@app.route('/api', methods=['GET'])
def api():
    r = request.get_json()
    os.system("echo {} > log.txt".format(r))
    # if r.strip().lower() == "colby":
    #     return json.dumps({"msg": "Meline"})
    return json.dumps({"msg": "User Not Found"})


if __name__ == "__main__":
    app.run(debug=False, port=5000)
