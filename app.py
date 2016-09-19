# movies.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  params = {'place':{'city':'Hà Nội','district':'Ba Đình'},'category':'rent','offset':0,'size':20,'price':{'lte': 0.1},'area':{'lte':30}}
  r = requests.get(
      'https://search.homify.com.vn/api/v3.0/realties/search/_filter/',
      params=params)
  return render_template('result.html', movies=json.loads(r.text)['movies'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)