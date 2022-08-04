import json
import requests

ip = requests.get('https://checkip.amazonaws.com').text.strip()

with open('my-server-parameters.json', 'r+') as f:
  data = json.load(f)
  data[1]['ParameterValue'] = ip + '/32'
  f.seek(0)       
  json.dump(data, f, indent=4)
  f.truncate()     

