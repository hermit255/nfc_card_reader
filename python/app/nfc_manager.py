import nfc
import binascii

import json
import requests

# clf = nfc.ContactlessFrontend('usb')

def connect():
  try:
    # `action` method run on nfc-card release
    # clf.connect(rdwr={'on-release':action})
    logger.info('ready to read...')
  except Exception as e:
    return e
    logger.info(e)

def close():
  try:
    clf.close()
  except Exception as e:
    logger.info(e)

def action(tag):
  try:
    uid = binascii.hexlify(tag.identifier).upper()
    send(uid)
    logger.info('Successfully sent' )
    return True
  except Exception as e:
    logger.info('Failed to send')
    return False

def sendToApi(uid):
  # input url of external api
  url = 'http://localhost:5000/store/' + uid
  data = { 'uid': uid, }
  headers = { 'Content-Type': 'application/json', }
  return requests.post(url, data=json.dumps(data).encode(), headers=headers)
