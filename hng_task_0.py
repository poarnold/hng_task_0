from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/', methods=['GET'])

def index():
    #current_url = request.url
    github_url = 'https://github.com/poarnold/hng_task_0'
    email = 'user-name@email.com'
    current_time = datetime.now()
    iso_time = current_time.isoformat()

    return jsonify({"email": email,
                    "current_datetime": iso_time,
                    "github_url": github_url})

if __name__ == '__main__':
    app.run()
