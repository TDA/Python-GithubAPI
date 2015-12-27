__author__ = 'saipc'

import json
from collections import OrderedDict

def pretty_print_json(data, file = None):
    parsed_json = json.loads(data, object_pairs_hook=OrderedDict)
    pretty_json = json.dumps(parsed_json, indent=4)
    if file:
        with open(file, 'a') as wfile:
            wfile.write(pretty_json)
    else:
        print pretty_json
