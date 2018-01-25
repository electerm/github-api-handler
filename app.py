#!/usr/bin/env python3
"""app main"""

import imp
from flask import Flask, request
import logging
imp.load_source('config', './config_default.py')

from config import conf

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def index():
  logging.info('index')
  return 'ok'

@app.route('/github-electerm-api/' + conf['apiName'], methods = ['POST'])
def github():
  data = request.data.decode("utf-8")
  data = data.encode('ascii', 'ignore').decode('ascii')
  with open(conf['githubReleaseJsonPath'], 'w') as the_file:
    the_file.write(data)
  return 'ok'

if __name__ == '__main__':
  print('server start', conf['host'], conf['port'])
  app.run(
    conf['host'],
    conf['port'],
    debug=False
  )

