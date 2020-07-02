from copy import deepcopy
from collections import defaultdict


from flask import Flask, request

import defaults


class Model:
  def __init__(self, kind, default_value):
    self.kind = kind
    self.content = defaultdict(lambda: deepcopy(default_value))

  def view(self, specimen_id):
    value = self.content[specimen_id]

    return {
      'kind': self.kind,
      'specimen_id': specimen_id,
      'data': value
    }

  def store(self, key, value):
    self.content[key] = value

    return key


models = [
  Model('IVSCC cell locations', defaults.location),
  Model('IVSCC expected cell count', 0)
]

models = {model.kind: model for model in models}

app = Flask('lims')


@app.route('/specimen_metadata/view', methods=['GET'])
def view():
  kind = request.args['kind']
  specimen_id = int(request.args['specimen_id'])

  result = models[kind].view(specimen_id)

  return {'version_number': 2, 'data': result}


@app.route('/specimen_metadata/store', methods=['POST'])
def store():
  body = request.get_json(force=True)

  kind = body['kind']
  specimen_id = int(body['specimen_id'])
  data = body['data']

  models[kind].store(specimen_id, data)

  return {'version_number': 2, 'id': specimen_id}
