from flask import Flask, jsonify, request
import json
from flask_caching import Cache 

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
cache = Cache(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/services/<name>')
@cache.cached(timeout=30, query_string=True)
def details(name):
    with open('shows_homeland.json', 'r') as f:
        file_data = json.load(f)
        filtered_data = [d for d in file_data['_embedded']['episodes'] if name in d['name'].lower()]
        f.close()
    if filtered_data is not None:
        return jsonify(message_status='success', data=filtered_data, status_code=200), 200
    else:
        return jsonify(message_status='Movie not Found', status_code=404), 404


@app.route('/services/<int:id>', methods = ['PUT', 'GET'])
@cache.cached(timeout=30, query_string=True)
def update_summary(id):
    if request.method == 'POST' or request.method == 'PUT':
        summary = request.get_json(force=True)
        if summary is not None:
            with open('shows_homeland.json', 'r') as f:
                file_data = json.load(f)
                f.close()
            for i in file_data['_embedded']['episodes']:
                if i['id'] == int(id):
                    i['summary'] = summary['summary']
                    return jsonify(message_status='success', data=i, status_code=200), 200
                else:
                    return jsonify(message_status='ID not Found', status_code=404), 404
            
    if request.method == 'GET':
        with open('shows_homeland.json', 'r') as f:
            file_data = json.load(f)
            filtered_data = [d for d in file_data['_embedded']['episodes'] if d['id']==id]
            f.close()
        if filtered_data is not None:
            return jsonify(message_status='success', data=filtered_data, status_code=200), 200
        return jsonify(message_status='no data found', status_code=404), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)