from flask import Flask
from flask import request
import redis
import json
import requests

app = Flask(__name__)

def get_redis_client():
	"""
	Returns redis client object for use in flask app. Hard coded for TACC isp02 port 6379 and lew2547's unique host

	Args:
		none

	Returns:
		redis client object
	"""
	return redis.Redis(host='10.98.50.43', port=6379)

@app.route('/',methods=['GET'])
def hello_world():
	return 'Hello World 2'

@app.route('/data',methods=['GET','POST'])
def data_route():
	"""
	The route has two functions. 
	For a POST request. The function updates the redis database thorugh a python redis server object. 
	For a GET request. The function returns the meteorite landind data loaded from the POST request.

	Args:
		none
	Returns
		if POST: confirmations string
		if GET: json of meteorite landing data 

	"""
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
