from flask import Flask
from flask import request
import redis
import json
import requests

app = Flask(__name__)

def get_redis_client():
	return redis.Redis(host='172.17.0.6', port=6379)

@app.route('/',methods=['GET'])
def hello_world():
	return 'Hello World'

@app.route('/data',methods=['GET','POST'])
def data_route():
	if request.method == 'POST':
		rd = get_redis_client()
		ml_raw = requests.get('https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json')
		rd.set('k1',ml_raw.content)
		return 'stored'
	else:
		rd = get_redis_client()
		ml_raw = rd.get('k1')
		ml_json = json.loads(ml_raw)
		return ml_json

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
