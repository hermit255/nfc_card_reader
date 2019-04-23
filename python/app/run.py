from flask import Flask
import redis
import nfc_manager
import random

app = Flask(__name__)
app.secret_key = 'hogehoge'
rds = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def show():
  return '<html><body><h1>Receptor API mock</h1><p>last uid is : ' + rds.get('uid') + '</p><p>To emulate card touch, access <a href="/card_read_emulate">/card_read_emulate</a> then you get another UID</p></body></html>'
@app.route('/close')
def close():
  nfc_manager.close()
  return '<html><body><h1>closed</h1></body></html>'
@app.route('/store/<val>', methods=['POST'])
def store(val):
  rds.set('uid', val)
  return 'redis[\'uid\'] = ' + val
@app.route('/card_read_emulate')
def emulate():
  nfc_manager.sendToApi(str(random.randrange(10000)) + '_test_uid')
  return 'card sent uid = ' + rds.get('uid')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    print nfc_manager.connect()
