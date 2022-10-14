from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
	with open("tweets_test.json","r") as fp:
		json_data=json.load(fp)

	response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
	return response

if __name__ == '__main__':
   app.run()